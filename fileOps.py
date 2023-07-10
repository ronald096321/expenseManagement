from os.path import exists;
from userexist import checkUserExist;
import csv;
import operator


#Function to add all the expenses to the file
def addExpTOFile(userData) :
      path = "expenses.csv";
      data = userData.values();
      fileExist = exists(path);
      if(fileExist) : 
            print("file exist");
            fileObj = open(path,"a",newline='');
            writer = csv.writer(fileObj);
            writer.writerow(data);
            fileObj.close();
      else :
            print("File dose not exist");
            fileObj = open(path,"x",newline='');
            writer = csv.writer(fileObj);
            writer.writerow(["Date" , "Category" , "Description", "Amount"]);
            writer.writerow(data);
            fileObj.close();


def getAllExpFromFile() : 
               path = "expenses.csv";
               fileExist = exists(path);
               if fileExist : 
                  fileObj = open(path,'r');
                  fileData = csv.reader(fileObj);
                  expData = list(fileData);
                  print("csv out", expData);
                  finalObj = mapExpenseData(expData);
                  return finalObj;
        

  

def mapExpenseData(expData) :
       expenseList = [];
       length = len(expData);
       for index in range(len(expData)) :
              if index > 0 and index != length :
                     expDict = {
                            "index" : index,
                            "Date" : "",
                            "Category" : "",
                            "Description": "",
                            "Amount" : "0"
                     }
                     for jindex in range(len(expData[index])) :
                            if jindex == 0 : 
                                    expDict["Date"] = expData[index][jindex];
                            elif jindex == 1 :
                                    expDict["Category"] = expData[index][jindex];
                            elif jindex == 2 :
                                    expDict["Description"] = expData[index][jindex];
                            else :
                                   expDict["Amount"] = expData[index][jindex];
                     expenseList.append(expDict);
                            
       return expenseList[0:len(expenseList)-1];

def showAllExpenses() : 
       fileData = getAllExpFromFile();
       displayResult(fileData);
       

def filter(key , value) :
       fileData = getAllExpFromFile();
       filteredResult = [d for d in fileData if d[key] == value];
       displayResult(filteredResult);     
     
def sort(key) :
       fileData = getAllExpFromFile();
       sortedResult = sorted(fileData , key=operator.itemgetter(key));
       displayResult(sortedResult);   

def modify(index ,key , value) : 
         fileData = getAllExpFromFile();
         fileData[index][key] = value;
         print(" Modify Successful !");
         displayResult(fileData);

def delete(index) :
       fileData = getAllExpFromFile();
       del fileData[index];
       for index1 in range(len(fileData)) :
              fileData[index1]["index"] = index1 + 1;
       print(" Delete Successful !");
       displayResult(fileData);



def displayResult(data) : 
       fileData = data;
       print("----------------------------------------------------------------------------");
       print("|slNo |     Date    |     Category   |     Description     |     Amount    |");
       print("----------------------------------------------------------------------------");
       for index in range(len(fileData)) : 
              desc = fileData[index]["Description"];
              Description = '';
              if len(desc) >= 15 :
                     Description = operator.getitem(desc, slice(0, 15));
              else :
                    lenToFill = 15 - len(desc);
                    Description = desc.ljust(lenToFill," ");           
              print("",fileData[index]["index"],"  ",fileData[index]["Date"],"     ",fileData[index]["Category"],"    ",Description,"              ",fileData[index]["Amount"]," ");




# getAllExpFromFile();