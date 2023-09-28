
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS


from dotenv import load_dotenv
import os

app=Flask(__name__)
CORS(app)
# CORS(app, resources={r"/": {"origins": "https://main--tasks-manager-site.netlify.app"}})





app = Flask(__name__)



client = MongoClient(os.environ.get('MONGO_URI'))

# mongodb+srv://PradeeP1G:Pradeep%402003@cluster0.50omidk.mongodb.net

db = client.awslambda

CORS(app)


@app.route('/addUser', methods=['PUT'])
def addUser():
    data = request.json

    
    collection = db.weatherusers
    result = collection.insert_one(data)
    




    if result:
        print("Success")
        return jsonify({"is_success":True})
    else:
        return jsonify({"is_success":False})
    







if __name__ == '__main__':
    app.debug = True
    app.run()
