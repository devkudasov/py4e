import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fh = open('mbox.txt')
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    host = pieces[1].split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (host,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (host,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (host,))
    conn.commit()

cur.close()
