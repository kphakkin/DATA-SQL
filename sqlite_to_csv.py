import sqlite_connection as db
import pandas as pd
import csv


connection = db.conn

cursor = connection.execute("SELECT * \
                          FROM movies \
                          LIMIT 10")

rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]

with open('movies.csv', 'w', newline='') as file: 
    writer = csv.writer(file, delimiter=';')
    writer.writerow(column_names)
    writer.writerows(rows)

print('Valmis')
# Toinen tapa to csv
df = pd.read_sql("SELECT * \
                          FROM movies \
                          LIMIT 10", connection)
df.to_csv("movies_using_to_csv.csv", sep=';')
print("valmis to_csv")

connection.close()