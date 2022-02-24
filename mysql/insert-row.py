import mysql.connector as mysql

db = mysql.connect(
    host = "abkhan.tplinkdns.com",
    user = "root",
    passwd = "abkhan",
    database = "pythonClass"
)

cursor = db.cursor()

## defining the Query
query = "INSERT INTO test44 (name, user_name) VALUES (%s, %s)"
## storing values in a variable
values = ("Group", "Ten")

## executing the query with values
cursor.execute(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "record inserted")
