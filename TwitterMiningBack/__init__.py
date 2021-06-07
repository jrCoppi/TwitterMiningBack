from flask import render_template
import connexion

from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)  
#api.add_api('swagger.yml')

CORS(app, support_credentials=True)


@app.route("/")
@cross_origin(supports_credentials=True)
def home():
  return jsonify(swagger(app))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)