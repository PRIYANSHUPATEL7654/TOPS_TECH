import mysql.connector

try:
    db=mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "PSP76542003",
        database = "advanced_sql"
    )
    cursor = db.cursor()
    print("Database connected")

except mysql.connector.Error as err:
    print("Database is not connected",err)

#Data viewing query
def viewdata():
    # try:
    #     tab_name = input("Enter table name : ")
    #     sql = "select * from %s"
    #     val = (tab_name,)
    #     cursor.execute(sql,val)
    #     db.commit()

    #     print("Data viewed successfully")

    # except mysql.connector.Error as err:
    #     print("Error viewing data:",err)

    try:
        cursor=db.cursor()
        cursor.execute("select * from stud_marks")
    
        data=cursor.fetchall()
        
        for i in data:
            print(i)
    except mysql.connector.Error as err:
        print("my data not fetch")

# viewdata()

# Data insertion query
def insertdata():
    try:
        id = int(input("Enter your id : "))
        name=input("Enter your name : ")
        sub=input("Enter you subject : ")
        marks = int(input("Enter your marks : "))

        sql = "insert into stud_marks(id,name,sub,marks) values (%s,%s,%s,%s)"
        val = (id,name,sub,marks)

        cursor.execute(sql,val)
        db.commit()
        
        print("Data inserted successfully")

    except mysql.connector.Error as err:
        print("Error inserting data:", err)
    
# insertdata()

# Data updation query
def updatedata():
    try:
        id = int(input("Enter id whose data needs to be updated : "))
        choice = int(input("1. NAME\n2. SUBJECT\n3. MARKS\nEnter you choice from above of which you want to change data : "))
        match choice:
            case 1:
                name = input("Enter updated name : ")
                sql = "update stud_marks set name = (%s) where id = (%s)"
                val = (name,id)
            case 2:
                sub = input("Enter updated subject : ")
                sql = "update stud_marks set sub = (%s) where id = (%s)"
                val = (sub,id)
            case 3:
                marks = int(input("Enter updated marks : "))
                sql = "update stud_marks set marks = (%s) where id = (%s)"
                val = (marks,id)
            case _ :
                print("Invalid choice")

        cursor.execute(sql,val)
        db.commit()

        print("Data updated successfully")

    except mysql.connector.Error as err:
        print("Error updating data:", err)

# updatedata()

# Data deletion query
def deletedata():
    try:
        id = int(input("Enter id whose data needs to be deleted : "))
        sql = "delete from stud_marks where id = (%s)"
        val = (id,) # If there is a single val that needs to be passed then we have to insert a comma at last because it treats val as tuple and not int

        cursor.execute(sql,val)
        db.commit()

        print("Data deleted successfully")

    except mysql.connector.Error as err:
        print("Error deleting data:", err)
    
# deletedata()

while True:
    choice = int(input("1. view\n2. insert\n3. update\n4. Delete\n5. exit\nEnter you choice from above of which you want to change data : "))
    match choice:
        case 1:
            viewdata()
        case 2:
            insertdata()
        case 3:
            updatedata()
        case 4:
            deletedata()
        case 5:
            break
        case _ :
            print("Invalid choice")