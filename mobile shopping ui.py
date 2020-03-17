import os, pickle, getpass, random

#class to store mobile details
class Mobile(object):
    def __init__(self):
        self.model_no=""
        self.name=""
        self.colour=""
        self.os=""
        self.ram=""
        self.weight=""
        self.dimen=tuple()
        self.front_cam=""
        self.back_cam=""
        self.qty=""
        self.price=""

    def create_rec(self):
        print ("ENTER THE MOBILE DETAILS-->")
        self.name=raw_input("NAME :")
        self.colour=raw_input("COLOUR :")
        self.os=raw_input("OS :")
        self.ram=raw_input("RAM :")
        self.weight=raw_input("WEIGHT :")
        print ("DIMENSIONS :")
        length=raw_input("ENTER THE LENGTH :")
        width=raw_input("ENTER THE WIDTH :")
        thick=raw_input("ENTER THE THICKNESS :")
        self.dimen=(length,width,thick)
        self.front_cam=raw_input("FRONT CAMERA :")
        self.back_cam=raw_input("BACK CAMERA :")
        self.qty=raw_input("QUANTITY :")
        self.price=raw_input("PRICE :")

    def display_rec(self):
        print ("THE MOBILE DETAILS->")
        print ("MODEL NUMBER : ",self.model_no)
        print ("NAME :",self.name)
        print ("COLOUR :",self.colour)
        print ("OS :",self.os)
        print ("RAM :",self.ram)
        print ("WEIGHT :",self.weight)
        print ("DIMENSIONS :",self.dimen[0], "X", self.dimen[1], "X", self.dimen[2])
        print ("FRONT CAMERA :",self.front_cam)
        print ("BACK CAMERA :",self.back_cam)
        print ("QUANTITY :",self.qty)
        print ("PRICE :",self.price)

#During modification of mobile record, if the user  does not enter any value #then the previous value only has to be taken
    def check_rec(self,rec2):
        if self.name=="":
            self.name=rec2.name
        if self.colour=="":
            self.colour=rec2.colour
        if self.os=="":
            self.os=rec2.os
        if self.ram=="":
            self.ram=rec2.ram
        if self.weight=="":
            self.weight=rec2.weight
        if self.dimen[0]=="":
            l=rec2.dimen[0]
        else:
            l=self.dimen[0]
        if self.dimen[1]=="":
            w=rec2.dimen[1]
        else:
            w=self.dimen[1]
        if self.dimen[2]=="":
            t=rec2.dimen[2]
        else:
            t=self.dimen[2]
        self.dimen=(l,w,t)
        if self.front_cam=="":
            self.front_cam=rec2.front_cam
        if self.back_cam=="":
            self.back_cam=rec2.back_cam
        if self.qty=="":
            self.qty=rec2.qty
        if self.price=="":
            self.price=rec2.price

#class for each customer
class Customer(object):
    def __init__(self):
        self.log_name=""
        self.pswd=""
        self.cust_id=0

    def enter_rec(self):
        self.pswd=getpass.getpass("ENTER THE PASSWORD: ")
        pswd=getpass.getpass("ENTER THE PASSWORD AGAIN: ")
        if pswd!=self.pswd:
            print ("THE TWO PASSWORDS DO NOT MATCH")
            ch=raw_input("Press any key to continue")
            return -1
        self.cust_id=random.randint(1,1000)
        return self.cust_id
           
#class for each item bought                      
class Order(object):
    def __init__(self):
        self.cust_id=0
        self.model_no=""
        self.qty=0
        self.price=0.0
        self.total=0.0

    def display_rec(self):
        print ("  ",self.model_no,"\t\t\t",self.qty,"\t\t  ",self.price)
        
       
def main_menu():
    while (True):
        os.system("cls")
        print ("******************************************************")
        print ("              WELCOME TO THE MOBILE SHOP     ")             
        print ("******************************************************")
        print("             ")
        print ("                     MAIN MENU")
        print("    ")
        print ("1.     ADMIN MODE")
        print(" ")
        print ("2.     USER MODE")
        print(" ")
        print ("3.     EXIT")
        print(" ")
        choice=input("ENTER THE CHOICE (1/2/3) : ")
        if choice==1:
            admin_mode()
        elif choice==2:
            cust_id=login()
            if cust_id!=-1:    
                user_mode(cust_id)
        else :
            return

