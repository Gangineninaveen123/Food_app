#!/usr/bin/env python
# coding: utf-8

# In[10]:


#in this cell I have executed user part
class Foodordering():
    #Every admin function called from here
    def admin_func(self):
        ad_fun=["add items","change price","change discount","add items by food_id",
                "remove items by food_id","View of list of food items","stock left"]
        print("sn", "operation")
        for i,j in enumerate(ad_fun,start=1):
            print(i,j)
        operation=input("enter sn of specific operation: ")
        if operation=="1":
            return self.additems()
        if operation=="2":
            return self.price()
        if operation=="3":
            return self.discount()
        if operation=="4":
            return self.add_by_id()
        if operation=="5":
            return self.remove_item_by_id()
        if operation=="6":
            return self.menu_is()
        if operation=="7":
            return self.stock()
    def menu_is(self):
        menu=["Tandoori Chicken (4 pieces) [INR 240]","Vegan Burger (1 Piece) [INR 320]","Truffle Cake (500gm) [INR 900]"]
        for i,j in enumerate(menu,start=1):
            print(i,j)
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()
       
    def remove_item_by_id(self):
        print("Present menu is")
        menu=["Tandoori Chicken (4 pieces) [INR 240]","Vegan Burger (1 Piece) [INR 320]","Truffle Cake (500gm) [INR 900]"]
        for i,j in enumerate(menu,start=1):
            print(i,j)
        del_id=int(input("enter food id to delete from menu"))
        del menu[del_id-1]
        print("Menu after deleting food item ")
        for i,j in enumerate(menu,start=1):
            print(i,j)  
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()
        
    def add_by_id(self): 
        menu=["Tandoori Chicken (4 pieces) [INR 240]","Vegan Burger (1 Piece) [INR 320]","Truffle Cake (500gm) [INR 900]"]
        fd_id=int(input("enter food_id to add items into: "))
        menu[fd_id]=input("changing items by fd_id ")
        for i, j in enumerate(menu,start=1):
            print(i,j)
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()    
        
            
    
    def additems(self):    
            
        item_dic={}
        items=int(input("add number of new items "))
        for i in range(items):
            item_list=[]
            
            item=input("enter item name")
            item_key=f"food_id_{i}"
            q1,q2=input("quantity1 and quantity2 ").split()
            drink_price=5
            pieces_price=10
            gms_price=45
            
            if "ml" in q1 and "ml" in q2:
                ml=q1.removesuffix("ml")
                ml=int(ml)
                ml2=q2.removesuffix("ml")
                ml2=int(ml2)
                values=f"{item} avail in:{q1} price is Rs.{(ml//100)*drink_price} and {q2} is Rs.{(ml2//100)*drink_price}"
            if "pieces" in q1 and "pieces" in q2:
                ps=q1.removesuffix("pieces")
                ps=int(ps)
                ps2=q2.removesuffix("pieces")
                ps2=int(ps2)
                values=f"{item} avail in:{q1} price is {(ps//2)*pieces_price} and {q2} is Rs.{(ps2//2)*pieces_price}"
            if "gm" in q1 and "gm" in q2:
                gm=q1.removesuffix("gm")
                gm=int(gm)
                gm2=q2.removesuffix("gm")
                gm2=int(gm2)
                values=f"{item} avail in:{q1} price is {(gm//50)*gms_price} and {q2} is Rs.{(gm2//50)*gms_price}"
            item_list.append(values)
            item_dic[item_key]=item_list
        for i in item_dic:
            st=""
            for j in item_dic[i]:
                st+=j
            print(i,st)
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()   
        
   
                    
    def admin_login(self):
        adminlogin={"rk":'@123'}
        print("Admin login - enter username")
        username=input()
        print("Enter password")
        password=input()
        
        
        if username in adminlogin.keys() and password in adminlogin.values():
            
            print("Hello admin")
            return self.admin_func()
        
        
        else:
            print("Invalid admin")
                
        
    def login_admin_user(self):
        
        print("Welcome to delicious foods ")
        who=input("Are you admin or user? ")
        if who=="admin":
            return self.admin_login()
        else:
            return self.user_login()
  
  
            
    def user_login(self):
        dic={}
        user_details=[]
        
        print("For login press y or n to register")
        login_register=input()
        
        if login_register=='y':
            print("Welcome back please enter fname ")
            fname_is=input()
            print("Enter password")
            
            pd_is=input()
            if dic[fname]==pd_is:
                print("success")
        elif login_register=='n':
            print("New user please register")
            print("Fullname")
            fname=input()
            print("Enter phone number")
            phone_num=int(input())
            print("Enter adress")
            
            adress=input()
            print("enter email")
            email=input()
            print("enter password")
            pd_is=input()
            dic[fname]=pd_is
            
            print("please login now")
            fname_is=input("enter full name")
            pd_is=input("enter password ")
            
            if fname_is in dic.keys() and pd_is in dic.values():
               
                print("You are logged in successfully, browse and please order ")
                return self.user_order()
                
            else:
                print("invalid user or give proper ")  
    def user_order(self):
        print("sn"," select")
        user=["place order","order history","update profile"]
        for i,j in enumerate(user,start=1):
            print(i,j)
        sn=int(input("enter a sn to continue: "))
        if sn==1:
            return self.place_order()
        if sn==2:
            return self.order_history()
        if sn==3:
            return self.update_profile()
    
    def order_history(self):
        print("Your last order is ")
        print('1 Burger [2pcs] [Rs.150],"\n", 2 pepsi [250ml] [Rs.40]')
      
    def update_profile(self):
        up_pro=["Name change","Password change","adress change"]
        print("sn"," type" )
        for i,j in enumerate(up_pro,start=1):
            print(i,j)
        a=int(input("enter a sn to update "))
        
        if a==1:
            up_pro[a-1]=input("Enter new name: ")
            aa=input("Do you want go to previous menu yes/no:  ")
            if aa=="yes":
                return self.update_profile()
        if a==2:
            up_pro[a-1]=input("Enter new password: ")
            aa=input("Do you want go to previous menu yes/no:  ")
            if aa=="yes":
                return self.update_profile()
        if a==3:
            up_pro[a-1]=input("Enter new adress")
            aa==input("Do you want go to previous menu yes/no:  ")
            if aa=="yes":
                return self.update_profile()
            
                
            
                
    def price(self):
        item_dic={}
        drink_price=int(input("enter drink 100ml price "))
        pieces_price=int(input("enter 2 pieces price "))
        gms_price=int(input("enter 100 gms price "))
        print("Successfully changed prices")
     
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()    
        
          
    def discount(self):
        print("Enter the dicount on every item ")
        dis=int(input("New discount is: "))
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()    
       
      
    def stock(self):
        items_sold=int(input("Enter items sold: "))
       
        print("stocks left is",100-items_sold)
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()
    def place_order(self):
        print("Here is the menu")
        menu=["Tandoori Chicken (4 pieces) [INR 240]","Vegan Burger (1 Piece) [INR 320]","Truffle Cake (500gm) [INR 900]"]
        for i,j in enumerate(menu,start=1):    
            print(i,j)
        

        print("place order")
        liss=[int(x) for x in input().split()]
        for i in liss:
            print(menu[i-1])
        order_confirm=input("Type yes to confirm order: ").lower() 
        if order_confirm=="yes":
            print("Order placed successfully")
            
            
            
