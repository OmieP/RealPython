# INSERT Command with Error Handler

# import the SQL library
import sqlite3

# create the connection
conn = sqlite3.connect("new.db")

# get a cursor object to execute SQL statements
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', \
        'NY', 8200000)")
    cursor.execute("INSERT INTO populations VALUES('San Franciso',  \
        'CA', 800000)")

    # commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print "Oops! Something went wrong! Try again..."
# Close the object
conn.close()
