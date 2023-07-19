from fileOps import filter,sort,showAllExpenses,getAllExpFromFile,displayResult,modify,delete;

def createfile():
    fileobject = open("userdetails.csv" , "x")
    data = " Date , Category , Description , Amount "
    fileobject.write(data)

    
detail = []
categoryDict = {
     "0" : 'Housing',
     "1" : 'Transport',
     "2":'Food',
     "3":'Utility',
     "4":'Cloth',
     "5":'Medical'
 }

filterDict = {
      "0" : 'Date',
      "1" : 'Category',
      "2": 'Amount',
      "3":'Description'
}

def userinput():
    date = input(" Please enter the date in DD-MM-YYYY format : ");
    selectedCategory = selectUserCategory();
    # category = input(" Please enter the category you want : ")
    description = input( "Please enter the Description : ")
    amount = int(input(" Please enter the amount : "))
    return {
        "date" : date,
        "category" : categoryDict[selectedCategory],
        "description" : description,
        "amount" : amount
    }

def selectUserCategory() : 
        selectCategory = True;
        print("Please select category from below list");
        print("For Housing select 0");
        print("For Transport select 1");
        print("For Food select 2");
        print("For Utility select 3");
        print("For Cloth select 4");
        print("For Medical select 5");
        while selectCategory :
            category = input("Please select your category input : ");
            if(category == '0' or category == '1' or category == '2' or category == '3' or category == '4' or category == '5') :
                 selectCategory = False;
            else : 
                 print("Please select the valid category from list only");
                 selectCategory = True;
        return category;


def filterOrSortExpense() :
     repeat = True;
     while repeat :
            operation = input("Press 1 for filter and 2 for sort : ");
            if operation == '1' or operation == '2' :
                repeat = False;
                if operation == '1' :
                    filterInputs();
                    print("filter logic");
                else :
                    sortInputs();
                    # sort(sortValues);
                    print("Sort logic");
            else :
                repeat = True;
                print("Please enter valid input");


def filterInputs() :
     repeat = True;
     print("Please select filter option from below list to filter");
     print("For date select 0");
     print("For category select 1");
     print("For amount select 2");
     while repeat :
          category = input("Please select the filter option value : ");
          if(category == '0' or category == '1' or category == '2') :
               repeat = False;
               value = input("Please enter the value to filter with : ");
               filter(filterDict[category],value);
          else :
               repeat = True;
               print("Please select the proper value ");




def sortInputs() :
     repeat = True;
     print("Please select sort option from below list to sort");
     print("For date select 0");
     print("For category select 1");
     print("For amount select 2");
     while repeat :
          category = input("Please select the sort option value : ");
          if(category == '0' or category == '1' or category == '2') :
               repeat = False;
               sort(filterDict[category]);
          else :
               repeat = True;
               print("Please select the proper value ");



def modifyExpData() : 
     showAllExpenses();
     selectedData = [];
     fileData = getAllExpFromFile();
     length = len(fileData);
     slno = input("Please select the slNo of the data you want to modify : ");
     intSl = int(slno);
     if intSl > 0 and intSl <= length :
          print("Data selected to modify ")
          selectedData.append(fileData[intSl - 1]);
          displayResult(selectedData);
          print("Please select the expense field to be modified");
          print("For Date select 0");
          print("For Category select 1");
          print("For Amount select 2");
          print("For Description select 3");
          
          prop = input("Please slect inputs from above list :");
          if prop == "0" or prop == "1" or prop == "2" or prop == "3" :
               if prop == "1" :
                    category = selectUserCategory();
                    modify(intSl - 1,filterDict[prop],categoryDict[category]);
                    
               else : 
                strNew = "Please enter the new value for " + filterDict[prop] + ":";
                val = input(strNew);
                modify(intSl - 1,filterDict[prop],val);
               
               
def deleteData() :
      showAllExpenses();
      selectedData = [];
      fileData = getAllExpFromFile();
      length = len(fileData);
      slno = input("Please select the slNo of the data you want to delete : ");
      intSl = int(slno);
      if intSl > 0 and intSl < length :  
           input1= input("Are you sure you want to delete y/n : ");
           if input1 == 'Y' or input1 =='y' : 
                          delete(intSl - 1);
           else :
                print("Delete cancelled !")
      else :
          print("Data not found to Delete ");
                  
          
def modifyOrDelete() :
     repeat = True;
     print("Please enter 1 to modify and 2 to delete");
     while repeat : 
        val = input("Please enter your input : ");
        if val == '1' or val == '2' :
            repeat = False;
            if val == '1' : 
                modifyExpData();
            else :
                deleteData();
        else :
            print("Please enter the proper value :")     
               



    

   
