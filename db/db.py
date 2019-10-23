#import mysql.connector as mysql
conn = mysql.MySQLConnection(
    host="evergreen.mysql.database.azure.com",
    port=3306,
    user="evergreenadmin@evergreen",
    password=".evergreen1",
    database="evergreen"
)
