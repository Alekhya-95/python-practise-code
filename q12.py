from urllib import request
from flask import Flask, render_template
import db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/student", methods = ['POST'])
def createStudent():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form['name']
            address = request.form['address']
            with sqlite3.connect('test.db') as con:
                cur = con.cursor()
                cur.execute("INSERT into Student (name, address)")
                con.commit()
                msg = "Student added successfully."
        except:
            con.rollback()
            msg = "Cant add Student."
        con.close()



if __name__ == "__main__":
    app.run()