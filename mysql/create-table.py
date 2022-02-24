## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "abkhan.tplinkdns.com",
    user = "groupTen",
    passwd = "groupTen10",
    database = "pythonClass"
)

cursor = db.cursor()

## creating a table called 'users' in the 'datacamp' database
cursor.execute("CREATE TABLE test44 (name VARCHAR(255), user_name VARCHAR(255))")

db.close()

