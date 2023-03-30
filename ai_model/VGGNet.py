import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import SparseCategoricalCrossentropy, CategoricalCrossentropy
from tensorflow.keras.activations import relu

def VGGNet(input_layer=Input(shape=(224,224,3)), num_layer=[2,2,3,3,3], num_class=5, base_channel=64, optimizer='adam', loss=SparseCategoricalCrossentropy):
    modules = []
    modules += [input_layer]
    # Conv_Block_1
    modules += [layers.Conv2D(base_channel,3,padding='same',activation='relu',use_bias=False) for _ in range(num_layer[0])]
    modules += [layers.MaxPooling2D(pool_size=2,strides=2, padding='same')]
    # Conv_Block_2
    modules += [layers.Conv2D(base_channel*2,3,padding='same',activation='relu',use_bias=False) for _ in range(num_layer[1])]
    modules += [layers.MaxPooling2D(pool_size=2,strides=2, padding='same')]
    # Conv_Block_3
    modules += [layers.Conv2D(base_channel*4,3,padding='same',activation='relu',use_bias=False) for _ in range(num_layer[2])]
    modules += [layers.MaxPooling2D(pool_size=2,strides=2, padding='same')]
    # Conv_Block_4]
    modules += [layers.Conv2D(base_channel*8,3,padding='same',activation='relu',use_bias=False) for _ in range(num_layer[3])]
    modules += [layers.MaxPooling2D(pool_size=2,strides=2, padding='same')]
    # Conv_Block_5
    modules += [layers.Conv2D(base_channel*8,3,padding='same',activation='relu',use_bias=False) for _ in range(num_layer[4])]
    modules += [layers.MaxPooling2D(pool_size=2,strides=2, padding='same')]

    model = Sequential(modules)
    # Fully_Connected_layer
    model.add(layers.Flatten())
    model.add(layers.Dense(4096,activation='relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(4096,activation='relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(num_class))

    # Model Compiling
    model.compile(optimizer=optimizer,
                      loss=loss(from_logits=True),
                      metrics=['accuracy'])
    return model