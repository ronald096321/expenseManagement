from os.path import exists;
from userexist import checkUserExist;
import csv;
import json;


#Function to add all the expenses to the file
def addExpTOFile() : 
      path = "expenses.csv";
      data = ["vinay" , "English" , "60.0"];
      fileExist = exists(path);
#       username = input("Enter the user name : ");
#       pasword = input("Enter the password : ");
#       users = open("users.json","r");
#       x = users.read();
#       userObj = json.loads(x);
#       print("users",len(userObj));
#       print(checkUserExist(userObj ,username, pasword));
#       isExist = checkUserExist(userObj ,username, pasword);
#       if isExist : 
#               print("Auth success") ;
#       else :
#               print("Not success");        
    #   for index in range(len(userObj)) : 
    #         if (userObj[index]["username"] == username and userObj[index]["password"] == pasword) :
    #               print("Auth success");
    #         else :
    #             print("Not success");
      
    #   for user in range(len(x)) : 
    #          print(user);
      if(fileExist) : 
            print("file exist");
            fileObj = open(path,"a");
            writer = csv.writer(fileObj);
            writer.writerow(data);
      else :
            print("File dose not exist");
            fileObj = open(path,"x");
            writer = csv.writer(fileObj);
            writer.writerow(["Name" , "Subject" , "Percentage"])
            writer.writerow(data);


addExpTOFile();


def getAllExpFromFile() : 
      print("hello");
        
                        