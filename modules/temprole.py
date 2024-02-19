import sqlite3

conn = sqlite3.connect('data/data.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS temprole (
        user INTEGER,
        role INTEGER,
        time INTEGER
    )
''')
conn.commit()
conn.close()


def getAll(time):
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM temprole WHERE time < ?;", (time,))
        data = c.fetchall()
        if data:
            return data
        else:
            return None
    finally:
        conn.close()


def set(time, user, role):
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    try:
        c.execute("UPDATE temprole SET time = ? WHERE user = ? AND role = ?;", (time, user, role,))
        if c.rowcount == 0:
            raise ValueError("Element does not exist in the database.")
        return True
    except:
        c.execute("INSERT INTO temprole (time, user, role) VALUES (?, ?, ?);", (time, user, role,))
        return False
    finally:
        conn.commit()
        conn.close()


def delete(user, role):
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    try:
        c.execute("DELETE FROM temprole WHERE user = ? AND role = ?;", (user, role,))
        if c.rowcount == 0:
            raise ValueError("Element does not exist in the database.")
        return True
    except:
        return False
    finally:
        conn.commit()
        conn.close()