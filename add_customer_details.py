from tkinter import *
from tkinter import messagebox
import pymysql


def addcustomer():
    Fname = custInfo1.get()
    Lname = custInfo2.get()
    PHNO = custInfo3.get()
    if ((len(PHNO)==10) and (Fname==([a-z]+)) and (Lname== ([a-z]+))  and (PHNO==[1-9]+)):
        insertCust = "insert into "+custTable+" values('"+Fname+"','"+Lname+"','"+PHNO+"')"
        cur.execute(insertCust)
        con.commit()
        messagebox.showinfo('Success',"Customer Added successfully")
    else:
        messagebox.showinfo("Error","Data is not valid")
     root.destroy()

def add_customer_details():
    global custInfo1, custInfo2, custInfo3, con, cur, custTable

    root= Tk()
    root.title("Add Customer details")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    con = pymysql.connect(host="localhost",user="root",password="ROOT123",database="Hotel_man")
    cur = con.cursor()
    
    custTable= "Customer"
    headingLabel = Label(root, text="Add Customer Details", bg='black', fg='white', font=('Courier',15))
    headingLabel.pack()

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 = Label(labelFrame,text="First Name:",bg='black',fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    custInfo1 = Entry(labelFrame)
    custInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    
    lb2 = Label(labelFrame,text="Last Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    custInfo2 = Entry(labelFrame)
    custInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
    
    lb3 = Label(labelFrame,text="Phone Number : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    custInfo3 = Entry(labelFrame)
    custInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
   
    SubmitBtn = Button(root,text="Add Details",bg='Grey', fg='black',command=addcustomer)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='Grey', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
