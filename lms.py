from tkinter import*
from tkinter import ttk
from tkinter.messagebox import *
import conn
import random as rd
from datetime import date,timedelta,datetime



class Library:
    def __init__(self,user,win):
        self.win=win
        self.username=user
        self.win=Toplevel()
        self.win.title('Library Management System')
        self.win.geometry('1350x750+0+0')
   
        
        #----frame---
        MainFrame =Frame(self.win)
        MainFrame.pack()

        TitleFrame =Frame(MainFrame,width=1360,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle =Label(TitleFrame,width=39,font=('arial',40,'bold'),text='\tLIBRARY MANAGEMENT SYSTEM',padx=12)
        self.lblTitle.grid()

        ButtonFrame =Frame(MainFrame,width=1360,padx=20,bd=20,height=50,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail =Frame(MainFrame,width=1360,padx=20,bd=20,height=300,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame,width=1380,padx=20,bd=20,height=400,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft =LabelFrame(DataFrame,width=800,padx=20,bd=10,height=340,relief=RIDGE,font=('arial',12,'bold'),text='LIBRARY MEMBER INFO:',)
        DataFrameLeft.pack(side=LEFT)


        DataFrameRight =LabelFrame(DataFrame,width=550,padx=20,bd=10,height=300,relief=RIDGE,font=('arial',12,'bold'),text='BOOK DETAILS:',)
        DataFrameRight.pack(side=RIGHT)
                   
        #----widget--
        
        self.lblMemberType =Label(DataFrameLeft,font=('arial',12,'bold'),text='Member Type:',padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0)

        self.type=ttk.Combobox(DataFrameLeft,font=('arial',12,'bold'),state='readonly',width=15)
        self.type['value']=('','Student','Lecturer','Admin Staff')
        self.type.current(0)
        self.type.grid(row=0,column=1)

        self.Ref =Label(DataFrameLeft,font=('arial',12,'bold'),text='Refernce No:',padx=2,pady=2).grid(row=1,column=0)
        self.Ref_text=Entry(DataFrameLeft,width=25)
        self.Ref_text.grid(row=1,column=1)
        
        self.First =Label(DataFrameLeft,font=('arial',12,'bold'),text='Firstname:',padx=2,pady=2).grid(row=2,column=0)
        self.First_text=Entry(DataFrameLeft,width=25)
        self.First_text.grid(row=2,column=1)

        self.Surname =Label(DataFrameLeft,font=('arial',12,'bold'),text='Surname:',padx=2,pady=2).grid(row=3,column=0)
        self.Surname_text=Entry(DataFrameLeft,width=25)
        self.Surname_text.grid(row=3,column=1)

        self.Add1 =Label(DataFrameLeft,font=('arial',12,'bold'),text='Address 1:',padx=2,pady=2).grid(row=4,column=0)
        self.Add1_text=Entry(DataFrameLeft,width=25)
        self.Add1_text.grid(row=4,column=1)
        
        self.Add2 =Label(DataFrameLeft,font=('arial',12,'bold'),text='Address 2:',padx=2,pady=2).grid(row=5,column=0)
        self.Add2_text=Entry(DataFrameLeft,width=25)
        self.Add2_text.grid(row=5,column=1)

        self.city =Label(DataFrameLeft,font=('arial',12,'bold'),text='City:',padx=2,pady=2).grid(row=6,column=0)
        self.city_text=Entry(DataFrameLeft,width=25)
        self.city_text.grid(row=6,column=1)
        
        self.Post =Label(DataFrameLeft,font=('arial',12,'bold'),text='Post Code:',padx=2,pady=2).grid(row=7,column=0)
        self.Post_text=Entry(DataFrameLeft,width=25)
        self.Post_text.grid(row=7,column=1)
        
        self.Mob =Label(DataFrameLeft,font=('arial',12,'bold'),text='Mobile No:',padx=2,pady=2).grid(row=8,column=0)
        self.Mob_text=Entry(DataFrameLeft,width=25)
        self.Mob_text.grid(row=8,column=1)


        self.Update=Button(DataFrameLeft,text='Update',font=('arial',12,'bold'),command=self.update_user).grid(row=9,column=1)
        
        self.Bid =Label(DataFrameLeft,font=('arial',12,'bold'),text='Book ID:',padx=2,pady=2).grid(row=0,column=3)
        self.Bid_text=Entry(DataFrameLeft,width=25)
        self.Bid_text.grid(row=0,column=4)

        self.Bktitle =Label(DataFrameLeft,font=('arial',12,'bold'),text='Book Title:',padx=2,pady=2).grid(row=1,column=3)
        self.Bktitle_text=Entry(DataFrameLeft,width=25)
        self.Bktitle_text.grid(row=1,column=4)

        self.Author =Label(DataFrameLeft,font=('arial',12,'bold'),text='Author:',padx=2,pady=2).grid(row=2,column=3)
        self.Author_text=Entry(DataFrameLeft,width=25)
        self.Author_text.grid(row=2,column=4)


        self.Datel =Label(DataFrameLeft,font=('arial',12,'bold'),text='Date on Loan:',padx=2,pady=2).grid(row=3,column=3)
        self.Datel_text=Entry(DataFrameLeft,width=25)
        self.Datel_text.grid(row=3,column=4)

        self.DateO =Label(DataFrameLeft,font=('arial',12,'bold'),text='Ref No:',padx=2,pady=2).grid(row=4,column=3)
        self.DateO_text=Entry(DataFrameLeft,width=25)
        self.DateO_text.grid(row=4,column=4)

        self.Sp =Label(DataFrameLeft,font=('arial',12,'bold'),text='Selling Price:',padx=2,pady=2).grid(row=5,column=3)
        self.Sp_text=Entry(DataFrameLeft,width=25)
        self.Sp_text.grid(row=5,column=4)

        self.Stock =Label(DataFrameLeft,font=('arial',12,'bold'),text='Stock:',padx=2,pady=2).grid(row=6,column=3)
        self.stoct_text=Entry(DataFrameLeft,width=25)
        self.stoct_text.grid(row=6,column=4)

        self.Issue =Label(DataFrameLeft,font=('arial',12,'bold'),text='Issue Id:',padx=2,pady=2).grid(row=7,column=3)
        self.Issue_text=Entry(DataFrameLeft,width=25)
        self.Issue_text.grid(row=7,column=4)

        self.DateD =Label(DataFrameLeft,font=('arial',12,'bold'),text='Date to Return:',padx=2,pady=2).grid(row=8,column=3)
        self.DateD_text=Entry(DataFrameLeft,width=25)
        self.DateD_text.grid(row=8,column=4)


        self.Addbk=Button(DataFrameLeft,text='Add Book',font=('arial',12,'bold'),command=self.Add_book)
        self.Addbk.grid(row=9,column=4)
        if self.username=='Admin' or self.username=='admin':
            self.Addbk.config(state=NORMAL)
        else:    
             self.Addbk.config(state=DISABLED)

        scroll_y=Scrollbar(DataFrameRight,orient=VERTICAL)

        
        self.Book_Table=ttk.Treeview(DataFrameRight,columns=('Book ID','Book Title','Author'),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.Book_Table.yview)
        self.Book_Table.pack()
        self.Book_Table.heading('Book ID',text='Book Id')
        self.Book_Table.heading('Book Title',text='Book Name')
        self.Book_Table.heading('Author',text='Author')
        self.Book_Table['show']='headings'
        self.Book_Table.bind('<ButtonRelease-1>',self.get_cursor)

        
        self.Addbk=Button(DataFrameRight,text='Fetch Books',font=('arial',12,'bold'),command=self.fetch,bd=4,width=20)
        self.Addbk.pack()

        
       


        self.user()
        
        #--bootom--

        scroll=Scrollbar(FrameDetail,orient=VERTICAL)
        self.Issue_Table=ttk.Treeview(FrameDetail,height=4,columns=(1,2,3,4,5,6,7),show='headings',yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.Issue_Table.yview)
        self.Issue_Table.pack()
        self.Issue_Table.heading(1, text="Ref_no")
        self.Issue_Table.column(1, minwidth=0, width=150,stretch=NO)
        self.Issue_Table.heading(2, text="First Nmae")
        self.Issue_Table.column(2, minwidth=0, width=150,stretch=NO)
        self.Issue_Table.heading(3, text="Surname")
        self.Issue_Table.column(3, minwidth=0, width=150,stretch=NO)
        self.Issue_Table.heading(4,text='Book Name')
        self.Issue_Table.heading(5,text='Date Issue')
        self.Issue_Table.heading(6,text='Date Return')
        self.Issue_Table.heading(7,text='Status')
        self.Issue_Table.column(7, minwidth=0, width=150,stretch=NO)
        self.fetch_detail()
        self.Issue_Table.bind('<ButtonRelease-1>',self.info)



        
        #--button--
        self.btnDisplayData=Button(ButtonFrame,text='Issue Book',font=('arial',12,'bold'),bd=4,width=22,command=self.issue).grid(row=0,column=0)
        self.ReturnBk=Button(ButtonFrame,text='Return',font=('arial',12,'bold'),bd=4,width=22,command=self.return_bk).grid(row=0,column=1)
        self.Display=Button(ButtonFrame,text='Dispaly All',font=('arial',12,'bold'),bd=4,width=22,command=self.fetch_detail).grid(row=0,column=2)

        self.Clrbk=Button(ButtonFrame,text='Clear',font=('arial',12,'bold'),command=self.clear,bd=4,width=22).grid(row=0,column=3)
        self.Exitybk=Button(ButtonFrame,text='LogOut',font=('arial',12,'bold'),command=self.Exit,bd=4,width=22).grid(row=0,column=4)

    def fetch(self):
        self.db=conn.getconn()
        self.mycursor=self.db.cursor()
        self.mycursor.execute("Select *  From book")
        row=self.mycursor.fetchall()
        if len(row)!=0:
            self.Book_Table.delete(*self.Book_Table.get_children())
            for x in row:
                self.Book_Table.insert('',END,values=x)
            self.db.commit()               
    
    def get_cursor(self,ev):
        cur_row=self.Book_Table.focus()
        contents=self.Book_Table.item(cur_row)
        x=contents['values']
        
        self.Bid_text.delete(0,END)
        self.Bid_text.insert(0,x[0])

        self.Bktitle_text.delete(0,END)
        self.Bktitle_text.insert(0,x[1])

        self.Author_text.delete(0,END)
        self.Author_text.insert(0,x[2])

        self.Datel_text.delete(0,END)
        self.Datel_text.insert(0,x[3])

        self.Sp_text.delete(0,END)
        self.Sp_text.insert(0,x[4])

        self.stoct_text.delete(0,END)
        self.stoct_text.insert(0,x[5])

        self.fetch()
        #self.Bid_text.config(state=DISABLED)
        #self.Bktitle_text.config(state=DISABLED)
        #self.Author_text.config(state=DISABLED)
        #self.Datel_text.config(state=DISABLED)
        #self.Sp_text.config(state=DISABLED)
        #self.stoct_text.config(state=DISABLED)

       
        
    def clear(self):
        #self.Bid_text.config(state=NORMAL)
        #self.Bktitle_text.config(state=NORMAL)
        #self.Author_text.config(state=NORMAL)
        #self.Datel_text.config(state=NORMAL)
        #self.Sp_text.config(state=NORMAL)
        #self.stoct_text.config(state=NORMAL)
        
        self.Bid_text.delete(0,END)
        self.Bktitle_text.delete(0,END)
        self.Author_text.delete(0,END)
        self.Datel_text.delete(0,END)
        self.Sp_text.delete(0,END)
        self.stoct_text.delete(0,END)

    def user(self):
        self.db=conn.getconn()
        self.mycursor=self.db.cursor()
        self.mycursor.execute(f"Select * From login where username='{self.username}'")
        result=self.mycursor.fetchone()
        self.Ref_text.insert(0,result[0])
        self.First_text.insert(0,result[1])
        self.Surname_text.insert(0,result[2])
        self.Add1_text.insert(0,result[3])
        self.Add2_text.insert(0,result[4])
        self.city_text.insert(0,result[5])
        self.Post_text.insert(0,result[6])
        self.Mob_text.insert(0,result[7])

        self.DateO_text.insert(0,result[0])

        self.DateO_text.config(state=DISABLED)
        self.Ref_text.config(state=DISABLED)

    def update_user(self):
        self.mycursor.execute(f"Update login Set First_name='{self.First_text.get()}',surname='{self.Surname_text.get()}',add1='{self.Add1_text.get()}',add2='{self.Add2_text.get()}',city='{self.city_text.get()}',post_code='{self.Post_text.get()}',mob_no='{self.Mob_text.get()}' WHERE Username='{self.username}'")
        if self.mycursor.rowcount > 0:
            showinfo(title = "Update", message = "Sucessfully Updated")
            self.db.commit()
    
        else:
             showinfo(title='Error',message='error occured please try again')
    
        

    def Exit(self):
        self.win.destroy()        

        
    def Add_book(self):
        self.mycursor.execute(f"Insert into book values({self.Bid_text.get()},'{self.Bktitle_text.get()}','{self.Author_text.get()}',{self.Datel_text.get()},{self.Sp_text.get()},{self.stoct_text.get()})")
        if self.mycursor.rowcount > 0:
            showinfo(title = "Saved", message = "Record saved sucessfully")
            self.Bid_text.delete(0,END)
            self.Bktitle_text.delete(0,END)
            self.Author_text.delete(0,END)
            self.Datel_text.delete(0,END)
            self.Sp_text.delete(0,END)
            self.stoct_text.delete(0,END)
            self.db.commit()
            
        else:
            showinfo(title='Error',message='error occured please try again')
   
    def issue(self):
        if self.Bktitle_text=='0':
            showinfo(title = "Stock", message = "Out of Stock")
            
        else:
            self.Today=date.today()
            null='Null'
            self.mycursor.execute(f"Update book Set Stock=Stock-1 where Book_Title='{self.Bktitle_text.get()}'")
            self.db.commit()
            self.mycursor.execute(f"Insert into issue values({self.Ref_text.get()},'{self.First_text.get()}','{self.Surname_text.get()}','{self.Bktitle_text.get()}','{self.Today}','{null}','{null}',{rd.randint(100,99999)})")
            if self.mycursor.rowcount > 0:
                showinfo(title = "Issued", message = "Book Issued")
                self.db.commit()
                
            else:
                showinfo(title='Error',message='error occured please try again')

    def fetch_detail(self):
        if self.username=='Admin' or self.username=='admin':
            self.mycursor.execute("Select * From issue")
        else:    
            self.mycursor.execute(f"Select * From issue where First_name='{self.First_text.get()}'")
        detail=self.mycursor.fetchall()
        if len(detail)!=0:
            self.Issue_Table.delete(*self.Issue_Table.get_children())
            for x in detail:
                self.Issue_Table.insert('',END,values=x)
            self.db.commit() 
        
    def info(self,ev):
        cur=self.Issue_Table.focus()
        content=self.Issue_Table.item(cur)
        x=content['values']
        self.Issue_text.delete(0,END)
        self.Issue_text.insert(0,x[7])
        res = (datetime.strptime(x[4], '%Y-%m-%d') + timedelta(days=7)).strftime('%Y-%m-%d')
        self.DateD_text.delete(0,END)
        self.DateD_text.insert(0,res)
        self.Bktitle_text.delete(0,END)
        self.Bktitle_text.insert(0,x[3])
        

    def return_bk(self):
        self.Rday=date.today()
        ret='Returned'
        self.mycursor.execute(f"Update book Set Stock=Stock+1 where Book_Title='{self.Bktitle_text.get()}'")
        self.db.commit()
        self.mycursor.execute(f"Update issue Set Date_Return='{self.Rday}',Status='{ret}' WHERE issue_id='{self.Issue_text.get()}'")
        if self.mycursor.rowcount > 0:
            showinfo(title = "Return", message = "Book has been returned")
            self.db.commit()
    
        else:
             showinfo(title='Error',message='Error in Returning Book')

            

                 

        
 
