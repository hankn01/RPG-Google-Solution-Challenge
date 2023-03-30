import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Add
from tensorflow.keras.losses import SparseCategoricalCrossentropy, CategoricalCrossentropy
from tensorflow.keras.activations import relu

def ConvBN(Input_layer, out_channel, kernel_size, padding, strides):
    x = Input_layer
    x = layers.Conv2D(out_channel,kernel_size,padding=padding,strides=strides,use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    return relu(x)

def Basic(input_layer, out_channel, down=False):
    x = input_layer
    out = x
    strides = 2 if down else 1

    x = ConvBN(x, out_channel, kernel_size=3, padding='same', strides=strides)
    x = layers.Conv2D(out_channel,3,padding='same',use_bias=False)(x)
    x = layers.BatchNormalization()(x)

    if down:
        out = layers.Conv2D(out_channel,1,strides=strides,use_bias=False)(out)
        out = layers.BatchNormalization()(out)

    return relu(Add()([x, out]))

def Bottleneck(input_layer, in_channel, mid_channel, out_channel, down=False):
    x = input_layer
    out = x
    strides = 2 if down else 1

    x = ConvBN(x, mid_channel, kernel_size=1, padding='valid', strides=strides)
    x = ConvBN(x, mid_channel, kernel_size=3, padding='same', strides=1)
    x = layers.Conv2D(out_channel,1,use_bias=False)(x)
    x = layers.BatchNormalization()(x)

    if down:
        out = layers.Conv2D(out_channel,1,strides=strides,use_bias=False)(out)
        out = layers.BatchNormalization()(out)

    if in_channel != out_channel and not down:
        out = layers.Conv2D(out_channel,1,strides=strides,use_bias=False)(out)
        out = layers.BatchNormalization()(out)

    return relu(Add()([x, out]))

def ResNet(input_layer=Input(shape=(224,224,3)), block='Bottleneck', num_layer=[3,4,6,3], num_class=5, out_channel=64, optimizer='adam', loss=SparseCategoricalCrossentropy):
    x = input_layer
    x = ConvBN(x, out_channel, kernel_size=7, padding='same', strides=2)
    x = layers.MaxPooling2D(pool_size=3, strides=2, padding='same')(x)

    # Cov_Blocks
    if block == 'Basic':
        for _ in range(num_layer[0]):
            x = Basic(x, out_channel)

        x = Basic(x, out_channel*2, down=True)
        for _ in range(num_layer[1]-1):
            x = Basic(x, out_channel*2)

        x = Basic(x, out_channel*4, down=True)
        for _ in range(num_layer[2]-1):
            x = Basic(x, out_channel*4)

        x = Basic(x, out_channel*8, down=True)
        for _ in range(num_layer[3]-1):
            x = Basic(x, out_channel*8)
    elif block == 'Bottleneck':
        x = Bottleneck(x, out_channel, out_channel, out_channel*4)
        for _ in range(num_layer[0]-1):
            x = Bottleneck(x, out_channel*4, out_channel, out_channel*4)

        x = Bottleneck(x, out_channel*4, out_channel*2, out_channel*8, down=True)
        for _ in range(num_layer[1]-1):
            x = Bottleneck(x, out_channel*8, out_channel*2, out_channel*8)

        x = Bottleneck(x, out_channel*8, out_channel*4, out_channel*16, down=True)
        for _ in range(num_layer[2]-1):
            x = Bottleneck(x, out_channel*16, out_channel*4, out_channel*16)

        x = Bottleneck(x, out_channel*16, out_channel*8, out_channel*32, down=True)
        for _ in range(num_layer[3]-1):
            x = Bottleneck(x, out_channel*32, out_channel*8, out_channel*32)    

    # Fully_Connected_layer
    x = layers.AveragePooling2D(padding='same')(x)
    x = layers.Flatten()(x)
    x = layers.Dense(num_class)(x)

    model = Model(
      inputs=input_layer,
      outputs=x
    )

    # Model Compiling
    model.compile(optimizer=optimizer,
                      loss=loss(from_logits=True),
                      metrics=['accuracy'])
    return model