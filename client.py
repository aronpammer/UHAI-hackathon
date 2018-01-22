import hashlib
import json
from time import time, sleep
from urlparse import urlparse
from uuid import uuid4
import sys
import IpfsInterface
import os
import json
import shutil
import socket
import sys
import time
import unittest
import logging

import ipfsapi

import requests
#from flask import Flask, jsonify, request
global __is_init = False
global g_file_dict
def init():
    if __is_init is True:
        return

    g_file_dict = {}
    __is_init = True
    return

def uploadNewFile(fileName):
    #add to IPFS here!
    if (fileName is None):
        return -1


    filehash = None
    with open(fileName, 'rb') as fp:
        filehash = IpfsInterface.addFileObj(fp)

    fileIdentifier = filehash["Hash"]
    print("file hash {file}".format(something=fileIdentifier))

    if fileIdentifier in g_file_dict:
        return g_file_dict[fileIdentifier]

    # result = call analyse(file)
    # g_file_dict [fileIdentifier] = result
    # block chain add(userid, fileid, result)
    json_data = {'patientID': 'd4ee26eee15148ee92c6cd394edd974e',
                 'fileHash': 'someone-other-address',
                 'result': '10'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = "http://0.0.0.0:5002/transactions/new"

    r = requests.post(url, data=json.dumps(json_data), headers=headers)

    print("content %s",  r.content)


def main():
    print('Starting data processing server')
    for i in range(10):
        sys.stdout.write(".")
        sys.stdout.flush()
        sleep(0.5)

    createNewBlock();

if __name__ == "__main__":
    main()

