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

dict = [dict(zip(column_names, row)) for row in rows]

with open('movies_to_tson.json',  'w') as json_file:
    json.dump(dict, json_file, indent=4)

print("json file tallennettu")

connection.close()