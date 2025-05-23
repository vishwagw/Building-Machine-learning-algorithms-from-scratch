from __future__ import division, print_function
from keras_models import load_model
from keras_preprocessing.image import load_img, img_to_array
import numpy as np
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import pickle
import cv2
import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.ERROR)
from os import listdir
from keras_preprocessing import image
import matplotlib.pyplot as plt

import os, sys, glob, re

app = Flask(__name__, template_folder="templates")

model = pickle.load(open('lr_model.pkl', 'rb'))

def modelpipeline(imagepath, model, label=-1):
    img = plt.imread(imagepath)
    img = img/255.
    img.reshape([1,-1])
    flat = np.array(img)
    flat = flat.reshape(-1,224*3)
    preds = model.predict(flat)

    predict = {0:"jute",1:"maize",2:"rice",3:"sugarcane",4:"wheat"}
    if (label!=1):
        predicted=plt.title("prediction : {} \naccurate  : {}".format(predict[preds[0]],predict[label]))
        predict=str(predicted)
        predicts=predict[28:-2]
        print(predicts)
    else:
        predicted=plt.title("prediction : {}".format(predict[preds[0]]))
        predict=str(predicted)
        predicts=predict[28:-2]
        print(predicts)
    return predicts

@app.route('/',methods=['GET'])
def index():
    return render_template('index2.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        f = request.files['files']

        basepath = os.path.dirname(__file__)
        File_path = os.path.join(basepath, 'static/user uploaded', secure_filename(f.filename))
        f.save(File_path)

        #making predictions 
        preds = modelpipeline(File_path, model)
        return preds
    return None

if __name__ == '__main__':
    app.run(debug=True)

