from tkinter import*
from PIL import Image,ImageTk
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        
        
        #<<<<<<<<<<TITLE>>>>>>>>>>>>                    
        self.icon_title = PhotoImage(file="images/logo1.png")                  
        title = Label(self.root,text="Inventory Management System",image = self.icon_title,compound = LEFT,font=("times new roman",40,"bold"),bg="#737373",fg="white",anchor='w',padx=10).place(x=0,y=0,relwidth=1,height=70)
        
        #<<<<<<<<<<BUTTON>>>>>>>>>>>>
        
        btm_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#F08080",cursor="hand2").place(x=1100,y=18,height=35,width=150)

        #<<<<<<<<<<CLOCK>>>>>>>>>>>>                    
        self.clock = Label(self.root,text="Welcome!\t\t Date: DD-MM-YYYY Time: HH-MM-SS",font=("times new roman",15,""),bg="#4d636d",fg="white")
        self.clock.place(x=0,y=70,relwidth=1,height=30)
        
        #<<<<<<<<<<Left Menu>>>>>>>>>>>>    
        self.menuLogo=Image.open()
        self.menuLogo=self.menuLogo.resize((200,200),Image.ANTIALIAS)
        self.menuLogo=ImageTK.PhotoImage(self.menuLogo)
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE)
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menuLogo=Label(LeftMenu,image=self.menuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        
    
root = Tk()
obj=IMS(root)
root.mainloop()




