import sqlite3

connection = sqlite3.connect('database.db')

with open('resetdb.sql') as f:
    connection.executescript(f.read())