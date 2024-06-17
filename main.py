from tkinter import *
import pymysql
from add_customer_list import *
from checkin import *
from checkout import *
from roomlist import *
from addrooms import *

con=pymysql.connect(host='localhost',user='root',password='ROOT123')

cursor=con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Hotel_man")
cursor.execute("USE Hotel_man")

cursor.execute("CREATE TABLE Customer(FNAME VARCHAR(20) PRIMARY KEY NOT NULL, LNAME VARCHAR(20) NOT NULL, PHNO INT NOT NULL)")
cursor.execute("CREATE TABLE Issued_rooms(RoomNo int AUTO_INCREMENT PRIMARY KEY NOT NULL, Issued_to VARCHAR(20)NOT NULL, Status VARCHAR(20) NOT NULL)")
cursor.execute("CREATE TABLE rooms (RoomNo int AUTO_INCREMENT PRIMARY KEY NOT NULL, RoomType VARCHAR(30) NOT NULL, Status VARCHAR(30) NOT NULL)")

root=Tk()
root.title("Hotel Management System")
root.minsize(width=400,height=400)
root.geometry("600x500")

headingLabel = Label(root, text="Hotel Management System", bg='black', fg='white', font=('Courier',15))
headingLabel.pack()

btn1 = Button(root, text="Add Customer Details", bg='Black',fg='white',command =add_customer_details)
btn1.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)

btn2 = Button(root, text="Check In", bg='Black',fg='white',command=checkinn)
btn2.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="Check Out",bg='black', fg='white',command=checkout)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="View Customer List",bg='black', fg='white',command = View)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Add Rooms",bg='black', fg='white',command = addrooms)
btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn6 = Button(root,text="Room List",bg='black', fg='white',command = View_Room)
btn6.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()

