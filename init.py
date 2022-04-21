import sqlite3

connection = sqlite3.connect('usu.db')
cursor = connection.cursor()
cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='USU' ''')

#if the count is 1, then table exists
if cursor.fetchone()[0] != 1 :
    print('Populating table USU..')
    cursor.execute('''CREATE TABLE IF NOT EXISTS USU
                  (Name TEXT NOT NULL, Age INT NOT NULL, Position INT NOT NULL, pk INTEGER PRIMARY KEY AUTOINCREMENT)''')
    cursor.execute('''CREATE INDEX IF NOT EXISTS age_idx ON USU (Age)''')
    cursor.execute('''CREATE INDEX IF NOT EXISTS position_idx ON USU (Position)''')

    data =  [{"name":"Milan", "age":"24", "position":"Frontend developer"},
             {"name":"Honza", "age":"30", "position":"Frontend developer"},
             {"name":"Jana", "age":"30", "position":"Frontend developer"},
             {"name":"Vera", "age":"36", "position":"Frontend developer"},
             {"name":"Zdenek", "age":"50", "position":"Frontend developer"},
             {"name":"Jarek", "age":"62", "position":"Frontend developer"},
             {"name":"Zuzana", "age":"63", "position":"Frontend developer"},
             {"name":"Karel", "age":"45", "position":"Backend developer"},
             {"name":"Josef", "age":"18", "position":"Backend developer"},
             {"name":"Petr", "age":"37", "position":"Backend developer"},
             {"name":"Roman", "age":"37", "position":"Backend developer"},
             {"name":"Roman", "age":"34", "position":"Product owner"},
             {"name":"Ales", "age":"43", "position":"Product owner"},
             {"name":"Jana", "age":"53", "position":"Scrum master"},
             {"name":"Jirka", "age":"28", "position":"Scrum master"},
             {"name":"Jirka", "age":"50", "position":"Scrum master"},
             {"name":"Alena", "age":"58", "position":"CEO"}]
    for row in data :
        print(row)
        tuple = (row["name"], row["age"], row["position"])
        cursor.execute('''INSERT INTO USU (Name, Age, Position) VALUES (?,?,?)''',tuple)

connection.commit()
connection.close()
