import sqlite3
import time
import numpy as np 

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


def get_temperatures(ID):
    conn, c = get_db(db)
    try:
        c.execute('''SELECT temperature, time FROM temperatures
                      WHERE probe=?''', (ID,))
        ret = np.asarray(c.fetchall())
    except:
        print 'Problem retreiving temperatures'
        pass

    temps = list(ret[:, 0])
    times = list(ret[:, 1])

    #print temps, times
    return {'probe_id': ID, 'temperaures':temps, 'timestamps':times}

    
def get_temperatures_interval(ID, time_interval):
    conn, c = get_db(db)
    try:
        c.execute('''SELECT temperature, time FROM temperatures
                      WHERE probe=? AND (? - time < ?)''', (ID,time.time(), time_interval))
        ret = c.fetchall()   
    except:
        print 'Problem retreiving temperatures'
        pass
    return ret

setup_db(db)


print get_temperatures(1)
