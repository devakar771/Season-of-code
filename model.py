import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Dense, Conv2D, concatenate
# from tensorflow.keras.utils import plot_model
import numpy as np
from copy import deepcopy
import random 
import math
import matplotlib.pyplot as plt
import os

# Input
inp = Input(shape=(4, 4, 14))

# Layer 1
conv1_lay1 = Conv2D(128, kernel_size=(1, 2), strides=(1, 1), activation='relu', padding='valid')(inp)
conv2_lay1 = Conv2D(128, kernel_size=(2, 1), strides=(1, 1), activation='relu', padding='valid')(inp)

# Layer 2
conv1_lay2 = Conv2D(128, kernel_size=(1, 2), strides=(1, 1), activation='relu', padding='valid')(conv1_lay1)
conv2_lay2 = Conv2D(128, kernel_size=(2, 1), strides=(1, 1), activation='relu', padding='valid')(conv1_lay1)
conv3_lay2 = Conv2D(128, kernel_size=(1, 2), strides=(1, 1), activation='relu', padding='valid')(conv2_lay1)
conv4_lay2 = Conv2D(128, kernel_size=(2, 1), strides=(1, 1), activation='relu', padding='valid')(conv2_lay1)

# Flatten
flat1 = Flatten()(conv1_lay2)
flat2 = Flatten()(conv2_lay2)
flat3 = Flatten()(conv3_lay2)
flat4 = Flatten()(conv4_lay2)

# Concatenate
concat = concatenate([flat1, flat2, flat3, flat4], axis=-1)

# Dense
dense = Dense(256, activation='relu')(concat)

model.summary()
out = Dense(4, activation=tf.keras.activations.linear)(dense)

# learning rate decay
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate = .001,
                                                             decay_steps = 1000,
                                                             decay_rate = 0.9,
                                                             staircase = True)

# Define the Model
model = Model(inputs=[inp], outputs=[out])
model.compile(optimizer = tf.keras.optimizers.RMSprop(learning_rate=lr_schedule),
              loss = 'mse',
              metrics = ['accuracy'])

model.summary()
model.save_weights(path)
