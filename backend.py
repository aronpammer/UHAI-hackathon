import sys
from flask import Flask, jsonify, request, render_template, redirect
import blockchain
# Instantiate the Node
import convolutional_neural_network_predict

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return redirect("/account", code=302)


@app.route('/uploading', methods=['GET'])
def uploading():
    return render_template("uploading.html")


@app.route('/account', methods=['GET'])
def main():
    return render_template("main_content.html")


@app.route('/upload', methods=['GET'])
def upload():
    return render_template("upload.html")


@app.route('/download/<ipfs_id>')
def download_ipfs(ipfs_id):
    import IpfsInterface
    from flask import send_file
    file = IpfsInterface.retriveFile(ipfs_id)
    return send_file("ipfs_downloads/{}".format(ipfs_id))

@app.route('/history', methods=['GET'])
def history():
    diagnosises = []
    for response in get_diagnosis_from_blockchain():
        print(response)
        # get file_url from ipfs
        file_hash = response["fileHash"]
        result = response["diagnosis"]
        date_time = response["date"]
        description = response["description"]
        is_cancerous = "cancerous" if float(response["diagnosis"]) > 0.5 else "not cancerous"
        diagnosises.append({
            "file_hash": file_hash,
            "description": description,
            "result": round(float(result) * 100, 2),
            "date": date_time,
            "is_cancerous": is_cancerous
        })
    return render_template("history.html", diagnosises=list(reversed(diagnosises)))


@app.route('/upload_image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image-file' not in request.files:
            return 'No file part'
        file = request.files['image-file']
        tmp_file_path = "/tmp/{}".format(file.filename)
        file.save(tmp_file_path)
        description = request.form['description']
        description = " " + description
        import IpfsInterface
        file_hash = IpfsInterface.addFileObj(tmp_file_path)
        print("file hash {file}".format(file=file_hash))
        path = "static/image/dicom/{}.png".format(file_hash)
        result = convolutional_neural_network_predict.predict_breast_cancer(tmp_file_path, path)

        upload_file_to_blockchain(file_hash, description, result)
    return redirect("/uploading", code=302)

# there can be any number of contract addresses, ideally one per patient, for the demo we are only using one
STATIC_CONTRACT_ADDRESS = "0x96d1b1cf4dd8d1cc6d61455ae88e213800877700"
# the from address would be ideally the service's address that uploads the data to the blockchain, in this case UHAI
STATIC_FROM_ADDRESS = "0x0fC1A83F77FA3C9f53dbA8B439D861faA35fE315"

def upload_file_to_blockchain(file_hash, description, result):
    import requests
    import datetime
    date_time = datetime.datetime.today().strftime("%b %d %Y at %I:%M %p").upper()
    response = requests.get("http://localhost:1337/add_diagnosis/{contract_address}?filehash={file_hash}&result={result}&from={from_address}&gas={gas}&description={description}&datetime={datetime}".format(
        contract_address=STATIC_CONTRACT_ADDRESS,
        file_hash=file_hash,
        result=result,
        description=description,
        from_address=STATIC_FROM_ADDRESS,
        gas=3000000,
        datetime=date_time
    ), timeout=5).text
    print(response)

def get_diagnosis_from_blockchain():
    import requests
    id = 0
    while True:
        loaderror = False
        for i in range(5):
            # don't look at this please, waaaay too hacky...
            try:
                response = requests.get("http://localhost:1337/diagnosis/{contract_address}/{id}".format(
                    contract_address=STATIC_CONTRACT_ADDRESS,
                    id=id
                ), timeout=2.5).text
                break
            except:
                pass
            if i == 4:
                loaderror = True
                print("------------------------------------------------")
                print("LOAD ERROR!LOAD ERROR!LOAD ERROR!LOAD ERROR! id:{}".format(id))
                print("------------------------------------------------")

        if loaderror is False:
            import json
            print(response)
            if "ERROR" in response:
                break
            try:
                obj = json.loads(response)
                yield obj
            except:
                pass

        id += 1



@app.route('/', methods=['GET'])
def login():
    return render_template("index.html")


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8000, type=int, help='port to listen on')
    parser.add_argument('-c', '--contract', default="0x96d1b1cf4dd8d1cc6d61455ae88e213800877700", type=str, help='the sample contract address')
    parser.add_argument('-a', '--account', default="0x0fC1A83F77FA3C9f53dbA8B439D861faA35fE315", type=str, help='you personal ethereum account address')
    args = parser.parse_args()
    port = args.port
    STATIC_CONTRACT_ADDRESS = args.contract
    STATIC_FROM_ADDRESS = args.account

    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)