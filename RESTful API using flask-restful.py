# By: Tim Tarver also known as CryptoKeyPlayer
# RESTful API using flask-restful

# These modules are needed for this API

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# This creates the Flask app

app = Flask(__name__)

# This creates an API object

api = Api(app)

# Now we create a class for a particular resource
# using the get and post methods to correspond to
# get and post requests.
# They are automatically mapped by flask_restful.
# Other methods include put, delete, etc.

class Hello(Resource):

    # This class corresponds to the GET request
    # The functions below is called whenever there
    # is a GET request for this resource
    
    def get(self):
        return jsonify({'message' : 'hello world'})

    # This methods corresponds to the POST request
    
    def post(self):

        data = request.get_json()  # to retrieve status codes
        return jsonify({'data' : data}), 201

# This class is another resource to calculate the square of a number

class Square(Resource):

    def get(self, num):

        return jsonify({'square' : num**2})

# The next lines adds the defined resources along with their corresponding url's

api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')

# This is the driver function
if __name__ == '__main__':

    app.run(debug = True)
