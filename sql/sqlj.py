# SQLite Functions

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # create a dictionary of SQL queries
    sql = {'average': "SELECT avg(population) FROM population",
        'maximum': "SELECT max(population) FROM population",
        'minimum': "SELECT min(population) FROM population",
        'sum': "SELECT sum(population) FROM population",
        'count': "SELECT count(population) FROM population"}

    # Run each SQL query in the dictionary
    for keys, values in sql.iteritems():

        # run SQL
        c.execute(values)

        # fetch the results
        results = c.fetchone()

        # output the results
        print keys + ":", results[0]

