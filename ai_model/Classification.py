import os
import argparse
import pathlib
import matplotlib.pyplot as plt
import numpy as np
import random
import PIL
import tensorflow as tf
import imp

from tensorflow import keras
from tensorflow.keras import layers, Input, Model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Add
from tensorflow.keras.losses import SparseCategoricalCrossentropy, CategoricalCrossentropy
from tensorflow.keras.activations import relu
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from AlexNet import AlexNet
from VGGNet import VGGNet
from ResNet import ResNet

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, default='CPU',
                       help='Choose CPU or GPU')
    parser.add_argument('--gpu_number', type=str, default=0,
                       help='Using GPU number')
    parser.add_argument('--model', type=str, default='AlexNet',
                        help='Choose a model (AlexNet, VGGNet, ResNet)')
    parser.add_argument('--config', type=str, default=os.path.join('.', 'config','alexnet.py'),
                        help='Path of model parameter file')
    parser.add_argument('--checkp', type=str, default=os.path.join('.', 'checkpoint'),
                        help='Path of model check point')
    parser.add_argument('--data_path', type=str, default=os.path.join('..','data','plants'),
                        help='Root directory of dataset')
    parser.add_argument('--seed', type=int, default=42,
                       help='Random seed')
    parser.add_argument('--mode', type=str, default='train',
                       help='Train mode or Prediction(pred) mode')
    parser.add_argument('--image_path', type=str, default=os.path.join('..','data','test_image','test01.jpg'),
                        help="Path of the image")
    args_opt = parser.parse_args()
    
    # Set Config File Path
    config_path = args_opt.config
    config = imp.load_source("",config_path).config
    
    # Set Random Seed
    random.seed(args_opt.seed)
    np.random.seed(args_opt.seed)
    os.environ["PYTHONHASHSEED"] = str(args_opt.seed)
    
    # Dataset 만들어야 함
    data_dir = pathlib.Path(os.path.join(os.getcwd(), args_opt.data_path))
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=config['valid_data_ratio'],
        subset="training",
        seed=args_opt.seed,
        image_size=(config['image_size'], config['image_size']),
        batch_size=config['batch_size'])
    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=config['valid_data_ratio'],
        subset="validation",
        seed=args_opt.seed,
        image_size=(config['image_size'], config['image_size']),
        batch_size=config['batch_size'])
    
    # 성능을 높이도록 데이터셋 구성
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    
    class_names = train_ds.class_names
    # print(class_names)
    
    # Mode
    if args_opt.mode === 'train':
        # Creating Model
        if args_opt.model == 'AlexNet':
            model = AlexNet(
                input_layer=Input(shape=(config['image_size'],config['image_size'],3)), 
                num_class=len(class_names), 
                base_channel=config['base_channel'], 
                optimizer='adam', 
                loss=SparseCategoricalCrossentropy)
        elif args_opt.model == 'VGGNet':
            model = vgg16(
                input_layer=Input(shape=(config['image_size'],config['image_size'],3)), 
                num_layer=config['num_layer'], 
                num_class=len(class_names), 
                base_channel=config['base_channel'], 
                optimizer='adam', 
                loss=SparseCategoricalCrossentropy)
        elif args_opt.model == 'ResNet':
            model = resnet34(
                input_layer=Input(shape=(config['image_size'],config['image_size'],3)), 
                block=config['block'], 
                num_layer=config['num_layer'], 
                num_class=len(class_names), 
                out_channel=config['base_channel'], 
                optimizer='adam', 
                loss=SparseCategoricalCrossentropy)
        # print(model.summary())
        
        # Training Steps
        if args_opt.device == 'CPU':
            with tf.device(f'/device:{args_opt.device}:0'):
                history = model.fit(
                  train_ds,
                  validation_data=val_ds,
                  epochs=config['epochs']
                )
        elif args_opt.device == 'GPU':
            with tf.device(f'/device:{args_opt.device}:{args_opt.gpu_number}'):
                history = model.fit(
                  train_ds,
                  validation_data=val_ds,
                  epochs=config['epochs']
                )
        # 
        model.save(f'{args_opt.checkp}/{args_opt.model}')
        
    elif args_opt.mode === 'pred':
        image = PIL.Image.open(args_opt.image_path)
        image = np.array(image)
        
        model = keras.models.load_model(f'{args_opt.config}/{args_opt.model}')
        
        pred = model.predict(image)
        pred = np.argmax(pred)
        
        target_class = class_names[pred]