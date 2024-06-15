import pickle
from flask import Flask, request, jsonify
import numpy as np

from flask_cors import CORS  # Import CORS from flask_cors module

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)





app = Flask(__name__)




CORS(app)

# Dummy function to process data using a model (replace with your actual model logic)
def process_data(data):
    # Example: Simply return a dictionary with processed data
    return {"result": data["input"] * 2}  # Example processing: doubling the input

# Route to receive data from Vue.js frontend
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # Assuming data is sent as JSON

    # Process data using your model
    result = data
    print(data["key"])
    
    data2d = []
    data2d.append(data["key"])
    data2d =np.array(data2d)
    predicted = model.predict(data2d)
    print(predicted)
    
    respose = predicted.tolist()

    data["key"] = respose

    result  = data
    print(result)

    #Return result as JSON response
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)  # Run Flask app in debug mode for development
