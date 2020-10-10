import sqlite3

conn = sqlite3.connect('../Level 2/Challenge 2/Data.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS Employees')

c.execute('''CREATE TABLE Employees 
	("Employee ID" INTEGER, "First Name" TEXT, "Last Name" TEXT, Age INTEGER, Salary TEXT)''')

records = [(1, 'Evelyn', 'Grace', 26, '280$'),
		   (2, 'Olivia', 'Harper', 28, '320$'),
		   (3, 'Robert', 'Hall', 24, '310$'),
		   (4, 'Doug', 'Judy', 32, '370$'),
		   (5, 'Leo', 'Valdez', 22, '270$')]

c.executemany('INSERT INTO Employees VALUES (?, ?, ?, ?, ?)', records)

for row in c.execute('SELECT * FROM Employees'):
	print(row)

conn.commit()
conn.close()