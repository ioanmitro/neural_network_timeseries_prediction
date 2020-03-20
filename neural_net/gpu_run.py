import numpy as np
import os
import sys,re
import os.path
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.python.keras.datasets import mnist
from tensorflow.python.keras.models import Sequential,load_model
from tensorflow.python.keras.layers import Dense,Dropout,LSTM,TimeDistributed,Flatten,CuDNNLSTM,Activation,RepeatVector
from tensorflow.python.keras.optimizers import Adam
from keras.utils import plot_model
import matplotlib.pyplot as plt

# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x/10.0) ## diairw kai gia 10 gt oso pio mikra noumera exeis toso pio euko   
        y.append(seq_y/10.0) ## sugklinei
    return np.array(X), np.array(y)
def saveModel(model):
    file_name = 'theModel.h5'
    model.save(file_name)
def loadModel():
    file_name = 'theModel.h5'
    model = load_model(file_name)
    return model
if len(sys.argv)!=1:
    filename=sys.argv[1]
    if( os.path.exists('./'+filename)):

        ##Read for the parsed file to train the model 
        data = pd.read_csv(filename, sep=",", header=None)
        
        #print data

        #Get the limits
        numRow=data.shape[1]
        numCol=data.shape[0]

        #print data.shape
        n = numRow*numCol

        #print n
        #Turn to array
        data=np.array(data)
        #print data

        n_steps = 10
        X, y = split_sequence(data, n_steps)
        
        n_features = 20
        #X = X.reshape((X.shape[0], X.shape[1], n_features))
        X = X.reshape((X.shape[0], X.shape[1], n_features))

        """"
        model=Sequential()
        model.add(LSTM(200, activation= 'relu' , input_shape=(n_steps, n_features),return_sequences=True))
        model.add(LSTM(150, activation= 'relu' ))
        model.add(Dense(20))
        model.compile(optimizer= 'adam' , loss= 'mse' ,metrics=['accuracy'])
        model.fit(X, y, epochs=4000, validation_split=0.3)"""
        step_after=1;
        model=Sequential()
        model.add(CuDNNLSTM(200, input_shape=(n_steps, n_features),return_sequences=False))
        model.add(RepeatVector(step_after))
        model.add(CuDNNLSTM(150,return_sequences=False))
        model.add(Dense(n_features))
        model.add(Activation('linear'))
        model.compile(optimizer= 'rmsprop' , loss= 'mse' ,metrics=['accuracy'])
        model.fit(X, y, epochs=4000, validation_split=0.05)
        saveModel(model)
    else:
        print("Input file doesn't exists.")
else:
    print("Give the name of the input file.")
    sys.exit()
