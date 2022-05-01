import mysql.connector
from tkinter import *
from tkinter import messagebox

#---------------------------------------------Main Window---------------------------------------------#

class MainWindow:
    def __init__(self):
        self.window=Tk()
        self.window.title("E-Commerce")
        self.window.config(padx=50,pady=50)
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/shoppingcart.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.orderbutton=Button(text="Customer Login",width=20,command=self.custlogin)
        self.orderbutton.grid(row=1,column=0,columnspan=3,padx=10,pady=5)
        
        self.companylgbutton=Button(text="Company Login",width=20,command=self.companylogin)
        self.companylgbutton.grid(row=2,column=0,columnspan=3,padx=10,pady=5)
        
        self.exitbutton=Button(text="Exit",width=20,command=self.window.destroy)
        self.exitbutton.grid(row=3,column=0,columnspan=3,padx=10,pady=5)
          
        self.window.mainloop()
        
    def custlogin(self):
        self.window.destroy()
        CustomerLogin()
    
    def companylogin(self):
        self.window.destroy()
        CompanyLogin()

#---------------------------------------------Company Login---------------------------------------------#
       
class CompanyLogin:
    def __init__(self):
        self.window=Tk()
        self.window.title("Company Login")
        self.window.config(padx=50,pady=50)
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/company.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.compnamelabel=Label(text="Company Name")
        self.compnamelabel.grid(row=1,column=0,padx=5,pady=5)
        
        self.compnameentry=Entry(width=30)
        self.compnameentry.focus()
        self.compnameentry.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        
        self.cpasslabel=Label(text="Password")
        self.cpasslabel.grid(row=2,column=0,padx=5,pady=5)
        
        self.cpassentry=Entry(width=30)
        self.cpassentry.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        
        self.loginbutton=Button(text="Login",width=10,command=self.login)
        self.loginbutton.grid(row=3,column=0,padx=5,pady=5)
        
        self.backbutton=Button(text="Back",width=10,command=self.back)
        self.backbutton.grid(row=3,column=2,padx=5,pady=5)
        
        self.window.mainloop()
        
    def login(self):#Read from Company table
        username=self.compnameentry.get()
        password=self.cpassentry.get()
        logincursor=mydb.cursor()
        logincursor.execute("SELECT * FROM company")
        
        companydata=logincursor.fetchall()
        for row in companydata:
            if row[1]==username:
                if row[2]==password:
                    #CompanyWindow(username)
                    #print("Successfill Login")
                    break
                else:
                    messagebox.showinfo(title="Oops", message="Incorrect Company Password!")
                    break
            else:
                continue
        if row[1]!=username:
            messagebox.showinfo(title="Oops", message="Incorrect Company Name!")
    
    def back(self):
        self.window.destroy()
        MainWindow()

#---------------------------------------------Company Login---------------------------------------------# 
       
class CompanyLogin:
    def __init__(self):
        self.window=Tk()
        self.window.title("Company Login")
        self.window.config(padx=50,pady=50)
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/company.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.usernamelabel=Label(text="Company Name")
        self.usernamelabel.grid(row=1,column=0,padx=5,pady=5)
        
        self.usernameentry=Entry(width=30)
        self.usernameentry.focus()
        self.usernameentry.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        
        self.passwordlabel=Label(text="Company Pass")
        self.passwordlabel.grid(row=2,column=0,padx=5,pady=5)
        
        self.passwordentry=Entry(width=30)
        self.passwordentry.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        
        self.loginbutton=Button(text="Login",width=10,command=self.login)
        self.loginbutton.grid(row=3,column=0,padx=5,pady=5)
        
        self.signupbutton=Button(text="Add Company",width=10,command=self.addcompany)
        self.signupbutton.grid(row=3,column=1,padx=5,pady=5)
        
        self.backbutton=Button(text="Back",width=10,command=self.back)
        self.backbutton.grid(row=3,column=2,padx=5,pady=5)
        
        self.window.mainloop()
        
    def back(self):
        self.window.destroy()
        MainWindow()
        
    def login(self):#Read from Company table 
        username=self.usernameentry.get()
        password=self.passwordentry.get()
        logincursor=mydb.cursor()
        logincursor.execute("SELECT * FROM company")
        
        companydata=logincursor.fetchall()
        for row in companydata:
            if row[1]==username:
                if row[2]==password:
                    self.window.destroy()
                    CompanyWindow(username,row[0])
                    break
                else:
                    messagebox.showinfo(title="Oops", message="Incorrect Password!")
                    break
            else:
                continue
        if row[1]!=username:
            messagebox.showinfo(title="Oops", message="Incorrect Company Name!")
          
    def addcompany(self):
        self.window.destroy()
        AddCompany()
        
