from peewee import MySQLDatabase


#local
db = MySQLDatabase(
    'db-crud',
    user = 'root',
    password = '',
    host = 'localhost',
    port = 3306 
)