def admin_mode():
    while (True):
        os.system("cls")
        print ("******************************************************")
        print ("                   ADMIN MODE                         ")                         
        print ("******************************************************")
        print("                                                        ")
        print ("                      MENU")
        print("                                      ")
        print ("1.      ADD MOBILE DETAILS")
        print ("2.      MODIFY MOBILE DETAILS")
        print ("3.      DELETE MOBILE DETAILS")
        print ("4.      DISPLAY MOBILE DETAILS")
        print ("5.      RETURN TO THE MAIN MENU")
        print ("6.      EXIT")
        print("                               ")
        choice=input("ENTER THE CHOICE (1-6) : ")
        if choice==1:
            add_mobile()
        elif choice==2:
            modify_mobile()
        elif choice==3:
            delete_mobile()
        elif choice==4:
            display_mobile()
        elif choice==5:
            return
        else :
            exit()

#method to check the credentials of an existing customer or to create a new
#customer
def login():
    os.system("cls")
    cust=Customer()
    file=open("customer.dat","rb+")
    ch=raw_input("ARE YOU AN EXISTING OR A NEW USER(E/N) :")
    if ch=='N' or ch=='n':
        login=raw_input("ENTER THE LOGIN NAME :")
        try:
            while True:
                cust=pickle.load(file)
                if login==cust.log_name :
                    print ("THIS LOGIN NAME ALREADY EXISTS")
                    ch=raw_input("Press any key to continue")
                    return -1
        except EOFError:
            cust.log_name=login
            cust_id=cust.enter_rec()
            if cust_id==-1:
                return -1
            pickle.dump(cust,file)
            return cust_id
        except IOError:
            print ("Unable to open File")
            exit
        finally:
            file.close()
    else:
        file=open("customer.dat","rb")
        name=raw_input("Enter your login name :")
        try:
            while True:
                rec=pickle.load(file)
                if rec.log_name==name:
                    pword=raw_input("Enter your password :")
                    if rec.pswd==pword:
                        cust_id=rec.cust_id
                        file.close()
                        return cust_id
                    else:
                        print ("INCORRECT PASSWORD")
                        return -1
        except EOFError:
            print ("INCORRECT LOGIN NAME")
            return -1
        finally:
            ch=raw_input("Enter a key to continue")
                        
def user_mode(cust_id):
    while (True):
        os.system("cls")
        print ("******************************************************")
        print ("                   USER MODE")
        print ("****************************************************")
        print("                             ")
        print ("                      MENU")
        print("                     ")
        print ("1.      DISPLAY MOBILE DETAILS")
        print ("2.      ADD TO CART")
        print ("3.      VIEW CART")
        print ("4.      RETURN TO THE MAIN MENU")
        print ("5.      EXIT")
        print("                  ")
        choice=input("ENTER THE CHOICE (1-5) : ")
        if choice==1:
            display_mobile()
        elif choice==2:
            add_to_cart(cust_id)
        elif choice==3:
            view_cart(cust_id)
        elif choice==4:
            return
        else :
            exit()
            
def add_to_cart(cust_id):
    mfound=False
    price=0.0
    ofile=open("order.dat","ab")
    mfile=open("mobile.dat","rb")
    try :   
        id=raw_input("Enter the model no. which you want to buy :")
        item=Order()
        while True:
            rec=pickle.load(mfile)
            if rec.model_no==id:
                mfound=True
                qty=input("Enter the no. of pieces :")
                if qty<=int(rec.qty):
                    item.cust_id=cust_id
                    item.model_no=id
                    item.qty=qty
                    item.price=float(rec.price)
                    item.total=item.qty*item.price
                    pickle.dump(item,ofile)
                    break
                else :
                    print (qty+" NUMBER OF PIECES ARE NOT AVAILABLE")
                    return -1
    except EOFError:
        if mfound==False:
            print ("The model does not exist")
    finally:
        ofile.close()
        mfile.close()

