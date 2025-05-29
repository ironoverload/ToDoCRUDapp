import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()