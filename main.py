import sqlite_connection as db
import pandas as pd
import csv
import json

connection = db.conn


cursor = connection.execute("SELECT * \
                          FROM movies \
                          LIMIT 10")

rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]

with open('movies.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow[column_names]
    writer.writerows(cursor)

print('Valmis')



connection.close()