#---------------------------------------------Company Window ---------------------------------------------#
 
class CompanyWindow:
    def __init__(self,companyname,companyid):
        self.companyname=companyname
        self.companyid=companyid
        
        self.window=Tk()
        self.window.title(f"{self.companyname}'s Dashboard")
        self.window.config(padx=50,pady=50)
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/company.window.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.viewitemsbutton=Button(text="View Items",width=10,command=self.viewitems)
        self.viewitemsbutton.grid(row=1,column=0,columnspan=3,padx=5,pady=5)
        
        self.additemsbutton=Button(text="Add Items",width=10,command=self.additems)
        self.additemsbutton.grid(row=2,column=0,columnspan=3,padx=5,pady=5)
        
        self.logoutbutton=Button(text="Logout",width=10,command=self.logout)
        self.logoutbutton.grid(row=3,column=0,columnspan=3,padx=5,pady=5)
        
        self.window.mainloop()
    
    def viewitems(self):
        self.window.destroy()
        CompanyViewItems(self.companyname,self.companyid)
    
    def additems(self):
        self.window.destroy()
        CompanyAddItems(self.companyname,self.companyid)
        
    def logout(self):
        self.window.destroy()
        CompanyLogin()
        
#---------------------------------------------Company Add Items ---------------------------------------------#
 
class CompanyAddItems:
    def __init__(self,cname,cid):
        self.cname=cname
        self.cid=cid
        self.itemid=0
        
        self.window=Tk()
        self.window.title(f"{self.cname}'s Add Items")
        self.window.config(padx=50,pady=50)
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/company.additem.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.itemnamelabel=Label(text="Item Name")
        self.itemnamelabel.grid(row=1,column=0,padx=5,pady=5)
        
        self.itemnameentry=Entry(width=30)
        self.itemnameentry.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        
        self.itempricelabel=Label(text="Item Price")
        self.itempricelabel.grid(row=2,column=0,padx=5,pady=5)
        
        self.itempriceentry=Entry(width=30)
        self.itempriceentry.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        
        self.additemsbutton=Button(text="Add Items",width=10,command=self.additems)
        self.additemsbutton.grid(row=3,column=0,padx=5,pady=5)
        
        self.backbutton=Button(text="Back",width=10,command=self.back)
        self.backbutton.grid(row=3,column=2,padx=5,pady=5)
        
        self.window.mainloop()
    
    def findlastids(self):
        findlast=mydb.cursor()
        findlast.execute("SELECT MAX(itid) FROM items")
        itid=findlast.fetchone()
        self.itemid=int(itid[0])+1
        
    def additems(self):
        self.findlastids()
        itemname=self.itemnameentry.get()
        itemprice=self.itempriceentry.get()
        additem=mydb.cursor()
        additem.execute("SELECT it_name FROM items WHERE companyid=%s",(self.cid,))
        products=additem.fetchall()
        flag=1
        for x in products:
            if itemname==x[0]:
                messagebox.showinfo(title="Oops", message="Item Already Exists!")
                flag=0
        if flag!=0:
            try:
                additem.execute("INSERT INTO items VALUES(%s,%s,%s,%s)",(self.itemid,float(itemprice),self.cid,itemname,))
                mydb.commit()
                messagebox.showinfo(title="Success", message="Item Added Successfully!")
            except:
                messagebox.showinfo(title="Oops", message="Item not added!")
                mydb.rollback()
               
    def back(self):
        self.window.destroy()
        CompanyWindow(self.cname,self.cid)      

#---------------------------------------------Company View Items ---------------------------------------------#

