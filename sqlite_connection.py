import sqlite3
from sqlite3 import Error


#AINA try-except
#käytä tiedostojen käsittelyssä
#käytä tietokannoissa 
try:
    conn = sqlite3.connect("./databases/movies.db")
except Error as e:
    print(e)
