import sqlite3
from unicodedata import name

con = sqlite3.connect("test.db")

print("DB Created.")

con.execute("create table Student (id INTEGER PRIMARY KEY AUTOINCREMENT),name STRING NOT NULL, address STRING NOT NULL")

print("Table got created.")

con.close()