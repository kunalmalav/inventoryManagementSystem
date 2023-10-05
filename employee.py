from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox    #importing library to use combobox and some other
import sqlite3

class employeeClass():     #Creating employeeclass
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()  #To highlight employee window

        #all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        self.var_address=StringVar()
        
        #search frame
        #creating search frame and placing in root
       # SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE).place(x=250,y=20,width=600,height=70)
        
        #options in search frame
        #creating combobox in search frame
        cmb_search=ttk.Combobox(self.root,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,
        font=("goudy old style",15,"bold"))
        cmb_search.place(x=260,y=50,width=180)
        cmb_search.current(0)   #current value is of index 0 ,state=readonly so that we can't type
        
        #in single row if we want to enter our data then we go for 'Entry' otherwise for 'Text'
        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=450,y=50)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=670,y=50,width=150,height=30)
        
        #title
        #creating label to show 'employee details'
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=900)

        #labels
        #content
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=650,y=150)
  
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow")
        txt_empid.place(x=150,y=150,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow")
        txt_contact.place(x=750,y=150,width=180)
        
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state="readonly",justify=CENTER,
        font=("goudy old style",15,"bold"))
        cmb_gender.place(x=450,y=150,width=180)
        cmb_gender.current(0)

        #row 2

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=650,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow")
        txt_name.place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow")
        txt_dob.place(x=450,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow")
        txt_doj.place(x=750,y=190,width=180)
        
        #row 3

        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=650,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow")
        txt_email.place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow")
        txt_pass.place(x=450,y=230,width=180)
        
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state="readonly",justify=CENTER,
        font=("goudy old style",15,"bold"))
        cmb_utype.place(x=750,y=230,width=180)
        cmb_utype.current(0)

        #row 4

        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)
        
        #using 'Text' to write more than one line
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow")
        txt_salary.place(x=600,y=270,width=180)
        
        #buttons
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=80,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=80,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=80,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=80,height=30)


        #employee details

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)   #creating frame for treeview
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        #treeview to show database in tables and column,
        self.EmployeeTable=ttk.Treeview(emp_frame,column=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        #to show headings in our tree view,case sesitive,eid can't be written as Eid
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        
        self.EmployeeTable["show"]="headings"  #to remove or hide some default headings
        
        #to reduce width of column of headings
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=90)
        self.EmployeeTable.column("email",width=90)
        self.EmployeeTable.column("gender",width=90)
        self.EmployeeTable.column("contact",width=90)
        self.EmployeeTable.column("dob",width=90)
        self.EmployeeTable.column("doj",width=90)
        self.EmployeeTable.column("pass",width=90)
        self.EmployeeTable.column("utype",width=90)
        self.EmployeeTable.column("address",width=90)
        self.EmployeeTable.column("salary",width=90)
        
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)    #buttonrelease is a type of event,when we release button after clicking then it will call fn 'get_data'

