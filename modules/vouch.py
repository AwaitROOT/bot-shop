import sqlite3

conn = sqlite3.connect('data/data.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS vouch (
        user INTEGER,
        stars INTEGER
    )
''')
conn.commit()
conn.close()


def getAverage():
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT AVG(stars) FROM vouch;")
        average = c.fetchone()[0]
        return average
    finally:
        conn.close()


def get(user):
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vouch WHERE user = ?;", (user,))
        data = c.fetchone()
        if data:
            return data[0]
        else:
            return None
    finally:
        conn.close()


def set(user, stars):
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    try:
        c.execute("UPDATE vouch SET stars = ? WHERE user = ? ;", (stars, user))
        if c.rowcount == 0:
            raise ValueError("Element does not exist in the database.")
        return True
    except:
        c.execute("INSERT INTO vouch (user, stars) VALUES (?, ?);", (user, stars))
        return False
    finally:
        conn.commit()
        conn.close()


def delete(user):
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    try:
        c.execute("DELETE FROM vouch WHERE user = ?;", (user,))
        if c.rowcount == 0:
            raise ValueError("Element does not exist in the database.")
        return True
    except:
        return False
    finally:
        conn.commit()
        conn.close()