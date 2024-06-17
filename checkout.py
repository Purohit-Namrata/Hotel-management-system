from tkinter import *
from tkinter import messagebox
import pymysql

con = pymysql.connect(host="localhost",user="root",password="ROOT123",database="Hotel_man")
cur = con.cursor()

roomTable = "rooms" 
issueTable = "issued_rooms" 

allRoomNo = [] 

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,status
    
    RoomNo = bookInfo1.get()

    extractRoomNo = "select RoomNo from "+issueTable
    cur.execute(extractRoomNo)
    con.commit()
    for i in cur:
        allRoomNo.append(i[0])
        
    if RoomNo in allRoomNo:
            checkAvail = "select status from "+roomTable+" where RoomNo = '"+RoomNo+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Room Number not present")
    except:
        messagebox.showinfo("Error","Can't fetch Room Number")
    
    
    issueSql = "delete from "+issueTable+" where RoomNo = '"+RoomNo+"'"
  
    print(RoomNo in allRoomNo)
    updateStatus = "update "+roomTable+" set status = 'avail' where RoomNo = '"+RoomNo+"'"
    try:
        if RoomNo in allRoomNo and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Checked Out  Successfully")
        else:
            allRoomNo.clear()
            messagebox.showinfo('Message',"Please check the Room No")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allRoomNo.clear()
    root.destroy()
    
def checkout(): 
    
    global bookInfo1,SubmitBtn,quitBtn,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Check Out")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    headingLabel = Label(root, text="Check Out", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Room No : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    SubmitBtn = Button(root,text="Return",bg='Grey', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='Grey', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
