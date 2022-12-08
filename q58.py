from flask import Flask

app = Flask(__name__)

data = [{'id':1,'name':"Alekhya","salary":20000,'departID':34254},
{'id':2,'name':"Sony","salary":30000,'departID':39684}]

@app.route("/Employees", methods= ["GET"])
def getAllEmployees():
    if len(data) != 0:
        return data, 200