#creating the expenses
#create 1st expense

def createfile():
    fileobject = open("userdetails.csv" , "x")
    data = " Date , Category , Description , Amount "
    fileobject.write(data)

    
detail = []

def userinput():
    date = input(" Please enter the date in DD-MM-YYYY format : ");
    category = input(" Please enter the category you want : ")
    description = input( "Please enter the Description : ")
    amount = int(input(" Please enter the amount : "))
    return {
        "date" : date,
        "category" : category,
        "description" : description,
        "amount" : amount
    }



    

   
