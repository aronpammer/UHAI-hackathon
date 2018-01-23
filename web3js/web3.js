var Web3 = require('web3');

var web3 = new Web3(new Web3.providers.HttpProvider('https://ropsten.infura.io'));

var contractJson = [
	{
		"constant": true,
		"inputs": [],
		"name": "patientId",
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
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "diagnosises",
		"outputs": [
			{
				"name": "fileHash",
				"type": "string"
			},
			{
				"name": "diagnosis",
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
];



var contractAddress = "0xccf510c7e770bce34345fc519795be9b6eee41cb";
var contract = new web3.eth.Contract(contractJson, contractAddress);

var my_private_key = "0x1e10130053d9528dd059706a8e8ff7cdea373c4b3437f9b0e66d8d68bcf6b528"
web3.eth.accounts.wallet.add(my_private_key);

var result = contract.methods.diagnosises(1).call(function(error, result) {
    console.log(result);
    console.log(error);
});
var result2 = contract.methods.addDiagnosis("aaa1", "bbb1").send({from: "0x0fC1A83F77FA3C9f53dbA8B439D861faA35fE315", gas: "3000000"}, function(error, result) {
    console.log(result);
    console.log(error);
});
//console.log(result2);