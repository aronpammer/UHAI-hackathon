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
    return render_template("history.html")


@app.route('/upload_image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image-file' not in request.files:
            return 'No file part'
        file = request.files['image-file']
        blockchain.uploadFile(file)
    return "file uploaded"


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