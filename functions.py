
def happy_birthday(name,age):
    
 print (f"happy birthday to {name}" )
 print(f"you are old {age}")
 print("happy birthday to you ")
 print("congratulations")

happy_birthday("joe","23")

happy_birthday("jack","45")


happy_birthday("hellen","67")

#invoice
def my_invoice(name,money,date):
    
    return(f"{name} " f"{money}" f"{date}") 
invoice=my_invoice("jack" ,"$500",2/23/2200)
print(invoice)

#employee salary calculator
def total_salary(name,salary):


    
    basic_salary=int(input("enter your basic salary"))
    
    allowance=int(input("enter your basic allowance"))
    
    salary=basic_salary + allowance
    
    return f"employee name :{name}", f" employee salary:{salary}"

name=input("enter your name")


print(total_salary("name","salary"))




    

