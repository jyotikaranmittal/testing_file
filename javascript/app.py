from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/EVP_db")
# mongo = MongoClient("mongodb://localhost:27017/")

# db=mongo['EVP_db']
# EV = db['Electric_vehicle']
# FS=db['alt_fuel_stations']
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/EVP")
def EVP():

    print("get_data")
    # query={"Make":"TOYOTA"}
    # results =EV.find(query)
    # return jsonify(list(results))
    query={"Make":"BMW"}
    results= mongo.db.Electric_vehicle.find(query)
    data=list(results)
    return jsonify(data)
    # return jsonify(list(results))
    # return render_template("EVP.html", results=list(results))

@app.route("/alt_fuel_stations")
def alt_fuel_stations():

    # print("get_data")
    query={"State":"TX"}
    results= mongo.db.alt_fuel_stations.find(query)
    return jsonify(list(results))





    
if __name__ == '__main__':
    app.run(debug=True)
