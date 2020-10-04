import sqlite3

dbconnect = sqlite3.connect("mydatabase.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
cursor.execute('''INSERT INTO temps values ('2020-10-03', 'now', "kitchen", 20.4)''');
dbconnect.commit();
cursor.execute('SELECT * FROM temps');
for row in cursor:
    print(row['tdate'], row['ttime'], row['zone'], row['temperature']);
    
cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"');
for row in cursor:
    print(row['sensorID'], row['type'], row['zone']);

cursor.execute('SELECT * FROM sensors WHERE type="door"');
for row in cursor:
    print(row['sensorID'], row['type'], row['zone']);
dbconnect.close();