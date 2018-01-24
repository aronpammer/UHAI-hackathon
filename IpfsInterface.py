'''
Code borrowed from IPFS test.py in functionality test
folder
This code is shareable using the MIT license

TODO: Add the license text here
'''

import hashlib
import json
from time import time
from urlparse import urlparse
from uuid import uuid4
import sys
import os

import ipfsapi

__is_available = None
api = ipfsapi.Client()

def is_available():
    """
    Return whether the IPFS daemon is reachable or not
    """
    global __is_available

    if not isinstance(__is_available, bool):
        try:
            ipfsapi.connect()
        except ipfsapi.exceptions.Error as error:
            __is_available = False

            # Make sure version incompatiblity is displayed to the user
            if isinstance(error, ipfsapi.exceptions.VersionMismatch):
                raise
        else:
            __is_available = True

    return __is_available

def isOnline():
    if is_available():
        return True
    else:
        return False

def addFileObj(fp):
    if file is None:
        return -1
    if (isOnline() is False):
        print ("no service")

    retHash = api.add(fp, pin=False)
    print ("file hash returned {something}".format(something=retHash["Hash"]))
    return retHash["Hash"]

def retriveFile(fileHash):
    if (isOnline() is False):
        print ("no service")
    if hash is None:
        print("invalid hash")
        return

    print("Hash to retrieve {something}".format(something=fileHash))
    return api.get(fileHash, filepath="ipfs_downloads/")

'''
def main():
    if (len(sys.argv) <= 1):
        print ("give me file args:")
        return
    retHash = None

    with open(sys.argv[1], 'rb') as fp:
        retHash = addFileObj(fp)

    retriveFile(retHash)
    assert retHash in os.listdir(os.getcwd())

if __name__ == "__main__":
    main()
'''
