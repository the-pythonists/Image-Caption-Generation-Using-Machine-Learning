from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from HomeApp.CaptionAssets.objects import object_Detector
import dill as pickle 
import cv2
import numpy as np
from nltk.tokenize.treebank import TreebankWordDetokenizer

with open('HomeApp/caption.pkl', 'rb') as fin:
    model_loaded = pickle.load(fin)

def home(request):
    user = request.session['user']
    if user:
        return render(request,'album.html',{'user':user})
    else:
        return render(request,'album.html')

def caption(request):
    # reading image
    img = cv2.imdecode(np.fromstring(request.FILES['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    print(type(img))
    # detecting objects
    objects = object_Detector(img)

    # generating caption
    cap = model_loaded.generate(text_seed=objects,num_words=7, random_seed=7)

    detokenize = TreebankWordDetokenizer().detokenize
    temp = []
    for token in cap:
        if token == '<s>':
            continue
        if token == '</s>':
            break
        temp.append(token)
        finalCap = detokenize(temp)
    print(finalCap)
    return render(request, 'album.html',{'cap':finalCap,'img':img,'user':request.session['user']})