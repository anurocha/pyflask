from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def hello():
    cursor.execute("SELECT * from Persons")
    data = cursor.fetchall()
    #print(data)
    return jsonify(data)

@app.route("/person", methods=['get'])
def add_person():
    name = request.args.get('name', None)
    lastname = request.args.get('lastname', None)

    cursor.execute("INSERT INTO Persons (FirstName, Lastname) VALUES (%s, %s)", (name, lastname))
    
    return jsonify("added %s $s", (name, lastname))

if __name__ == "__main__":
    app.run()