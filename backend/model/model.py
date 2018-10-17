import tflearn

from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression


SIZE = 50
LR = 0.001


cnn = input_data(shape=[None, SIZE, SIZE, 1], name='input')

cnn = conv_2d(cnn, 32, 5, activation='relu')
cnn = max_pool_2d(cnn, 5)

cnn = conv_2d(cnn, 64, 5, activation='relu')
cnn = max_pool_2d(cnn, 5)

cnn = conv_2d(cnn, 32, 5, activation='relu')
cnn = max_pool_2d(cnn, 5)

cnn = conv_2d(cnn, 64, 5, activation='relu')
cnn = max_pool_2d(cnn, 5)

cnn = conv_2d(cnn, 32, 5, activation='relu')
cnn = max_pool_2d(cnn, 5)

cnn = conv_2d(cnn, 32, 5, activation='relu')
cnn = max_pool_2d(cnn, 5)


cnn = fully_connected(cnn, 1024, activation='relu')
cnn = dropout(cnn, 0.8)

cnn = fully_connected(cnn, 2, activation='softmax')
cnn = regression(cnn, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

MODEL = tflearn.DNN(cnn, tensorboard_dir='log')
