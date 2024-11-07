import sqlite3
from sqlite3 import Error
import os #operating system

# ctrl +k+c (comment), ctrl +k +u (uncomment)
# tai ctrl +' (TOGLE COMMENTS ON/OFF)

#region Versio 1
# versio 1
# try:
#     # sqlite3.connect luo tiedoston jos polku on olemassa
#     # jos polkua ei ole niin tulee virhe, koska ei luo kansioita
#     # piste kansioiden allussa viittaa nykyiseen kansioon
#     conn =sqlite3.connect("./databases/moviesDB.db")
#     if conn is None:
#         print("no connection")
#     else:
#         print(" CONNECTION OK")
# except Error as e:
#     print(e)
#     conn = None
# endregion

# region Versio 2 (Tarkistetaan polku)
db_path = "./databases/movies.db"

if os.path.exists(db_path):
    conn = sqlite3.Connection(db_path)
    print("db found and connected!")
else:
    print(f"can't connect to {db_path}")
    
# endregion

