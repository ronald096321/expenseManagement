#creating the expenses
#create 1st expense

def createfile():
    fileobject = open("userdetails.csv" , "x")
    data = " Date , Category , Description , Amount "
    fileobject.write(data)

    
detail = []

def userinput():
    date = int(input(" Please enter the date : "))
    category = input(" Please enter the category you want : ")
    description = input( " Description : ")
    amount = int(input(" Please enter the amount : "))
    data = date+","+category+","+description+","+amount
    return data

createfile()
userinput()


    

   