c=Foodordering()
c.login_admin_user()
            


# In[11]:


#In this cell I have executed admin operations
class Foodordering():
    #Every admin function called from here
    def admin_func(self):
        ad_fun=["add items","change price","change discount","add items by food_id",
                "remove items by food_id","View of list of food items","stock left"]
        print("sn", "operation")
        for i,j in enumerate(ad_fun,start=1):
            print(i,j)
        operation=input("enter sn of specific operation: ")
        if operation=="1":
            return self.additems()
        if operation=="2":
            return self.price()
        if operation=="3":
            return self.discount()
        if operation=="4":
            return self.add_by_id()
        if operation=="5":
            return self.remove_item_by_id()
        if operation=="6":
            return self.menu_is()
        if operation=="7":
            return self.stock()
    def menu_is(self):
        menu=["Tandoori Chicken (4 pieces) [INR 240]","Vegan Burger (1 Piece) [INR 320]","Truffle Cake (500gm) [INR 900]"]
        for i,j in enumerate(menu,start=1):
            print(i,j)
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()
       
    def remove_item_by_id(self):
        print("Present menu is")
        menu=["Tandoori Chicken (4 pieces) [INR 240]","Vegan Burger (1 Piece) [INR 320]","Truffle Cake (500gm) [INR 900]"]
        for i,j in enumerate(menu,start=1):
            print(i,j)
        del_id=int(input("enter food id to delete from menu"))
        del menu[del_id-1]
        print("Menu after deleting food item ")
        for i,j in enumerate(menu,start=1):
            print(i,j)  
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()
        
    def add_by_id(self): 
        menu=["Tandoori Chicken (4 pieces) [INR 240]","Vegan Burger (1 Piece) [INR 320]","Truffle Cake (500gm) [INR 900]"]
        fd_id=int(input("enter food_id to add items into: "))
        menu[fd_id]=input("changing items by fd_id ")
        for i, j in enumerate(menu,start=1):
            print(i,j)
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()    
        
            
    
    def additems(self):    
            
        item_dic={}
        items=int(input("add number of new items "))
        for i in range(items):
            item_list=[]
            
            item=input("enter item name")
            item_key=f"food_id_{i}"
            q1,q2=input("quantity1 and quantity2 ").split()
            drink_price=5
            pieces_price=10
            gms_price=45
            
            if "ml" in q1 and "ml" in q2:
                ml=q1.removesuffix("ml")
                ml=int(ml)
                ml2=q2.removesuffix("ml")
                ml2=int(ml2)
                values=f"{item} avail in:{q1} price is Rs.{(ml//100)*drink_price} and {q2} is Rs.{(ml2//100)*drink_price}"
            if "pieces" in q1 and "pieces" in q2:
                ps=q1.removesuffix("pieces")
                ps=int(ps)
                ps2=q2.removesuffix("pieces")
                ps2=int(ps2)
                values=f"{item} avail in:{q1} price is {(ps//2)*pieces_price} and {q2} is Rs.{(ps2//2)*pieces_price}"
            if "gm" in q1 and "gm" in q2:
                gm=q1.removesuffix("gm")
                gm=int(gm)
                gm2=q2.removesuffix("gm")
                gm2=int(gm2)
                values=f"{item} avail in:{q1} price is {(gm//50)*gms_price} and {q2} is Rs.{(gm2//50)*gms_price}"
            item_list.append(values)
            item_dic[item_key]=item_list
        for i in item_dic:
            st=""
            for j in item_dic[i]:
                st+=j
            print(i,st)
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()   
        
   
                    
    def admin_login(self):
        adminlogin={"rk":'@123'}
        print("Admin login - enter username")
        username=input()
        print("Enter password")
        password=input()
        
        
        if username in adminlogin.keys() and password in adminlogin.values():
            
            print("Hello admin")
            return self.admin_func()
        
        
        else:
            print("Invalid admin")
                
        
    def login_admin_user(self):
        
        print("Welcome to delicious foods ")
        who=input("Are you admin or user? ")
        if who=="admin":
            return self.admin_login()
        else:
            return self.user_login()
  
  
            
    def user_login(self):
        dic={}
        user_details=[]
        
        print("For login press y or n to register")
        login_register=input()
        
        if login_register=='y':
            print("Welcome back please enter fname ")
            fname_is=input()
            print("Enter password")
            
            pd_is=input()
            if dic[fname]==pd_is:
                print("success")
        elif login_register=='n':
            print("New user please register")
            print("Fullname")
            fname=input()
            print("Enter phone number")
            phone_num=int(input())
            print("Enter adress")
            adress=input()
            print("enter email")
            email=input()
            print("enter password")
            pd_is=input()
            dic[fname]=pd_is
            
            print("please login now")
            fname_is=input("enter full name")
            pd_is=input("enter password ")
            
            if fname_is in dic.keys() and pd_is in dic.values():
               
                print("You are logged in successfully, browse and please order ")
                return self.user_order()
                
            else:
                print("invalid user or give proper ")  
    def user_order(self):
        print("sn"," select")
        user=["place order","order history","update profile"]
        for i,j in enumerate(user,start=1):
            print(i,j)
        sn=int(input("enter a sn to continue: "))
        if sn==1:
            return self.place_order()
        if sn==2:
            return self.order_history()
        if sn==3:
            return self.update_profile()
    
    def order_history(self):
        print("Your last order is ")
        print('1 Burger [2pcs] [Rs.150],"\n", 2 pepsi [250ml] [Rs.40]')
      
    def update_profile(self):
        up_pro=["Name change","Password change","adress change"]
        print("sn"," type" )
        for i,j in enumerate(up_pro,start=1):
            print(i,j)
        a=int(input("enter a sn to update "))
        
        if a==1:
            up_pro[a-1]=input("Enter new name: ")
            aa=input("Do you want go to previous menu yes/no:  ")
            if aa=="yes":
                return self.update_profile()
        if a==2:
            up_pro[a-1]=input("Enter new password: ")
            aa=input("Do you want go to previous menu yes/no:  ")
            if aa=="yes":
                return self.update_profile()
        if a==3:
            up_pro[a-1]=input("Enter new adress")
            aa==input("Do you want go to previous menu yes/no:  ")
            if aa=="yes":
                return self.update_profile()
            
                
            
                
    def price(self):
        item_dic={}
        drink_price=int(input("enter drink 100ml price "))
        pieces_price=int(input("enter 2 pieces price "))
        gms_price=int(input("enter 100 gms price "))
        print("Successfully changed prices")
     
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()    
        
          
    def discount(self):
        print("Enter the dicount on every item ")
        dis=int(input("New discount is: "))
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()    
       
      
    def stock(self):
        items_sold=int(input("Enter items sold: "))
       
        print("stocks left is",100-items_sold)
        press=input("do you want to go to previous menu yes or no: ").lower()
        if press=="yes":
            return self.admin_func()
    def place_order(self):
        print("Here is the menu")
        menu=["Tandoori Chicken (4 pieces) [INR 240]","Vegan Burger (1 Piece) [INR 320]","Truffle Cake (500gm) [INR 900]"]
        for i,j in enumerate(menu,start=1):    
            print(i,j)
        

        print("place order")
        liss=[int(x) for x in input().split()]
        for i in liss:
            print(menu[i-1])
        order_confirm=input("click yes to confirm order: ").lower() 
        if order_confirm=="yes":
            print("Order placed successfully")
            
            
            
c=Foodordering()
c.login_admin_user()


# In[ ]:




