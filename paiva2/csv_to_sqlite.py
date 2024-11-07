import sqlite3
from pathlib import Path
import pandas as pd

# LUO tyhjän tiedoston
Path('./databases/employees.db').touch()

PATH_db = './databases/employees.db'
PATH_csv = './csvs/us-500.csv'

with sqlite3.connect(PATH_db) as conn:
    cursor = conn.cursor()

employee_data = pd.read_csv(PATH_csv, encoding='latin-1', sep=',')

cursor.execute("CREATE TABLE IF NOT EXISTS all_employees\
               (first_name TEXT, \
               last_name TEXT, \
               company_name TEXT, \
               address TEXT, \
               city TEXT, \
               county TEXT, \
               state TEXT, \
               zip REAL, \
               phone1 TEXT, \
               phone2 TEXT, \
               email TEXT, \
               web\
               )") # voidaan jakaa usealle riville myös multilinestringillä eli kolmet hipsut """ """

employee_data.to_sql('all_employees', conn , if_exists='replace', index=True)