from tkinter import *
from tkinter import messagebox
import pymysql

con = pymysql.connect(host="localhost",user="root",password="ROOT123",database="Hotel_man")
cur = con.cursor()

roomTable="rooms" 

def View_Room(): 
    root = Tk()
    root.title("Rooms List")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
   
    headingLabel = Label(root, text="View Room List", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-40s%-60s%-70s"%('RoomNo','RoomType','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from "+roomTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-50s%-60s%-80s"%(i[0],i[1],i[2]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Close",bg='Dark Greyish Orange', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    
