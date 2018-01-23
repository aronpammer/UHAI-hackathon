import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from web3.contract import ConciseContract

abi = json.loads("""
[
	{
		"constant": true,
		"inputs": [
			{
				"name": "id",
				"type": "uint256"
			}
		],
		"name": "getDiagnosis",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "fileHash",
				"type": "string"
			},
			{
				"name": "diagnosis",
				"type": "string"
			}
		],
		"name": "addDiagnosis",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "patientId",
				"type": "string"
			}
		],
		"name": "setPatientInfo",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
""")


web3prov = Web3(HTTPProvider('https://ropsten.infura.io'))
my_account = "0x0fC1A83F77FA3C9f53dbA8B439D861faA35fE315"
my_password = "titok123"
my_private_key = "1e10130053d9528dd059706a8e8ff7cdea373c4b3437f9b0e66d8d68bcf6b528"
contractAddress = '0xf3ecfa7a51f4aafb0ba59ae998bf4ac5d4fbbd27'
contract = web3prov.eth.contract(abi, contractAddress)
print(contract)
transaction = contract.functions.addDiagnosis('filehash1', 'Diag1').buildTransaction({'gasPrice': 21000000000})
signed = web3prov.eth.account.signTransaction(transaction, my_private_key)
web3prov.eth.sendRawTransaction(signed.rawTransaction)
# add new string here
#print(contract.addDiagnosis('filehash1', 'Diag1', transact={'from': web3prov.eth.accounts[0]}))
print('result string', contract.getDiagnosis(1))

