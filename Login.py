from tkinter import*
from tkinter.messagebox import *
import conn
from tkinter.messagebox import *
import lms as lib
import random as rd


win=Tk()


class Login_System:
    def __init__(self,win):
        self.win=win
        self.win.title('Library Login')
        self.win.geometry("1350x700+0+0")
        self.win.config(bg='powder blue')

        title=Label(self.win,text='Login System',font=('times new roman',40,'bold')).place(x=1,y=1,relwidth=1)

        Login_frame=Frame(self.win,borderwidth=4)
        Login_frame.place(x=400,y=200)
        lbl1=Label(Login_frame,text='USERNAME: ',font=('times new roman',12,'bold')).grid(row=0,column=0)
        lbl2=Label(Login_frame,text='PASSWORD: ',font=('times new roman',12,'bold')).grid(row=1,column=0)
        global user
        user=Entry(Login_frame,width=30)
        user.grid(row=0,column=1)
        global pas
        pas=Entry(Login_frame,show="*",width=30)
        pas.grid(row=1,column=1)
        global l
        l=db()
            
        btn=Button(Login_frame,text="Sign up",font=('times new roman',10,'bold'),borderwidth=4,width=17,command=create).grid(row=4,column=0,pady=30,padx=30)
        btn1=Button(Login_frame,text="Login",font=('times new roman',10,'bold'),borderwidth=4,width=17,command=l.log).grid(row=4,column=1,pady=30,padx=30)
        btn2=Button(Login_frame,text="Reset",font=('times new roman',10,'bold'),borderwidth=4,width=17,command=update).grid(row=4,column=2,pady=30,padx=30)
            
        
class db():
    def __init__(self):
        self.db=conn.getconn()
        self.mycursor=self.db.cursor()
    def Register(self):
        self.mycursor.execute(f"Insert into login values({rd.randint(100,999)},'{f1.get()}','{s1.get()}','{ad1.get()}','{ad2.get()}','{c1.get()}',{pcode.get()},{mobno.get()},'{u1.get()}','{p1.get()}')")
        if self.mycursor.rowcount > 0:
            showinfo(title = "Saved", message = "Record saved sucessfully")
            self.db.commit()
            screen.destroy()
            
        else:
            showinfo(title='Error',message='error occured please try again')
            screen.destroy()
    def log(self):
        self.l1=False
        self.mycursor.execute(f"Select Username,Password FROM login")
        for (Username,Password) in self.mycursor:
            if Username == user.get() and Password == pas.get():
                self.l1 = True
                break

        if self.l1 == True:
            lib.Library(user.get(),win)

        else:
            showinfo(title='Error',message='Error Please Try Again') 
        
        

    def reset(self):
        self.mycursor.execute(f"Update login Set Password= '{p2.get()}' WHERE Username='{u2.get()}'")
        if self.mycursor.rowcount > 0:
            showinfo(title = "Update", message = "Sucessfully Updated")
            self.db.commit()
            screen.destroy()
        else:
             showinfo(title='Error',message='error occured please try again')
             screen.destroy()
             





        
class create(Login_System,db):
    def __init__(self):
        global screen
        screen=Toplevel()
        screen.title('Register')
        screen.geometry('250x250')
        First=Label(screen,text='First Name:',font=('times new roman',10,'bold')).grid(row=0,column=0)
        Surname=Label(screen,text='Surname:',font=('times new roman',10,'bold')).grid(row=1,column=0)
        Add1=Label(screen,text='Address1:',font=('times new roman',10,'bold')).grid(row=2,column=0)
        Add2=Label(screen,text='Address2:',font=('times new roman',10,'bold')).grid(row=3,column=0)
        City=Label(screen,text='City:',font=('times new roman',10,'bold')).grid(row=4,column=0)
        Pc=Label(screen,text='Pin Code:',font=('times new roman',10,'bold')).grid(row=5,column=0)
        mob=Label(screen,text='Mob:',font=('times new roman',10,'bold')).grid(row=6,column=0)
        l1=Label(screen,text='Enter Username:',font=('times new roman',10,'bold')).grid(row=7,column=0)
        l2=Label(screen,text='Enter password:',font=('times new roman',10,'bold')).grid(row=8,column=0)

        global f1
        f1=Entry(screen,width=20)
        f1.grid(row=0,column=1)

        global s1
        s1=Entry(screen,width=20)
        s1.grid(row=1,column=1)
        
        global ad1
        ad1=Entry(screen,width=20)
        ad1.grid(row=2,column=1)

        global ad2
        ad2=Entry(screen,width=20)
        ad2.grid(row=3,column=1)

        global c1
        c1=Entry(screen,width=20)
        c1.grid(row=4,column=1)

        global pcode
        pcode=Entry(screen,width=20)
        pcode.grid(row=5,column=1)

        global mobno
        mobno=Entry(screen,width=20)
        mobno.grid(row=6,column=1)

        global u1
        u1=Entry(screen,width=20)
        u1.grid(row=7,column=1)

        global p1
        p1=Entry(screen,show="*",width=20)
        p1.grid(row=8,column=1)
        r=db()
        b1=Button(screen,text='Register',command = r.Register).grid(row=9,column=1)
        

    

class update(Login_System,db):
    def __init__(self):
        global screen
        screen=Toplevel()
        screen.title('Register')
        screen.geometry('250x100')
        l1=Label(screen,text='Enter Username:',font=('times new roman',10,'bold')).grid(row=0,column=0)
        l2=Label(screen,text='Reset password:',font=('times new roman',10,'bold')).grid(row=1,column=0)
        global u2
        u2=Entry(screen,width=20)
        u2.grid(row=0,column=1)
        global p2
        p2=Entry(screen,show="*",width=20)
        p2.grid(row=1,column=1)
        u=db()
        b1=Button(screen,text='Reset',command = u.reset).grid(row=2,column=1)
    
        
        
            




obj=Login_System(win)
win.mainloop()
