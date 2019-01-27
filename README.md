# Files:

1.train.py --> Gia na ekpaideusoume to montelo mas

2.parse.py --> Gia na parsaroume to outputacm.txt

3.gpu_run.py --> Idia logikh me to train.py alla xrisimopoiei CuDNNLSTM gia GPU support

4.outputacm.txt --> arxeio pou pernoume dedomena

## Steps for parsing and train:

1.python parse.py outputacm.txt

2.python train.py finalParsing.txt

3.python gpu_run.py finalParsing.txt (Einai idio me to (2) alla xrhsimopoiei GPU)

## Libraries:
1.NumPy --> gia diaxeirish pinakwn

2.Keras API --> gia to montelo kai genikotera gia to training

3.pandas --> gia diavasma twn arxeiwn

4.tensorflow --> basizetai to keras sto tensorflow

5.matplotlib --> gia na kanoume ta plots
