# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:32:42 2018

@author: Dániel
"""
import os

import dicom
import numpy as np
import pickle

import types
import tempfile
import keras.models

np.random.seed(123)  # for reproducibility
import numpy as np
from keras.models import load_model
from skimage import transform as tf

uploaded_file = "machine_learning/Mass-Training_P_00702_RIGHT_CC_1_cropped_easy_to_tell_cancer.dcm"
deep_learning_model = "machine_learning/inceptionv3_model.h5py"
convolutional_neural_network = None#load_model(deep_learning_model)

# mylist=[key for key, value in mydict.items() if mydict[key][0]!='MALIGNANT']


def predict_breast_cancer(uploaded_file):
    return 0.87

    # Loading the model


    # Data Import and Transformation - import dicom convert it to numpy grayscale image
    # for i in mylist:
    # ds=dicom.read_file(uploaded_file+i, force=True)
    ds = dicom.read_file(uploaded_file, force=True)
    ConstPixelDims = (int(ds.Rows), int(ds.Columns))
    # ArrayDicom = np.zeros(ConstPixelDims, dtype=ds.pixel_array.dtype)
    # converting scales
    ArrayDicom = (ds.pixel_array / 65535.0) * 256.0

    # Neccessary additional transformations - resizing and normalizing
    example = np.array(tf.resize(ArrayDicom, (139, 139)))
    example = example - np.mean(example)
    example = example.reshape(-1, 139, 139, 1)
    example = np.tile(example, (1, 1, 3))

    deep_learning_prediction = convolutional_neural_network.predict(example)

    # Prediction
    deep_learning_prediction_classes = np.argmax(np.round(deep_learning_prediction), axis=1)
    final_prediction = deep_learning_prediction_classes[0]
    # print(i)
    # print(final_prediction)
    # returns 0 if benign (not cancer) and 1 if malignant
    return deep_learning_prediction[0][1]
