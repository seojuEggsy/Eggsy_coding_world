import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS todo
             (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')

conn.commit()
