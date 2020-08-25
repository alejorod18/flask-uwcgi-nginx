from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'hello': 'world'})


@app.route('/<name>')
def hello_name(name):
    if name == 'version':
        return jsonify({'version': '1.0'})
    else:
        return jsonify({'hello': '{}'.format(name)})



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 443))
    app.run(host='0.0.0.0', port=port, ssl_context= "adhoc")