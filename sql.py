import sqlite3

db = 'brew_db.db'

def get_db(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    return conn, c

def setup_db(db_file):
    conn, c = get_db(db_file)
    c.execute('''CREATE TABLE IF NOT EXISTS temperatures
                 (probe INTEGER, temperature NUMBER, 
                  time NUMBER)''')
    conn.commit() # Save the changes

def write_temperature(probe_id, temp, timestamp):
    conn, c = get_db(db)
    c.execute('''INSERT INTO temperatures VALUES (?, ?, ?)''',
                  (probe_id, temp, timestamp))
    conn.commit()


setup_db(db)
