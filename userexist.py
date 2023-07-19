import json;

def checkUserExist(username , password) :
               users = open("users.json","r");
               userData = users.read();
               userJson = json.loads(userData);
               present = False;
               for index in range(len(userJson)) : 
                      if userJson[index]["username"] == username and userJson[index]["password"] == password : 
                             present = True;
               return present;