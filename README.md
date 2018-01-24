# ABOUT UHAI

Universal Health Artificial Intelligence (UHAI) is a decentralized platform that processes, stores and unifies electronic medical information on the blockchain where AI is used to detect anomalies and predict health outcomes.  UHAI is powered by UHAI cryptographic utility tokens that enable participants to earn tokens in exchange for participation.  Security and privacy are first priorities.

Please visit us at www.uhai.io <br />
Executive Summary: https://uhai.io/publications/UHAI_Summary_English.pdf <br />
White Paper: https://uhai.io/publications/UHAI_white_paper_longform_english.pdf <br />


# FutureHack Hackathon

The UHAI Breast Cancer Detection Project is an end-to-end offering that can determine if a mass lesion on an x-ray image is benign or cancerous.  To achieve this analysis, we leveraged IPFS (a decentralized file storage) and Ethereum blockchains in combination with our internally tuned machine learning algorithms. Currently users can receive almost as good as a radiologist diagnosis by simply uploading an mammography (68% accuracy algorithm developed during the Hackathon) which can be later improved above 90% based on recent studies [3] . The results are returned within seconds.

**IMPACT:** We are providing solutions under SDG 3, Health and Wellbeing.  We have chosen breast cancer because it is the number one killer of women globally at 800k deaths annual.  As well, it’s the number one new cancer case in the world, at 30%.  Breast cancer affects every mother, daughter, aunt—- every woman on the planet.  For the very first time, patients can upload her medical information to a platform that will give instant diagnosis. The average error rate among radiologists is around 30% [3] . With the help of large datasets and deep learning algorithms our system can help doctors and radiologists to detect malignant breast lesions and decrease this error ratio.

**BLOCKCHAIN:**  We use the IPFS (decentralized file storage) to store image files and the Ethereum blockchains to store transactional information and metadata.

**SCALE:**  The system will scale as fast as the blockchain network.   Plus, the front-end is a webservice and can be powered up by renting computation from provider.   The platform can be globally scaled instantly.

**DESIGN:**  The system has many components, designed to work separately or collaboratively.  We design the system to blockchain agnostic, which effectively shields us from performance issues of certain blockchains.  If a blockchain cannot scale as fast as we need, we can move to a better one.

**WALKTHROUGH:**
User user logs into web
User uploads x-ray image
Data is sent to IPS for storage.  System retrieves hash.
AI engine runs analysis on x-ray.
Results and history are sent back to the user.
Results + IPFS hash are written onto the Ethereum blockchain.

