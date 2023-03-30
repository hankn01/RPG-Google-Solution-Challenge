import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import SparseCategoricalCrossentropy, CategoricalCrossentropy
from tensorflow.keras.activations import relu

def AlexNet(input_layer=Input(shape=(227,227,3)), num_class=5, base_channel=96, optimizer='adam', loss=SparseCategoricalCrossentropy):
    modules = []
    modules += [input_layer]
    # Conv_Block_1
    modules += [layers.Conv2D(base_channel,11,strides=4,activation='relu',use_bias=False)]
    modules += [layers.MaxPooling2D(pool_size=3,strides=2)]
    # Conv_Block_2
    modules += [layers.Conv2D(256,5,strides=1,padding='same',activation='relu',use_bias=False)]
    modules += [layers.MaxPooling2D(pool_size=3,strides=2)]
    # Conv_Block_3
    modules += [layers.Conv2D(384,3,strides=1,padding='same',activation='relu',use_bias=False)]
    # Conv_Block_4]
    modules += [layers.Conv2D(384,3,strides=1,padding='same',activation='relu',use_bias=False)]
    # Conv_Block_5
    modules += [layers.Conv2D(256,3,strides=1,padding='same',activation='relu',use_bias=False)]
    modules += [layers.MaxPooling2D(pool_size=3,strides=2)]

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