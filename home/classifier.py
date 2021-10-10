from tensorflow import keras
import numpy as np

def nn_predictions(path,modal) :
    
    df = np.loadtxt(path)
    
    stop = df.shape[0]
    index = 1
    start = 0
    end = 1024

    sequences = []


    while end < stop :
      sequences.append(df[start:end])
      start = end
      end += 1024

    sequences = np.array(sequences)
    ln = sequences.shape[0]
    
    sequences = sequences.reshape((sequences.shape[0], sequences.shape[1], 1))
    
    try :
        model = keras.models.load_model("Models/{}_model.h5".format(modal))
    except OSError :
        return "please provide right modality"
    
    
    a = np.argmax(model.predict(sequences), axis=1)
    t = np.bincount(a).argmax()
    f = np.bincount(a)[t]


    cont = ['neutral', 'stress', 'amusement']
    
    
    return cont[t],f*(1024/700), ln*(1024/700)