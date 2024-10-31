import sqlite_connection as db
import pandas as pd
from pathlib import Path

Path('leffat.db').touch()

connection = db.conn

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movies \
               (id INT, \
               title TEXT, \
               overview TEXT, \
               popularity REAL, \
               release_date TEXT, \
               vote_average REAL, \
               vote_count INT)")

movie_data = pd.read_csv('movies.csv',encoding='latin1')

movie_data.to_sql('movies', connection, if_exists='append',index=False)