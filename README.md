
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

4.tensorflow --> Based on the keras of tensorflow

5.matplotlib --> Used for the plots
