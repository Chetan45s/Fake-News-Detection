import nltk
import os
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import tensorflow
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
from nltk.stem.porter import PorterStemmer
from tensorflow import keras
from django.conf import settings

def fnm(inputnewstext):
    stemnews=re.sub('[^a-zA-Z]',' ',inputnewstext)
    stemnews=stemnews.lower()
    stemnews=stemnews.split()
    ps=PorterStemmer()
    stemnews= [ps.stem(word) for word in stemnews if not word in stopwords.words('english')]
    stemnews = ' '.join(stemnews)

    vocabulary_size=10000

    onehot_repr=[one_hot(stemnews,vocabulary_size)] 
    embedded_text=pad_sequences(onehot_repr,padding='pre',maxlen=50)
    x=embedded_text.reshape(1,50)
    fnm_model=keras.models.load_model('my_model.h5',compile=False)
    result=fnm_model.predict_classes(x)
    print(result[0][0])

m = "chetan is fail"
fnm(m)