class CompanyViewItems():
    def __init__(self,cname,cid):
        self.window=Tk()
        self.window.title(f"{cname}'s Products")
        self.window.config(padx=50,pady=50)
        
        self.username=cname
        self.cid=cid
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/company.viewitems.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.checkitemsbutton=Button(text="Check Items",command=self.viewitems)
        self.checkitemsbutton.grid(row=1,column=0)
        
        self.backbutton=Button(text="Back",command=self.back)
        self.backbutton.grid(row=1,column=2)
        
        self.itemslistbox=Listbox(width=50,height=10)
        self.itemslistbox.grid(row=2,column=0,columnspan=3,rowspan=4)
              
        self.window.mainloop()
        
    def viewitems(self):
        checkcursor=mydb.cursor()
        checkcursor.execute("SELECT * FROM items WHERE companyid=(%s)",(self.cid,))
        itemslist=checkcursor.fetchall()
        items=[]
        i=0
        self.itemslistbox.delete(0,END)
        if itemslist!=[]:
            for x in itemslist:
                i=i+1
                self.itemslistbox.insert(i,str("Item No: "+str(x[0])+" Item Name: "+str(x[3])+ " Price: "+str(x[1])))
        else:
            self.itemslistbox.insert(0,"No Items Found!")
            
    def back(self):
        self.window.destroy()
        CompanyWindow(self.username,self.cid)
        
#---------------------------------------------Add Company---------------------------------------------#

class AddCompany:
    def __init__(self):
        self.window=Tk()
        self.window.title("Add Company")
        self.window.config(padx=50,pady=50)
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/newcompany.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.companynamelabel=Label(text="Company Name")
        self.companynamelabel.grid(row=1,column=0,padx=5,pady=5)
        
        self.companynameentry=Entry(width=30)
        self.companynameentry.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        
        self.cpasslabel=Label(text="Password")
        self.cpasslabel.grid(row=2,column=0,padx=5,pady=5)
        
        self.cpassentry=Entry(width=30)
        self.cpassentry.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        
        self.addbutton=Button(text="Add",width=10,command=self.addcompany)
        self.addbutton.grid(row=3,column=0,padx=5,pady=5)
        
        self.back=Button(text="Back",width=10,command=self.back)
        self.back.grid(row=3,column=2,padx=5,pady=5)
        
        self.window.mainloop()
        
    def addcompany(self):#insert into company
        name=self.companynameentry.get()
        password=self.cpassentry.get()
        
        signupcursor=mydb.cursor()
        signupcursor.execute("SELECT * FROM company")
        
        companydata=signupcursor.fetchall()
        f=0
        for row in companydata:
            if row[1]==name:
                messagebox.showinfo(title="Oops", message="Company already present!")
                f=1
            lid=row[0]
        lid=lid+1       
        if f==0:
            if name!="" and password!="":        
                try:
                    signupcursor.execute("INSERT INTO company VALUES(%s,%s,%s)",(lid,name,password))
                    mydb.commit()
                    self.back()
                except:
                    mydb.rollback()
            else:
                messagebox.showinfo(title="Oops", message="Please fill all the fields!")
        
    def back(self):#Back to login page
        self.window.destroy()
        CompanyLogin()       
        
#---------------------------------------------Customer Login---------------------------------------------#
        
