from tkinter import *
from tkinter import messagebox
import pymysql


con = pymysql.connect(host="localhost",user="root",password="ROOT123",database="Hotel_man")
cur = con.cursor()

roomTable = "rooms" 
issuedTable = "issued_rooms" 

allRoomNo = []

def checkinn():
    global issueBtn,labelFrame,lb1,inf1,inf2,inf3,quitBtn,root,Canvas1,status

    RoomNo = inf1.get()
    issueto = inf2.get()
    status = inf3.get()
    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractRoomNo = "select RoomNo from"+roomTable
    try:
        cur.execute(extractRoomNo)
        con.commit()
        for i in cur:
            allRoomNo.append(i[0])
        
        if RoomNo in allRoomNo:
            checkavail = "select status from"+roomTable+"where RoomNo = '"+RoomNo+"'"
            cur.execute(checkavail)
            con.commit()
            for i in cur:
                check = i[0]
            
    
            if check == 'avail':
                status = True
            else:
                status  = False
        else:
            messagebox.showinfo("Error","RoomNo not availabe")
    except:
        messagebox.showinfo("Error","Can't fetch Room No's")

    issueSql = "insert into"+issuedTable+" values('"+RoomNo+"','"+issuedto+"')"
    show = "select * from " +issuedTable


    upadateStatus = "update "+roomTable+" set status = 'issued' where RoomNo ='"+RoomNo+"'"
    try:
        if RoomNo in allRoomNo and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(upadateStatus)
            con.commit()
            messagebox.showinfo("Success", "Checked In Succesfully")
            root.destroy()
        else:
            allRoomNo.clear()
            messagebox.showinfo("Success","Checked In Succesffuly")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","This value entered is wrong, Try again")
    
    print(RoomNo)
    print(issuedto)

    allRoomNo.clear()
def checkin():
    global issueBtn,labelframe,lb1,inf1,inf2,quitBtn,root,Canvas1,status

    root = Tk()
    root.title("Check In")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
        
    headingLabel = Label(root, text="Issue Room", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5) 

    #Room No
    lb1 = Label(labelFrame, text="Room No:", bg='black',fg='white')
    lb1.place(relx=0.05,rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2,relwidth=0.62)
    
    #First Name
    lb2 = Label(labelFrame,text="First Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)

    #Issue Date
    lb3 = Label(labelFrame,text="Issue Date: ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4)
        
    inf3 = Entry(labelFrame)
    inf3.place(relx=0.3,rely=0.4, relwidth=0.62)


    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=checkinn)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
