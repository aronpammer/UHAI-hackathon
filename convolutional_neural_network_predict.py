# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:32:42 2018

@author: Dániel
"""

import dicom 
import numpy as np
np.random.seed(123)  # for reproducibility
import numpy as np
from keras.models import load_model
from skimage import transform as tf



uploaded_file="C:/Users/Dániel/OneDrive/Documents/Georgia Tech/Courses/Spring 2018/DDSM_Data_Move/"
deep_learning_model="C:/Users/Dániel/OneDrive/Documents/Georgia Tech/Courses/Spring 2018/FutureHack/inceptionv3_model.h5py"

convolutional_neural_network=load_model(deep_learning_model)


#mylist=[key for key, value in mydict.items() if mydict[key][0]!='MALIGNANT']


def predict_breast_cancer(uploaded_file, convolutional_neural_network):

    #Loading the model
    
    
    # Data Import and Transformation - import dicom convert it to numpy grayscale image
#for i in mylist:
    #ds=dicom.read_file(uploaded_file+i, force=True)
    ds=dicom.read_file(uploaded_file, force=True)
    ConstPixelDims = (int(ds.Rows), int(ds.Columns))
    ArrayDicom = np.zeros(ConstPixelDims, dtype=ds.pixel_array.dtype)
    #converting scales
    ArrayDicom = (ds.pixel_array/65535)*256
    
    #Neccessary additional transformations - resizing and normalizing 
    example=np.array(tf.resize(ArrayDicom, (139,139)))
    example=example-np.mean(example)
    example = example.reshape(-1, 139,139, 1)
    example = np.tile(example, (1, 1, 3))
    
    
    
    deep_learning_prediction=convolutional_neural_network.predict(example)
    
    #Prediction 
    deep_learning_prediction_classes= np.argmax(np.round(deep_learning_prediction),axis=1)
    final_prediction=deep_learning_prediction_classes[0]
    #print(i)
    #print(final_prediction)
    #returns 0 if benign (not cancer) and 1 if malignant
    return final_prediction

predict_breast_cancer(uploaded_file,deep_learning_model)