class CustomerLogin:
    def __init__(self):
        self.window=Tk()
        self.window.title("Customer Login")
        self.window.config(padx=50,pady=50)
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/customer.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.usernamelabel=Label(text="Username")
        self.usernamelabel.grid(row=1,column=0,padx=5,pady=5)
        
        self.usernameentry=Entry(width=30)
        self.usernameentry.focus()
        self.usernameentry.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        
        self.passwordlabel=Label(text="Password")
        self.passwordlabel.grid(row=2,column=0,padx=5,pady=5)
        
        self.passwordentry=Entry(width=30)
        self.passwordentry.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        
        self.loginbutton=Button(text="Login",width=10,command=self.login)
        self.loginbutton.grid(row=3,column=0,padx=5,pady=5)
        
        self.signupbutton=Button(text="Sign Up",width=10,command=self.signup)
        self.signupbutton.grid(row=3,column=1,padx=5,pady=5)
        
        self.backbutton=Button(text="Back",width=10,command=self.back)
        self.backbutton.grid(row=3,column=2,padx=5,pady=5)
        
        self.window.mainloop()
        
    def back(self):
        self.window.destroy()
        MainWindow()
        
    def login(self):#Read from Customer table 
        username=self.usernameentry.get()
        password=self.passwordentry.get()
        logincursor=mydb.cursor()
        logincursor.execute("SELECT * FROM customer")
        
        customerdata=logincursor.fetchall()
        for row in customerdata:
            if row[1]==username:
                if row[6]==password:
                    self.window.destroy()
                    CustomerWindow(username,row[0])
                    break
                else:
                    messagebox.showinfo(title="Oops", message="Incorrect Password!")
                    break
            else:
                continue
        if row[1]!=username:
            messagebox.showinfo(title="Oops", message="Incorrect Username!")
          
    def signup(self):
        self.window.destroy()
        SignUp()

#---------------------------------------------Customer Window---------------------------------------------#
    
class CustomerWindow:
    def __init__(self,username,cid):      
        self.window=Tk()
        self.window.title(f"{username}'s Window")
        self.window.config(padx=50,pady=50)
        
        self.username=username
        self.cid=cid
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/customerdetails.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.checkorderbutton=Button(text="Check Your Order History",width=30,command=self.checkhistory)
        self.checkorderbutton.grid(row=1,column=0,columnspan=3,pady=10)
        
        self.ordernewbutton=Button(text="Order New Product",width=30,command=self.order)
        self.ordernewbutton.grid(row=2,column=0,columnspan=3,pady=10)
        
        self.logout=Button(text="Logout",width=30,command=self.logout)
        self.logout.grid(row=3,column=0,columnspan=3,pady=10)
        
        self.window.mainloop()
        
    def checkhistory(self):
        self.window.destroy()
        OrderHistory(self.username,self.cid)
        
    def order(self):
        self.window.destroy()
        OrderItems(self.username,self.cid)
        
    def logout(self):
        self.window.destroy()
        CustomerLogin() 

#---------------------------------------------Order Items---------------------------------------------#

