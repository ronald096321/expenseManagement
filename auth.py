#user authentication
from os.path import exists;
from userexist import checkUserExist;
import csv;
import json;


#Function to add all the expenses to the file
def authFile() :
      username = input("Enter the user name : ")
      pasword = input("Enter the password : ")
      users = open("users.json","r")
      x = users.read()
      userObj = json.loads(x)
      print("users",len(x))