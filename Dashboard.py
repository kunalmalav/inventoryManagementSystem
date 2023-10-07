# Standard Library Imports
import os
import sqlite3
import time
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Custom Module Imports
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesclass

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="black")
        
        
        #<<<<<<<<<<TITLE>>>>>>>>>>>>                    
        self.icon_title = PhotoImage(file="images/logo1.png")                  
        title = Label(self.root,text="Inventory Management System",image = self.icon_title,compound = LEFT,font=("times new roman",40,"bold"),bg="#737373",fg="white",anchor='w',padx=10).place(x=0,y=0,relwidth=1,height=70)
        
        #<<<<<<<<<<BUTTON>>>>>>>>>>>>
        
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#F08080",cursor="hand2").place(x=1100,y=18,height=35,width=150)

        #<<<<<<<<<<CLOCK>>>>>>>>>>>>                    
        self.clock = Label(self.root,text="Welcome!\t\t Date: DD-MM-YYYY Time: HH-MM-SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.clock.place(x=0,y=70,relwidth=1,height=30)
        
        #<<<<<<<<<<Left Menu>>>>>>>>>>>>    
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE)
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        self.icon_side = PhotoImage(file="images/side.png")                  
        lbl_menu = Label(LeftMenu,text="Menu",font=("times new roman",20,"bold"),bg="#009688").pack(side=TOP,fill=X)
        
        btn_employee = Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category = Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product = Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       
        #<<<<<<<<<<CONTENT>>>>>>>>>>>> 
        self.employee=Label(self.root,text="Total Employee\n[0]",bg="#33bbf9",bd=5,relief=RIDGE,
        fg="white",font=("times new roman",15,"bold")).place(x=250,y=120,height=150,width=300)

        self.supplier=Label(self.root,text="Total Supplier\n[0]",bg="#ff5722",bd=5,relief=RIDGE,
        fg="white",font=("times new roman",15,"bold")).place(x=600,y=120,height=150,width=300)

        self.category=Label(self.root,text="Total Category\n[0]",bg="#009688",bd=5,relief=RIDGE,
        fg="white",font=("times new roman",15,"bold")).place(x=950,y=120,height=150,width=300)

        self.product=Label(self.root,text="Total Products\n[0]",bg="#607d8b",bd=5,relief=RIDGE,
        fg="white",font=("times new roman",15,"bold")).place(x=250,y=300,height=150,width=300)

        self.sales=Label(self.root,text="Total Sales\n[0]",bg="#ffc107",bd=5,relief=RIDGE,
        fg="white",font=("times new roman",15,"bold")).place(x=600,y=300,height=150,width=300)

        #<<<<<<<<<<FOOTER>>>>>>>>>>>>                    
        lbl_footer= Label(self.root,text="IMS - Inventory Management System | Developed by Kunal Malav",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win) 

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesclass(self.new_win)  

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try: 
            cur.execute("select *from product")  
            product=cur.fetchall()
            self.lbl_product.config(text=f'total products \n[ {str(len(product))} ]')

            cur.execute("select *from supplier")  
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'total suppliers \n[ {str(len(supplier))} ]')

            cur.execute("select *from category ")  
            category=cur.fetchall()
            self.lbl_category.config(text=f'total category\n[ {str(len(category))} ]')

            cur.execute("select * from employee ")  
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'total employees\n[ {str(len(employee))} ]')     
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total sales[{str(bill)}]')
            
            time_=time.strftime("DD-MM-YYYY")
            date_=time.strftime("HH-MM-SS")
            self.lbl_clock.config(text=f"Welcome!\t\t Date: {str(date_)}\t\t Time:{str(time_)}")
            self.lbl_clock.after(200,self.update_content)
            

            pass
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.root)  

    def logout(self):
        self.root.destroy()
        os.system("python login.py")   

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()







 