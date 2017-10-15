from flask import Flask, jsonify, request, redirect
from flaskext.mysql import MySQL
import os
import env

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = env.MYSQL_DATABASE_USER
app.config['MYSQL_DATABASE_PASSWORD'] = env.MYSQL_DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = env.MYSQL_DATABASE_DB
app.config['MYSQL_DATABASE_HOST'] = env.MYSQL_DATABASE_HOST
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def index():
    return redirect("/static/index.html", code=302)

@app.route("/getperson")
def getperson():
    cursor.execute("SELECT * from Persons")
    data = cursor.fetchall()
    #print(data)
    return jsonify(data)

@app.route("/person", methods=['get'])
def add_person():
    name = request.args.get('name', None)
    lastname = request.args.get('lastname', None)

    cursor.execute("INSERT INTO Persons (Firstname, Lastname) VALUES (%s, %s)", (name, lastname))
    conn.commit()
    
    return jsonify("added %s $s", (name, lastname))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
