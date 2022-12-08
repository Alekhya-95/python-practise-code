"""
select ID as ManagerId, name as ManagerName, Salary, DepartID
 from Employee e join Department d where e.ID = d.ManagerID


db = SqlALchemy(app)

db.queryall().filter(id).first()
"""
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

data = [{'id':1,'name':"Alekhya","salary":20000,'departID':34254},
{'id':2,'name':"Sony","salary":30000,'departID':39684}]

@app.route("/Employees", methods= ["GET", "POST"])
def getAndPostEmployees():
    if request.method == "GET":
        if len(data) != 0:
            return data, 200

    if request.method == "POST":
        new_id = data[-1]['id'] + 1
        new_record = {'id': new_id, 'name':"Sai","salary":40000,'departID':93857}
        data.append(new_record)
        return "Data Added Successfully", 201


@app.route("/Employees/int:<id>", methods= ["GET", "PUT", "DELETE"])
def getAndPutAndDeleteEmployees(id):
    if request.method == "GET":
        if len(data) != 0:
            for i in data:
                record = data[i].get(id)
            return record, 200

    if request.method == "PUT":
        new_record = {'name':"Sai","salary":45000,'departID':93857}
        for i in data:
            record = data[i].get(id)
            record.update(new_record)
        return "Data Updated Successfully", 201

    if request.method == "DELETE":
        if len(data) != 0:
            for i in data:
                record = data[i].get(id)
                data.remove(record)
            return "Record Deleted Successfully", 200


