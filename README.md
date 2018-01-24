UHAI
Predictive AI engine for cancer diagnosis

Introduction

This document gives a high level overview of the
development, hacks, shortcomings and their solutions
that was done and faced during the FutureHack

Major modules

- UHAI analytical engine
- Ethereum interfacing module
- Pythom Web service engine for end user
- IPFS client interface

Design decisions and pattern

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

Dependencies

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

Scalability
UHAI can handle a few hundred requests per second

UHAI is dependent on IPFS which has an evaluated
IO bandwidth of 2MBps in the current network that we have here.
The current infrastructure of a 5Ghz wifi network will gate how much
data can be sent on the wire.

On a faster network infrastructure, UHAI can scale to much more
than what we observe here.
The UHAI can run on multiple nodes, each node running
the same UHAI code.

Ethereum and IPFS are symmetric, as a result the same user can upload
the same set of data on multiple nodes *without* duplication or loss
in performance
