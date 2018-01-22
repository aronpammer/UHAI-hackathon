from flask import Flask, jsonify, request, render_template

# Instantiate the Node
app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template("main.html",
                           name="John")

@app.route('/', methods=['POST'])
def login_post():
    return render_template("index.html")


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8888, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port, debug=True)