def view_cart(cust_id):
    cfound=False
    total=0.0
    item=Order()
    ofile=open("order.dat","rb")
    print (" MODEL NO             QUANTITY             PRICE")
    print (" -----------------------------------------------")
    try :
        while True:
            item=pickle.load(ofile)
            if item.cust_id==cust_id:
                cfound=True
                item.display_rec()
                total=total+item.total           
    except EOFError:
        if cfound==False:
            print ("THE CART IS EMPTY")
        else:
            print(" ")
            print(" ")
            print (" TOTAL PRICE =                             "+str(total))
    finally:
        ofile.close()
        ch=raw_input("Press any key to continue")                     
    
def add_mobile():
    found=False
    wrfile=open("mobile.dat","rb+")
    mobj=Mobile()
    mobj2=Mobile()
    model=raw_input("MODEL NUMBER :")
    try:
        while True:
            mobj=pickle.load(wrfile)
            if mobj.model_no==model:
                found=True
                print ("This model number already exists")
                ch=raw_input("Press any key to continue")
                break
    except EOFError:
        mobj2.model_no=model
        mobj2.create_rec()
        pickle.dump(mobj2,wrfile)
    finally:
        wrfile.close()
        return
    
def modify_mobile():
    found=False
    mod_obj=Mobile()
    model=raw_input("Enter the model number which you want to modify :")
    try :    
            rdfile=open("mobile.dat","rb")
            tmp=open("temp.dat","wb")
            while (True):
                mobj=pickle.load(rdfile)
                if found==False and mobj.model_no==model :
                    found=True
                    mobj.display_rec()
                    print ("Please enter the new values :")
                    mod_obj.model_no=model
                    mod_obj.create_rec(MODIFY)
                    mod_obj.check_rec(mobj)
                    ch=raw_input("\nPress any key to continue :")
                    pickle.dump(mod_obj,tmp)
                else:
                    pickle.dump(mobj,tmp)
    except EOFError:
            if found==False:
                print ("MODEL NOT FOUND")
                ch=raw_input("\nPress any key to continue :")
    except IOError:
            print ("FILE DOES NOT EXIST")
            ch=raw_input("\nPress any key to continue :")
    finally:
            rdfile.close()
            tmp.close()
            if found==True:
                os.remove("mobile.dat")
                os.rename("temp.dat","mobile.dat")
            else :
                os.remove("temp.dat")

def delete_mobile():
    found=False
    mod_obj=Mobile()
    model=raw_input("Enter the model number which you want to delete :")
    try :    
            rdfile=open("mobile.dat","rb")
            tmp=open("temp.dat","wb")
            while (True):
                mobj=pickle.load(rdfile)
                if found==False and mobj.model_no==model :
                    found=True
                    mobj.display_rec()
                    ch=raw_input("\nAre you sure you want to delete this record(Y/N):")
                    if ch!="y" and ch!="Y" :     
                        print ("before writing")
                        pickle.dump(mobj,tmp)
                        ch=raw_input("after writing")
                else:
                    pickle.dump(mobj,tmp)                            
    except EOFError:
            if found==False:
                print ("MODEL NOT FOUND")
                ch=raw_input("\nPress any key to continue :")
    except IOError:
            print ("FILE DOES NOT EXIST")
            ch=raw_input("\nPress any key to continue :")
    finally:
            rdfile.close()
            tmp.close()
            os.remove("mobile.dat")
            os.rename("temp.dat","mobile.dat")

def display_mobile():
        found=False
        model=raw_input("Search for the model no :")
        try :    
            rdfile=open("mobile.dat","rb")
            while (True):
                mobj=pickle.load(rdfile)
                if mobj.model_no.find(model)!=-1 :
                    found=True
                    mobj.display_rec()
                    ch=raw_input("\nPress any key to continue :")
                    
        except EOFError:
            if found==False:
                print ("MODEL NOT FOUND")
                ch=raw_input("\nPress any key to continue :")
        except IOError:
            print ("FILE DOES NOT EXIST")
            ch=raw_input("\nPress any key to continue :")
        finally:
            rdfile.close()
                    
    
#main
main_menu()
