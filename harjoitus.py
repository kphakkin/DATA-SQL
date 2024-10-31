import sqlite_connection as db
import csv


connection = db.conn

cursor = connection.execute("SELECT * \
                            FROM movies \
                            limit 10")

rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]

with open('harjotus.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow[column_names]
    writer.writerows(cursor)