from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()
#allow all origins (response header Access-Control-Allow-Origin='*')
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_db(cur):
    print('Creating DB USU..')
    cur.execute('''CREATE TABLE IF NOT EXISTS USU
                  (Name TEXT NOT NULL, Age INT NOT NULL, Position INT NOT NULL, pk INTEGER PRIMARY KEY AUTOINCREMENT)''')
    cur.execute('''CREATE INDEX IF NOT EXISTS age_idx ON USU (Age)''')
    cur.execute('''CREATE INDEX IF NOT EXISTS position_idx ON USU (Position)''')

def gen_json(curs):
    """
        From Python Essential Reference by David Beazley
    """
    #fields = [d[0].lower() for d in curs.description]

    data = []
    for row in curs.fetchall():
        d = dict()
        #for i in range(len(row)) :
         #   print(curs.description[i][0])
        for name, val in zip(curs.description, row) :
            d[name[0]] = val
        data.append(d)
    return data

@app.get("/gendb")
def genDB():
    """
       GFG Test Init
    """
    connection = sqlite3.connect('usu.db')
    cursor = connection.cursor();
    cursor.execute('''DROP TABLE USU''')
    create_db(cursor)

    print('Populating test table USU by test data..')
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

@app.get("/")
def fetchRoot():
    """
       GFG API info
    """
    return {"version": "1.0.0","methods": "GET,PUT,POST"}

@app.get("/table")
def fetchTable():
    """
       GFG Fetches the whole table
    """
    connection = sqlite3.connect('usu.db')
    cursor = connection.cursor()
    cursor.execute(''' SELECT * FROM USU''')
    data = gen_json(cursor)
    connection.close()
    #return (data[0] if data else None)
    return data

@app.get("/avgage")
def fetchAvgAge():
    """
       GFG Fetches the average age
    """
    connection = sqlite3.connect('usu.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT Position, count(*) as Count, sum(Age) / Count(*) as `Average Age` FROM USU GROUP BY Position ORDER BY Position''')
    data = gen_json(cursor)
    connection.close()
    return data

@app.get("/agedistr")
def fetchAgeDistr():
    """
       GFG Fetches the age distribution
    """
    connection = sqlite3.connect('usu.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT count(*) as `Count of Employees`,  CASE  WHEN  Age < 20  THEN  " 20 -" WHEN  Age >=20  and Age<=40 THEN  " 20 - 40" WHEN  Age >40  and Age<60 THEN  "41 - 60" ELSE "60+" END AS `Average Age` FROM USU GROUP BY `Average Age` ORDER BY  `Average Age` ASC''')
    data = gen_json(cursor)
    connection.close()
    return data

@app.put("/update")
def updateRow(name: str, age: int, position: str, pk: int = 0):
    """
       GFG Updates or adds row
    """
    print("updateRow")
    connection = sqlite3.connect('usu.db')
    cursor = connection.cursor()
    if pk > 0:
        print("update")
        tuple = (name, age, position, pk)
        cursor.execute('''UPDATE USU SET Name = ?, Age = ?, Position =? WHERE pk = ?''', tuple)
    else:
        print("insert")
        tuple = (name, age, position)
        cursor.execute('''INSERT INTO USU (Name, Age, Position) VALUES (?,?,?)''',tuple)
    connection.commit()
    connection.close()
    return

@app.post("/delete")
def deleteRow(pk: int):
    """
       GFG deletes Row
    """
    connection = sqlite3.connect('usu.db')
    cursor = connection.cursor()
    tuple = (pk,)
    cursor.execute('''DELETE FROM USU WHERE pk = ?''', tuple)
    connection.commit()
    connection.close()
    return

#test for the db existence
connection = sqlite3.connect('usu.db')
cursor = connection.cursor()
cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='USU' ''')

#if the count is 1, then table exists
if cursor.fetchone()[0] != 1 :
    create_db(cursor)
connection.commit()
connection.close()
