#user authentication
from userexist import checkUserExist;


#Function to add all the expenses to the file
def authFile() :

      userMatched = False;
      while not userMatched : 
            username = input("            Enter the user name : ");
            pasword =  input("             Enter the password : ");
            isUserExist = checkUserExist(username,pasword);
            if isUserExist == True : 
                  print("                 Authentication Successful ");
                  userMatched = True;
                  return True;
            else : 
                  print("                 Unable to Aunthenticate User Please Try Again! " );     