class OrderItems():
    def __init__(self,username,cid):
        self.username=username
        self.cid=cid
        self.itemsarray=[]
        self.displaybasket=[]
        self.products=[]
        self.amount=0
        self.orderid=0
        self.itemcount=0
        self.findlastids()
        
        self.window=Tk()
        self.window.title("Order Items")
        self.window.config(padx=50,pady=50)
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/createorder.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=4)
        
        self.compname=Label(text="Company Name")
        self.compname.grid(row=1,column=0,padx=5,pady=5)
        
        self.compentry=Entry(width=30)
        self.compentry.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        
        self.compcheck=Button(text="Check Products",command=self.checkproducts)
        self.compcheck.grid(row=1,column=3,padx=5,pady=5)
        
        self.productslabel=Label(text="Products Present")
        self.productslabel.grid(row=2,column=0,padx=5,pady=5)
        
        self.comproducts=Listbox(height=5)
        self.comproducts.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        
        self.itemname=Label(text="Item Name")
        self.itemname.grid(row=3,column=0,padx=5,pady=5)
        
        self.itementry=Entry(width=30)
        self.itementry.grid(row=3,column=1,columnspan=2,padx=5,pady=5)
        
        self.quantitylabel=Label(text="Quantity")
        self.quantitylabel.grid(row=4,column=0,padx=5,pady=5)
        
        self.quantityentry=Entry(width=10)
        self.quantityentry.grid(row=4,column=1,padx=5,pady=5)
        
        self.totalamountlabel=Label(text="Order Amount:")
        self.totalamountlabel.grid(row=4,column=2,padx=5,pady=5)
        
        self.totalamount=Label(text="0",width=12,borderwidth=2,anchor=W,relief=SUNKEN)
        self.totalamount.grid(row=4,column=3,padx=5,pady=5)
             
        self.basketlistbox=Listbox(width=50,height=5)
        self.basketlistbox.grid(row=5,column=0,columnspan=4,padx=5,pady=5)
      
        self.itemadd=Button(text="Add Item",width=20,command=self.additem)
        self.itemadd.grid(row=6,column=0,padx=5,pady=5)
        
        self.order=Button(text="Order",width=20,command=self.orderbasket)
        self.order.grid(row=6,column=1,columnspan=2,padx=5,pady=5)
        
        self.backbutton=Button(text="Back",width=20,command=self.back)
        self.backbutton.grid(row=6,column=3,padx=5,pady=5)        
        
        self.window.mainloop()
    
    def findlastids(self):
        findlast=mydb.cursor()
        findlast.execute("SELECT MAX(o_no) FROM orders")
        orno=findlast.fetchone()
        self.orderid=int(orno[0])+1
             
    def checkproducts(self):
        company=self.compentry.get()
        checkcursor=mydb.cursor()
        checkcursor.execute("SELECT * FROM items WHERE companyid=(SELECT compid FROM company WHERE compname =%s)",(company,))
        self.products=checkcursor.fetchall()
        p=[]
        if self.products!=[]:
            for x in self.products:
                p.append(x[3])
                
            self.comproducts.delete(0,END)
            if p!=[]:
                self.comproducts.insert(END,*p)
            else:
                self.comproducts.insert(END,"No Products")
        else:
            self.comproducts.delete(0,END)
            messagebox.showinfo(title="Oops",message="Invalid Company Name")
            
    def additem(self):
        itemname=self.itementry.get()
        quantity=self.quantityentry.get()
        addcursor=mydb.cursor()
        addcursor.execute("SELECT * FROM items WHERE it_name=%s",(itemname,))
        item=addcursor.fetchone()
        if itemname!="":
                if quantity!="0":
                    if item!=None:
                        itid=item[0]
                        self.itemsarray.append([int(self.orderid),int(itid),int(quantity)])
                        self.displaybasket.append([itemname,quantity])
                        self.basketlistbox.insert(self.itemcount,str("Item Name: "+itemname+"\n Quantity: "+quantity))
                        self.itemcount=self.itemcount+1
                        self.amount=self.amount+int(quantity)*int(item[1])
                        self.totalamount.config(text=str(self.amount))
                    else:
                        messagebox.showinfo(title="Oops",message="Item not found!")
                else:
                    messagebox.showinfo(title="Oops",message="Please enter a valid quantity!")
        else:
            messagebox.showinfo(title="Oops", message="Itemname cannot be empty")
            
    def orderbasket(self):
        orderbasket=mydb.cursor()
        if self.itemsarray!=[]:
            try:
                orderbasket.execute("INSERT INTO orders VALUES(%s,%s,%s)",(int(self.orderid),int(self.amount),int(self.cid),))
                for x in self.itemsarray:
                    orderbasket.execute("INSERT INTO basket VALUES(%s,%s,%s)",(int(x[0]),int(x[1]),int(x[2]),))
                mydb.commit()
                messagebox.showinfo(title="Success",message="Order placed successfully!")
            except:
                mydb.rollback()
                print("Order not placed!")
        else:
            messagebox.showinfo(title="Oops", message="Empty Basket Items not added")
    
    def back(self):
        self.window.destroy()
        CustomerWindow(self.username,self.cid)
                            
#---------------------------------------------Order History---------------------------------------------#
   
class OrderHistory:
    def __init__(self,username,cid):        
        self.window=Tk()
        self.window.title("Order History")
        self.window.config(padx=50,pady=50)
        
        self.username=username
        self.cid=cid
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/previousorders.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.checkrecordsbutton=Button(text="Check Records",command=self.checkrecords)
        self.checkrecordsbutton.grid(row=1,column=0)
        
        self.backbutton=Button(text="Back",command=self.back)
        self.backbutton.grid(row=1,column=1)
        
        self.recordslistbox=Listbox(width=35)
        self.recordslistbox.grid(row=2,column=0,columnspan=3,rowspan=4)
              
        self.window.mainloop()
    
    def checkrecords(self):
        checkcursor=mydb.cursor()
        checkcursor.execute("SELECT * FROM orders WHERE cuno=(%s)",(self.cid,))
        orderlist=checkcursor.fetchall()
        i=0
        self.recordslistbox.delete(0,END)
        if orderlist!=[]:
            for x in orderlist:
                self.recordslistbox.insert(i,str("Order No: "+str(x[0])+" Amount: "+str(x[1])))
                i=i+1
        else:
            self.recordslistbox.insert(0,"No Records Found!")
        
    def back(self):
        self.window.destroy()
        CustomerWindow(self.username,self.cid)       

