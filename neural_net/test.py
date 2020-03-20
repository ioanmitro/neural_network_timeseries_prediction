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

# Split a univariate sequence into samples
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
        X.append(seq_x/10.0) ## diairw dia 10 gt oso pio mikra noumera exeis toso pio eukola
        y.append(seq_y/10.0) ## sugklinei
    return np.array(X), np.array(y)

# Saves the model after training
def saveModel(model):
    file_name = 'theModel.h5'
    model.save(file_name)
# Load an existing model
def loadModel():
    file_name = 'theModel.h5'
    model = load_model(file_name)
    return model

if len(sys.argv)!=1:
    filename=sys.argv[1]
    if( os.path.exists('./'+filename)):

        ##Read for the parsed file to train the model
        data = pd.read_csv(filename, sep=",", header=None)

        #Turn to array
        data=np.array(data)

        #Number of steps
        n_steps = 1 #10

        #Split the parsed data into sequence
        X, y = split_sequence(data, n_steps)

        n_features = 11#20

        #Reshape the array in order to use it with LSTM
        X = X.reshape((X.shape[0], X.shape[0], n_features))

        #Load model
        model =loadModel()

        #Get the loss and the accuracy
        scores=model.evaluate(X, y)
        print("Loss: %lf Accuracy:%lf "%(scores[0],scores[1]))
        
    else:
        print("Input file doesn't exists.")
else:
    print("Give the name of the input file.")
    sys.exit()
