from auth import authFile;
from createExp import userinput;
from fileOps import addExpTOFile ,getAllExpFromFile; 
#Starter file
def loginOrRegister(login) : 
            match login:
                case 1 :
                    return authFile();
                case 2 : 
                    return "0";
                case default :
                     return 0;   

def expenseOptions() : 
      print("           Press 1 for creating the new expense");
      print("           Press 2 for Listing all the expenses");
      print("           Press 3 for expense filtering and sorting");
      print("           Press 4 for expense modification and deletion");
      print("           Press 5 for expense reporting");
      option = int(input("Please enter your input for performing above mentioned operations : "));
      return option;

def performOperation(option) :
      match option :
                case 1 : 
                    expObj = userinput();
                    addExpTOFile(expObj);
                    print("Created Expense");
                    return 0;
                case 2 : 
                    getAllExpFromFile();
                    print("fetched Expense");
                    return 0;
                case 3:
                    print("Filtered Expense");
                    return 0;
                case 4 :
                    print("Modified Expense");
                    return 0;
                case 5 : 
                    print("Reported Expense");
                    return 0;
                case default :
                    return 0;


print("");
print("");
print("** Welcom to Expense Management, A solution to manage ypur expenses implemented using Python technology **");
print("");
print("");
login = int(input("         Please Enter 1 to login and 2 to register   : "));

isUserLoggedIn = loginOrRegister(login);

if isUserLoggedIn : 
      userOption = expenseOptions();
      performOperation(userOption);
      





