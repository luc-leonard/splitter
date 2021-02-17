from flask import Flask, request

from splitter.splitter.splitter import Splitter
from flask_cors import CORS
app = Flask(__name__)
splitter = Splitter('spleeter:5stems')
CORS(app, resources={r"/*": {"origins": ['http://localhost:8080']}})

@app.route('/split', methods=['POST', 'GET'])
def split():
    print('new query !')
    uploaded_file = request.files['file']
    print(uploaded_file)

@app.after_request
def add_headers(response):
    for hdr_name in list(response.headers.keys()):
        if hdr_name.startswith('Access-Control-'):
            response.headers.remove(hdr_name)
    return response

if __name__ == '__main__':
    app.run(port=6001)