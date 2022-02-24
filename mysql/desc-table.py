import mysql.connector as mysql

db = mysql.connect(
    host = "abkhan.tplinkdns.com",
    user = "group10",
    passwd = "update",
    database = "pythonClass"
)

cursor = db.cursor()

## executing the statement using 'execute()' method
cursor.execute("DESC test44")

## printing the list of databases
print(cursor.fetchall())

db.close()

