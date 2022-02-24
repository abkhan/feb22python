import mysql.connector as mysql

db = mysql.connect(
    host = "abkhan.tplinkdns.com",
    user = "root",
    passwd = "abkhan",
    database = "pythonClass"
)

cursor = db.cursor()

## defining the Query
query = "UPDATE test44 SET name = 'Kareem' WHERE user_name = 'peter'"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()

print(cursor.rowcount, "record(s) updated")