# OVERALL ARCHITECTURE DIAGRAM*
![System](https://github.com/velvetz7/UHAI-hackathon/blob/master/system.PNG)

# Major modules

- UHAI analytical engine
- Ethereum interfacing module
- Pythom Web service engine for end user
- IPFS client interface

# Design decisions and pattern

- A web browser based tool is the easiest tool that an end user can utilize.
- Our python based web service engine recieves requests from the end user
  and calls the image processing library which we have developed.
- The python web services logic interfaces with our simple javascript
  based Ethereum web service engine. 
  The javascript based web services engine was
  used, since python Ethereum interface is not very mature yet.
  The javascript based webservice communicates with the Ethereum ecosystem
  for reading and creating smart contracts.
- IPFS is used as a storage medium for our images which user uploads for
  diagnosis. We use IPFS to also retrieve these images when a user wants to
  review his diagnosis history
- The AI engine which we developed as part of this hackathon is used
  as a library inside the python web services logic

# Module interactions

![Receiving Data](https://github.com/velvetz7/UHAI-hackathon/blob/master/receiving_data.PNG)
![Sending Data](https://github.com/velvetz7/UHAI-hackathon/blob/master/sending.PNG)

# Dependencies

- IPFS (and its dependencies)
- node.js
- keras
- pydicom
- numpy
- skimage
- boto
- flask
- scipy
- pil

# Scalability

UHAI can handle a few hundred requests per second currently on a consumer laptop,  but it can be easily scaled to higher level by deployin on e.g Amazon AWS

UHAI is dependent on IPFS.

On a faster network infrastructure, UHAI can scale to much more
than what we observe here.
The UHAI can run on multiple nodes, each node running
the same UHAI code.

Ethereum and IPFS are symmetric, as a result the same user can upload
the same set of data on multiple nodes *without* duplication or loss
in performance

# AI Engine Logic Description

## Deep Learning - Convolutional Neural Network_7_final.ipynb
 
### Inception V3 Deep Neural Network Used to Predict Breast Lesion Diagnosis
 
Our model uses the Inception V3 Convolutional Neural Network pretrained on Imagenet, retraining the top 3 Inception layers to fit the Digital Database of Screening Mammography[1] (DDSM) images segmented via radiologist notation and cropped into a Region of Interest (ROI) by the Cancer Imaging Archive (TCIA) Public Access[2].
 
The Inception V3 Neural Network was designed by Google and initially trained on the ImageNet Large Visual Recognition Challenge.  It consists of multiple convolutional, pooling, and concatenation batch normalization nodes, in addition to 11 inception models that contain parallel pathways of convolution and pooling nodes.3
 
### Training and model evaluation steps:
 
Loaded data and kernel on AWS Ubuntu GPU Instance in order to reduce large training times.
 
As detailed in the jupyter notebook, we first converted the images into numpy array format, converted grayscale to RGB format, resized images to 299x299, and normalized values to 0-1, and coded response binary data (“BENIGN” or “MALIGNANT”). These transformations are necessary to input into the pretrained Inception V3 model.
 
We split the 1317 images into training, validation, and test sets at 70%, 15%, and 15% of the data, respectively.
 
In building the training model, we loaded the Inception V3 CNN trained on ImageNet, removing the top layer that outputs response data to the previous image categories in order to add our own layers that pool the previous layers, add a dense layer (which makes all the weighted connections), and then creates a softmax that creates a probabilistic response function between our binary responses.
 
We then froze all other layers, and trained just the new layers to get a baseline of accurate weights.  We then unfroze the main top 3 layers of inception modules and trained them on our dataset for 80 epochs, with a patience factor of 30 (meaning if the validation error didn’t improve in 30 epochs, the model would stop training).
 
Through our model iterations we added additional features, including a dropout layer to reduce overtraining, tested different frozen and nonfrozen modules, and augmented our data, in addition to many other features. A large majority and planned features of our model was based on the keras.io repository, and recent research papers3-9.
 
For all these models built and trained in the last 48 hours, we compared accuracy on the validation dataset to choose our final prediction model, reaching an 68% diagnostic accuracy rate on the test data.
 
The final output of the script is the trained inceptionv3_model.h5py deep learning model (around 150 MB, so it could not be uploaded to github, but can be reproduced by running the file)
 
## Convolutional_neural_network_predict.py

The previously mentioned inceptionv3_model.h5py deep learning model file is used by the convolutional_neural_network_predict.py function for predicting all the newly uploaded mammogram images whether the mass lesion is malignant or benign.  The prediction function creates a vector consisting of probability scores for the lesion being malignant or benign. If the softmax classifier for being malignant is higher than 0.5 we classify it as cancerous lesion.

The function is also converting the uploaded DICOM image to PNG format so it can be plotted on the UI.
 
 



1. p://marathon.csee.usf.edu/Mammography/Database.html
2. https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM
3. Chougrad, et al. Deep Convolutional Neural Networks for Breast Cancer Screening.  https://www.sciencedirect.com/science/article/pii/S0169260717301451
4. Qiu Y, Yan S, Tan M, Cheng S, Liu H, Zheng B (2016) Computer-aided classification of mammographic masses using the deep learning technology: a preliminary study:
5. Jiao Z, Gao X, Wang Y, Li J (2016) A deep feature based framework for breast masses classification. Neurocomputing 197:221–231
6. Computational mammography using deep neural networks
7. Probabilistic visual search for masses within mammography images using deep learning
8. https://www.researchgate.net/publication/320321443_Mammogram_Classification_using_Deep_Learning_Features
9. https://keras.io/applications/
