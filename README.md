The aim of this project was to implement a neural network for time series forecasting using Tensorflow and Keras.
# Files:

1.train.py --> To train the model

2.parse.py --> To parse outputacm.txt

3.gpu_run.py --> The same logic train.py with the use of CuDNNLSTM for GPU support

4.outputacm.txt --> Input file of data

## Steps for parsing and train:

1.python parse.py outputacm.txt

2.python train.py finalParsing.txt

3.python gpu_run.py finalParsing.txt It is the same as 2 but with the use of GPU

## Libraries:
1.NumPy --> Used for matrices management

2.Keras API --> Used for the training and for the model

3.pandas --> Used to read files

4.tensorflow --> Based on the Keras of Tensorflow

5.matplotlib --> Used for the plots


## General

For the training we can choose train.py for CPU training and gpu_train.py for GPU depending on the performance we desire. Before this procedure, we should firstly parse the input file output.acm with the execution of parse.py 
