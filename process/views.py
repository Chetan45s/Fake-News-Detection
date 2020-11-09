import os
import re
import nltk
import tensorflow
from tensorflow import keras
from nltk.corpus import stopwords
from django.conf import settings
from django.shortcuts import render
from process.forms import InputForm
from django.shortcuts import redirect
from tensorflow.keras.layers import LSTM
from nltk.stem.porter import PorterStemmer
from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import Sequential
from process.models import InputData,Contribution
from django.core.exceptions import ObjectDoesNotExist
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.backend import manual_variable_initialization 
from tensorflow.keras.layers import Dense,Bidirectional,Dropout
from tensorflow.keras.preprocessing.sequence import pad_sequences


def fnm_title(inputnewstext):
    manual_variable_initialization(True)

    stemnews=re.sub('[^a-zA-Z]',' ',inputnewstext)
    stemnews=stemnews.lower()
    stemnews=stemnews.split()
    ps=PorterStemmer()
    stemnews= [ps.stem(word) for word in stemnews if not word in stopwords.words('english')]
    stemnews = ' '.join(stemnews)

    vocabulary_size=10000
    onehot_repr=[one_hot(stemnews,vocabulary_size)] 
    embedded_text=pad_sequences(onehot_repr,padding='pre',maxlen=50)

    embedding_vector_features=40
    bestmodel=Sequential()
    bestmodel.add(Embedding(vocabulary_size,embedding_vector_features,input_length=50))
    bestmodel.add(LSTM(150))
    bestmodel.add(Dense(1,activation='sigmoid'))
    bestmodel.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    bestmodel.load_weights(os.path.join(settings.MODEL_ROOT, 'titleweights.h5'))
    x=embedded_text.reshape(1,50)
    result=bestmodel.predict_classes(x)
    return result[0][0]

def fnm_text(inputnewstext):
    manual_variable_initialization(True)

    stemnews=re.sub('[^a-zA-Z]',' ',inputnewstext)
    stemnews=stemnews.lower()
    stemnews=stemnews.split()
    ps=PorterStemmer()
    stemnews= [ps.stem(word) for word in stemnews if not word in stopwords.words('english')]
    stemnews = ' '.join(stemnews)[0:1000]
    vocabulary_size=10000 
    onehot_repr=[one_hot(stemnews,vocabulary_size)] 
    embedded_text=pad_sequences(onehot_repr,padding='pre',maxlen=1000)
    embedding_vector_features=50
    tmodel=Sequential()
    tmodel.add(Embedding(vocabulary_size,embedding_vector_features,input_length=1000))
    tmodel.add(Bidirectional(LSTM(100)))
    tmodel.add(Dense(1,activation='sigmoid'))
    tmodel.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    tmodel.load_weights(os.path.join(settings.MODEL_ROOT, 'textweights.h5'))

    x=embedded_text.reshape(1,1000)
    result=tmodel.predict_classes(x)
    return result[0][0]

def fnm(title,text):
    stemnews1=re.sub('[^a-zA-Z]',' ',title)
    stemnews1=stemnews1.lower()
    stemnews1=stemnews1.split()
    ps=PorterStemmer()

    stemnews1= [ps.stem(word) for word in stemnews1 if not word in stopwords.words('english')]
    stemnews1= ' '.join(stemnews1)[0:50]
    stemnews2=re.sub('[^a-zA-Z]',' ',text)
    stemnews2=stemnews2.lower()
    stemnews2=stemnews2.split()
    stemnews2= [ps.stem(word) for word in stemnews2 if not word in stopwords.words('english')]
    stemnews2= ' '.join(stemnews2)[0:450]
    stemnews=stemnews1+" text: "+stemnews2

    vocabulary_size=10000 
    onehot_repr=[one_hot(stemnews,vocabulary_size)] 
    embedded_text=pad_sequences(onehot_repr,padding='pre',maxlen=500)

    embedding_vector_features=50
    model=Sequential()
    model.add(Embedding(vocabulary_size,embedding_vector_features,input_length=500))
    model.add(LSTM(100))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    model.load_weights(os.path.join(settings.MODEL_ROOT, 'titletextweights.h5'))

    x=embedded_text.reshape(1,500)
    result=model.predict_classes(x)

    return result[0][0]

def home(request):
    form = InputForm()
    input = InputData.objects.all()
    cont = Contribution.objects.all()
    res = InputData.objects.filter(result=1)
    context = {
        'form':form,
        'input':input,
        'cont':cont,
        'res':res,
    }
    return render(request, 'process/index.html',context)

def InputView(request):
    text = request.GET.get('text')
    title = request.GET.get('title')
    text_cont = request.GET.get('text_cont')
    title_cont = request.GET.get('title_cont')
    label = request.GET.get('label')
    if text_cont is None:
        if request.GET.get('title') and request.GET.get('text'):
            result = fnm(title,text)
            accuracy = 91.21
            InputData.objects.create(text=text,title=title,result=result)
            print("1----------",result)
        elif request.GET.get('text'):
            result = fnm_text(text)
            accuracy = 91.30
            InputData.objects.create(text=text,result=result)
            print("2--------",result)
        elif request.GET.get('title'):
            result = fnm_title(title)
            accuracy = 91.77
            InputData.objects.create(title=title,result=result)
            print("3-----------",result)
        context = {
            'result' :result,
            'accuracy':accuracy,
        }
        return render(request, 'process/result.html',context)    
    if title is None:
        Contribution.objects.create(text=text_cont,title=title_cont,label=label)
        return render(request,"process/index.html")
    