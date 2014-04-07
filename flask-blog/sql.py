# sql.py - Create a SQLite3 table and populate it with data

import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:

    # get the connection object
    c = connection.cursor()

    # create the Table
    c.execute("""CREATE TABLE posts
        (title TEXT, post TEXT)""")

    # insert dummy data into tables
    c.execute('INSERT INTO posts VALUES("Good","I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well","I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent","I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay","I\'m okay.")')

