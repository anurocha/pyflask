import pymysql
import env

rds_host  = env.MYSQL_DATABASE_HOST
name = env.MYSQL_DATABASE_USER
password = env.MYSQL_DATABASE_PASSWORD
db_name = env.MYSQL_DATABASE_DB
port = 3306

conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=5, cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

def lambda_handler(event, context):
    cursor.execute("SELECT * from Persons")
    data = cursor.fetchall()
    return data