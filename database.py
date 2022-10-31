from cProfile import label
from cgitb import text
from email.header import Header
from tkinter import*
from wsgiref import headers
import mysql.connector
from tabulate import tabulate

H=Tk()
global input1
global input2
global input3
global input4
H.config(background='orange')
H.geometry("500x500")
Label(H, text="Database").pack()
#FUNCTIONS

def erorr():

    erorr=Tk()
    erorr.geometry("300x200")
    erorr.title('Not available')
    alert=Label(erorr,text="Not available")
    alert.pack()

def done():
    d = Tk()
    d.title("Operation completed successfully")
    alert=Label(d,text="Operation completed succsessfully")
    alert.pack()












#database
def insert():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database"
    )

    mycursor = mydb.cursor()



    sql = "INSERT INTO Data (Name, Id, Phone, Email) VALUES (%s, %s, %s, %s)"
    val = (input1.get(), input2.get(), input3.get(), input4.get())

    mycursor.execute(sql, val)

    mydb.commit()
    done()

def update():
    up = Tk()
    up.config(background='orange')
    up.geometry("500x500")
    up.title("update")
    mYdata = [
        input1.get(), input2.get(), input3.get(), input4.get()
    ]

    la = Label(up, text=(tabulate (mYdata,)))
    la.place(x="300", y="100")

    inputa1 = Entry(up)
    inputa2 = Entry(up)
    inputa3 = Entry(up)
    inputa4 = Entry(up)
    #LABEL
    label1 = Label(up, text="Name")
    label2 = Label(up, text="ID")
    label3 = Label(up, text="Phone")
    label4 = Label(up, text="Email")
    label1.place(x=250, y=50)
    label2.place(x=250, y=150)
    label3.place(x=250, y=250)
    label4.place(x=250, y=350)
    #place
    inputa1.place(x=100, y=50)
    inputa2.place(x=100, y=150)
    inputa3.place(x=100, y=250)
    inputa4.place(x=100, y=350)
    btn= Button(up, text="Done", command=don)

def don():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="database"
    )



    mycursor = mydb.cursor()

    sql = "UPDATE FROM Data WHERE address = 'input1.get()'"
    sql2 = "UPDATE FROM Data WHERE address = 'input2.get()'" 
    sql3 = "UPDATE FROM Data WHERE address = 'input3.get()'"
    sql4 = "UPDATE FROM Data WHERE address = 'input4.get()'"

    mycursor.execute(sql, sql2, sql3, sql4)


    mydb.commit()

    don()



def read():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase"
    )
    mycursor = mydb.cusor()
    data_read = Tk()
    data_read.title("Data read")
    la = Label(up, text=(tabulate (mycursor.fetchall())))
    la.place(x="300", y="100")


def Delete():
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM customers WHERE address = 'input1.get()'"
    sql2 = "DELETE FROM customers WHERE address = 'input2.get()'" 
    sql3 = "DELETE FROM customers WHERE address = 'input3.get()'"
    sql4 = "DELETE FROM customers WHERE address = 'input4.get()'"

    mycursor.execute(sql, sql2, sql3, sql4)

    mydb.commit()

    done()



#INPUTS
input1 = Entry(H)
input2 = Entry(H)
input3 = Entry(H)
input4 = Entry(H)
#LABEL
label1 = Label(H, text="Name")
label2 = Label(H, text="ID")
label3 = Label(H, text="Phone")
label4 = Label(H, text="Email")
label1.place(x=250, y=50)
label2.place(x=250, y=150)
label3.place(x=250, y=250)
label4.place(x=250, y=350)
#place
input1.place(x=100, y=50)
input2.place(x=100, y=150)
input3.place(x=100, y=250)
input4.place(x=100, y=350)
#buttons
btn1=Button(H,text='insert',command =insert)
btn1.place(x=350 , y = 50)
btn2=Button(H,text='update',command =update)
btn2.place(x=350 , y = 150)
btn3=Button(H,text='Read',command =read)
btn3.place(x=350 , y = 250)
btn4=Button(H,text='Delete',command =Delete)
btn4.place(x=350 , y = 350)
H.mainloop()
