import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "",
    database = "nbdatabase"
)

mycursor = mydb.cursor()

def checkUsr(val):
    mycursor.execute("SELECT id,fname FROM `myapp_student` WHERE funq='" + str(val) + "';")
    myresult = mycursor.fetchone()

    usrdata = []
    if myresult:
        for x in myresult:
            usrdata.append(x)
        return usrdata
    else:
        return False


def getNotices(acayr, dpt):
    mycursor.execute("SELECT * FROM `myapp_notice` WHERE (acayear = '"+ str(acayr) +"' OR acayear = '0') AND (dpt = '"+ str(dpt) +"' OR dpt = 'all');")
    myresult = mycursor.fetchall()

    collection = []
    if myresult:
        for x in myresult:
            collection.append(x)
        return collection
    else:
        return False


def getUserImages():
    mycursor.execute("SELECT * FROM `myapp_uimage`")
    myresult = mycursor.fetchall()

    collection = []
    usr = ''
    if myresult:
        for x in myresult:
            collection.append(x[0])
            usr = x[1]
        return collection, usr
    else:
        return False


def facialFunq(value,usr):
    mycursor.execute("UPDATE `myapp_student` SET `funq` = '"+ str(value) +"' WHERE `id` = '"+ str(usr) +"';")
    mydb.commit()

def truncateSnap():
    query = "TRUNCATE `nbdatabase`.`myapp_uimage`;"
    mycursor.execute(query)
    mydb.commit()

# # INSERT DATA TO THE DB

# sql = "INSERT INTO students (uindex, name, funq) VALUES (%s, %s, %s)"
# val = ('3601', "Dilmi", "101000111017001.111")
# mycursor.execute(sql, val)
# mydb.commit()



# # SELECT ONE DATA ROW FROM A DB

# mycursor.execute("SELECT name FROM students WHERE uindex=3606")
# myresult = mycursor.fetchone()
# for x in myresult:
#   print(x)

# # SELECT ALL DATA FROM A DB

# datasets = []

# mycursor.execute("SELECT * FROM students")
# myresult = mycursor.fetchall()
# for x in myresult:
#     datasets.append(x)
#     print(x)

# print(datasets[1][1])
