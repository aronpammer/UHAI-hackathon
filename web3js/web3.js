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
		"inputs": [],
		"name": "getDiagnosesCount",
		"outputs": [
			{
				"name": "count",
				"type": "uint256"
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

var my_private_key = "0x1e10130053d9528dd059706a8e8ff7cdea373c4b3437f9b0e66d8d68bcf6b528"
web3.eth.accounts.wallet.add(my_private_key);


const express = require('express');
const app = express();
const port = 1337;

app.get('/', (request, response) => {
  response.send('Hello from Express!')
});

app.get('/diagnosis/:contractaddress/:id', (request, response) => {
  let id = request.params.id;
  //0x6477e21f70ee303bb0a47b96a737cbf64eb99852
  var contractAddress = request.params.contractaddress;
  var contract = new web3.eth.Contract(contractJson, contractAddress);
  contract.methods.diagnosises(id).call(function(error, result) {
        console.log(result);
        console.log(error);

        if(result != null) {
            response.send(result);
        } else {
            response.send(error);
        }
    });
});


//http://localhost:1337/add_diagnosis/0xccf510c7e770bce34345fc519795be9b6eee41cb?filehash=text1&result=test2&from=0x0fC1A83F77FA3C9f53dbA8B439D861faA35fE315&gas=3000000
app.get('/add_diagnosis/:contractaddress', (request, response) => {
  let contractAddress = request.params.contractaddress;
  let fileHash = request.query.filehash;
  let result = request.query.result;
  //0x0fC1A83F77FA3C9f53dbA8B439D861faA35fE315
  let fromAddress = request.query.from;
  //3000000
  let gas = request.query.gas;

  var contract = new web3.eth.Contract(contractJson, contractAddress);
  var result2 = contract.methods.addDiagnosis(fileHash, result).send({from: fromAddress, gas: gas}, function(error, result) {
        console.log(result);
        console.log(error);

        if(result != null) {
            response.send("transaction queued: " + result);
        } else {
            response.send(error);
        }
  });
});

app.listen(port, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }
  console.log(`server is listening on ${port}`)
});


/*
var result = contract.methods.diagnosises(1).call(function(error, result) {
    console.log(result);
    console.log(error);
});

var result2 = contract.methods.addDiagnosis("aaa2", "bbb2").send({from: "0x0fC1A83F77FA3C9f53dbA8B439D861faA35fE315", gas: "3000000"}, function(error, result) {
    console.log(result);
    console.log(error);
});*/