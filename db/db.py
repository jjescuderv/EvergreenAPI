import mysql.connector as mysql
conn = mysql.MySQLConnection(
    host="evergreen-server.mysql.database.azure.com",
    port=3306,
    user="evergreenadmin@evergreen-server",
    password=".evergreen1",
    database="evergreen"
)
