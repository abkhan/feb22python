import mysql.connector as mysql

db = mysql.connect(
    host = "abkhan.tplinkdns.com",
    user = "groupOne",
    passwd = "update",
    database = "pythonClass"
)

cursor = db.cursor()

## defining the Query
query = "SELECT * FROM test44"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)
