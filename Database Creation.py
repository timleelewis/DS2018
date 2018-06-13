import sqlite3


connection = sqlite3.connect("project.db")
cursor = connection.cursor()


sql_command = """
CREATE TABLE main (
ID INTEGER,
user INTEGER, 
tasks VARCHAR, 
postingTime DATETIME, 
deadline DATETIME, 
finishedStatus VARCHAR);"""

cursor.execute(sql_command)
