from flask import Flask, request, jsonify
from flask_cors import CORS
from search import Scrapper

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resorces={r'/*': {"orgins": '*'}})


@app.route('/')
def home():
    return "hello world"


@app.route('/search', methods=['POST'])
def search_query():
    contents = request.get_json()
    print(contents)
    query = contents['query']

    response = Scrapper.query(query)
    return jsonify({'result': response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
