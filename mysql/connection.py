## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "abkhan.tplinkdns.com",
    user = "groupTen",
    passwd = "groupTen10"
)

print(db) # it will print a connection object if everything is fine

db.close()

