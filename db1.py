import sqlite3

con = sqlite3.connect('mydatabase.db')
print("connection established")

cursorObj=con.cursor()
print("database created")


def createTable():
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text)")
    con.commit()
    print("table created")

def insertTable(entity):
    cursorObj.execute("INSERT INTO employees VALUES(?,?,?,?)", entity)
    con.commit()
    print("row inserted")
    

def updateTable(entity):
    try:
        cursorObj.execute("UPDATE employees SET salary=? where id=?",entity)
        con.commit()
        print("table updated")
    except sqlite3.OperationalError:
        pass
    
def delete(entity):
    cursorObj.execute("DELETE FROM employees where id=?",entity)
    con.commit()
    print("Row deleted")

def display():
    cursorObj.execute("SELECT * FROM employees")
    con.commit()
    rows = cursorObj.fetchall()
 
    for row in rows:
        print(row)
 
def displayEmp(entity):
    cursorObj.execute("SELECT * FROM employees where id=?",entity)
    con.commit()
    rows = cursorObj.fetchall()
 
    for row in rows:
         print(row)

 

print("enter your choice")
ch=int(input(""))
if(ch==1):
     createTable()
if(ch==2):
    print("enter the values")
    v1,v2,v3,v4=input(" ").split(" ")
    entity=(v1,v2,v3,v4)
    insertTable(entity)
    
if(ch==3):
    print("enter the salary value and id for updation")
    v1,v2=input(" ").split(" ")
    entity=(v1,v2)
    updateTable(entity)

if(ch==4):
    print("enter the id")
    v1=input(" ")
    entity=(v1)
    delete(entity)

if(ch==5):
    display()

if(ch==6):
    print("enter the emp id whose details you want to view")
    v1=input(" ")
    entity=(v1)
    displayEmp(entity)
    
    

        
