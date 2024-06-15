import pickle
from flask import Flask, request, jsonify
import numpy as np

from flask_cors import CORS  # Import CORS from flask_cors module

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)





app = Flask(__name__)




CORS(app)



@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  
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


    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)  