global name

global address

global age 

global status


def menu():
    
    print ('MENU')
    
    print ('1.Add')
    
    print ('2.Display')
    
    print ('3.Edit')
    
    print ('4.Delete')
    
    print ('5.Exit')
    choose = int(input("Choose on Menu: "))
    
    if choose == 1:
    	add()
    elif choose == 2:
    	display()
    elif choose == 3:
    	edit()
    elif choose == 4:
    	delete()
    else:
    	print ("Invalid")
    
def add():
  
  global name

  global address

  global age 

  global status

menu()

name = str(input("Name: "))
address = str(input("Address: "))
age = int(input("Age: "))
status = str(input("Status: "))
    
    


def display():
	
    global name

    global address

    global age 

    global status
	
    print ("Name: ",name)
    print ("Adress: ",address)
    print ("Age: ",age)
    print ("Status: ",status)
    
menu()

def edit():

  global name

  global address

  global age 

  global status
    
choose = str(input("Choose to Edit: "))
    
if choose == 'name':
    name= str(input("Name: "))
elif choose == 'address':
    	address= str(input("Address: "))
elif choose == 'age':
    	age= int(input("Age: "))
elif choose == 'status':
    	status= str(input("Status: "))
else:
    	print ("Invalid")
    
def delete():

  global name

  global address

  global age 

  global status
    
choose = str(input("Choose to Delete: "))

if choose == 'name':
    	name = (" ")
elif choose == 'address':
    	address = (" ")
elif choose == 'age':
    	age = (" ")
elif choose == 'status':
    	status = (" ")
elif choose == 'dall':
    name = (" ")
    address = (" ")
    age = (" ")
    status = (" ")
else:
    	print ("Invalid")
        
menu()
    
menu()
