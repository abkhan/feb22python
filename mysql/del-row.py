import mysql.connector as mysql

db = mysql.connect(
    host = "abkhan.tplinkdns.com",
    user = "root",
    passwd = "abkhan",
    database = "pythonClass"
)

cursor = db.cursor()

## defining the Query
query = "DELETE FROM test44 WHERE user_name = 'Ten'"

## executing the query with values
cursor.execute(query)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "record deleted")
