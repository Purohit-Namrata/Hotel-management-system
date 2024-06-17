from tkinter import *
from tkinter import messagebox
import pymysql


def addroomss():
    RoomNO = custInfo1.get()
    RoomType = custInfo2.get()
    Status = custInfo3.get()
     
    insertCust = "insert into "+roomTable+" values('"+RoomNO+"','"+RoomType+"','"+Status+"')"
    try:
        cur.execute(insertCust)
        con.commit()
        messagebox.showinfo('Sucess',"Room Added successfully")
    except:
        messagebox.showinfo("Error","Room Already Exists")    

    root.destroy()



def addrooms():
    global custInfo1, custInfo2, custInfo3, custInfo4, Canvas1, con, cur, roomTable,root

    root= Tk()
    root.title("Add Rooms")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    con = pymysql.connect(host="localhost",user="root",password="ROOT123",database="Hotel_man")
    cur = con.cursor()

    roomTable= "rooms"     

    headingLabel = Label(root, text="Add Rooms", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 = Label(labelFrame,text="Room No :",bg='black',fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    custInfo1 = Entry(labelFrame)
    custInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    
    lb2 = Label(labelFrame,text="Room Type : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    custInfo2 = Entry(labelFrame)
    custInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
    
    lb3 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
    
    custInfo3 = Entry(labelFrame)
    custInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
   
    SubmitBtn = Button(root,text="Add Room",bg='Orange', fg='black',command=addroomss)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='Yellow', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
