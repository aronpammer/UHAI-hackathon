import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from web3.contract import ConciseContract


web3prov = Web3(HTTPProvider('https://ropsten.infura.io'))
contractAddress = '0x3c7bec02bd4fa73dce24413d2a13c02e1a91e858'
#contract =