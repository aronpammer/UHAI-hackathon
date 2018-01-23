from flask import Flask, jsonify, request, render_template
import blockchain
# Instantiate the Node
app = Flask(__name__)


@app.route('/account', methods=['GET'])
def main():
    return render_template("main_content.html")


@app.route('/upload', methods=['GET'])
def upload():
    return render_template("upload.html")


@app.route('/history', methods=['GET'])
def history():
    diagnosises = []
    for response in get_diagnosis_from_blockchain():
        print(response)
        # get file_url from ipfs
        file_url = response["fileHash"]
        result = response["diagnosis"]
        diagnosises.append({
            "file_url": file_url,
            "result": result
        })
    return render_template("history.html", diagnosises=diagnosises)


@app.route('/upload_image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image-file' not in request.files:
            return 'No file part'
        file = request.files['image-file']
        upload_file_to_ipfs_blockchain(file)
    return "file uploaded"

# there can be any number of contract addresses, ideally one per patient, for the demo we are only using one
STATIC_CONTRACT_ADDRESS = "0x6477e21f70ee303bb0a47b96a737cbf64eb99852"
# the from address would be ideally the service's address that uploads the data to the blockchain, in this case UHAI
STATIC_FROM_ADDRESS = "0x0fC1A83F77FA3C9f53dbA8B439D861faA35fE315"

def upload_file_to_ipfs_blockchain(file):
    file_hash = "FILEHASH"  #IpfsInterface.addFileObj(file)
    print("file hash {file}".format(file=file_hash))
    # here we are going to analyze the data
    # ...
    result = "0.9"

    # here we are going to upload the data to eth

    import requests
    response = requests.get("http://localhost:1337/add_diagnosis/{contract_address}?filehash={file_hash}&result={result}&from={from_address}&gas={gas}".format(
        contract_address=STATIC_CONTRACT_ADDRESS,
        file_hash=file_hash,
        result=result,
        from_address=STATIC_FROM_ADDRESS,
        gas=3000000
    )).text
    print(response)

def get_diagnosis_from_blockchain():
    import requests
    id = 0
    while True:
        response = requests.get("http://localhost:1337/diagnosis/{contract_address}/{id}".format(
            contract_address=STATIC_CONTRACT_ADDRESS,
            id=id
        )).text
        print(response)
        if "ERROR" in response:
            break
        import json
        yield json.loads(response)
        id += 1



@app.route('/', methods=['GET'])
def login():
    return render_template("index.html")


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8888, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port, debug=True)