#---------------------------------------------Sign Up---------------------------------------------#
        
class SignUp:#Customer Sign Up
    def __init__(self):
        self.window=Tk()
        self.window.title("Customer Signup")
        self.window.config(padx=50,pady=50)
        
        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="Logos/signup.logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        self.namelabel=Label(text="Customer Name")
        self.namelabel.grid(row=1,column=0,padx=5,pady=5)
        
        self.nameentry=Entry(width=30)
        self.nameentry.grid(row=1,column=1,columnspan=2)
        
        self.addresslabel=Label(text="Customer Address")
        self.addresslabel.grid(row=2,column=0,padx=5,pady=5)
        
        self.addressentry=Entry(width=30)
        self.addressentry.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        
        self.emaillabel=Label(text="Customer Email")
        self.emaillabel.grid(row=3,column=0,padx=5,pady=5)
        
        self.emailentry=Entry(width=30)
        self.emailentry.grid(row=3,column=1,columnspan=2,padx=5,pady=5)
        
        self.cardnumberlabel=Label(text="Card Number")
        self.cardnumberlabel.grid(row=4,column=0,padx=5,pady=5)
        
        self.cardnumberentry=Entry(width=30)
        self.cardnumberentry.grid(row=4,column=1,columnspan=2,padx=5,pady=5)
               
        self.phonenumberlabel=Label(text="Customer Phone Number")
        self.phonenumberlabel.grid(row=5,column=0,padx=5,pady=5)
        
        self.phonenumberentry=Entry(width=30)
        self.phonenumberentry.grid(row=5,column=1,columnspan=2,padx=5,pady=5)
                
        self.passwordlabel=Label(text="Password")
        self.passwordlabel.grid(row=6,column=0,padx=5,pady=5)
        
        self.passwordentry=Entry(width=30)
        self.passwordentry.grid(row=6,column=1,columnspan=2,padx=5,pady=5)
        
        self.backbutton=Button(text="Back",width=10,command=self.back)
        self.backbutton.grid(row=7,column=2,padx=5,pady=5)
        
        self.signupbutton=Button(text="Sign Up",width=10,command=self.signup)
        self.signupbutton.grid(row=7,column=1,padx=5,pady=5)
        
        self.window.mainloop()
        
    def signup(self):#insert into customer
        name=self.nameentry.get()
        address=self.addressentry.get()
        email=self.emailentry.get()
        cardnumber=self.cardnumberentry.get()
        phonenumber=self.phonenumberentry.get()
        password=self.passwordentry.get()
        
        signupcursor=mydb.cursor()
        signupcursor.execute("SELECT * FROM customer")
        
        customerdata=signupcursor.fetchall()
        f=0
        for row in customerdata:
            if row[1]==name:
                messagebox.showinfo(title="Oops", message="Customer already present!")
                f=1
            lid=row[0]
        lid=lid+1       
        if f==0:
            if name!="" and address!="" and email!="" and cardnumber!="" and phonenumber!="" and password!="":        
                try:
                    signupcursor.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s)",(lid,name,address,email,cardnumber,phonenumber,password))
                    mydb.commit()
                except:
                    mydb.rollback()
            else:
                messagebox.showinfo(title="Oops", message="Please fill all the fields!")
        
    def back(self):#Back to login page
        self.window.destroy()
        CustomerLogin()

#---------------------------------------------Database Connection---------------------------------------------#
                     
if __name__=="__main__":
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="RishiMore12",#Enter your password here
                                   database="ecommerce")#Enter your database name here
    MainWindow()#Call MainWindow function
    
#Created by Rishi More
#This code is not to be distributed in any form to any person.

    
