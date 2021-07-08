from flask import render_template
import connexion

from flask import Flask, request
from flask_restx import Resource, Api
from flask_cors import CORS, cross_origin
from Runner import Runner;

app = Flask(__name__)
api = Api(app)  

runner = Runner()

CORS(app, support_credentials=True)
@cross_origin(supports_credentials=True)

@app.route('/search', methods=['GET'])
def search():
    term = request.args.get('term')
    return runner.search(term)

@app.route('/results', methods=['GET'])
def results():
    searchId = request.args.get('searchId')
    return runner.getResults(searchId)

@app.route('/mostSearched', methods=['GET'])
def mostSearched():
    return runner.getMostSearched()

@app.route('/latestSearchs', methods=['GET'])
def latestSearchs():
    return runner.getLatestSearchs()

@app.route('/getLog', methods=['GET'])
def Log():
    term = request.args.get('term')
    return runner.getLog(term)

@app.route('/saveFile', methods=['POST'])
def post():
    file = request.form['name']
    runner.saveFile(file)
    return {'sucesso': True}

@app.route('/restoreFile', methods=['GET'])
def get():
    file = request.args.get('name')
    runner.restoreFile(file)
    return {'sucesso': True}

        
if __name__ == "__main__":
  app.run(debug=True)