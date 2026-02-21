# get username and password:

u_name = "python"
u_password = "1234"


# Handle error inputs:
try:
    User_name = input("Enter your username: ").lower()
    Password = input("Enter your password: ")
  
    if User_name == u_name and Password == u_password:
      print("Login successful________")
      print("Please wait.........") 
      pass
          
    else:        
      print("Wrong password")
      print("Please  enter a valid username and password!!")
      
except ValueError:
        print("ERROR INPUT!!")         
    
def main():
    balance = 1000
    Running = True
    amount = 0
    
    
    while True:
        print("*********************")
        print(f"WELCOME TO XAMY BANK {User_name}!!")
        print("**********************")
        
        print("Please choose an option:")
        print("1. check balance")
        print("2. Deposit fund")
        print("3. withdraw")
        print("4. Exit")
        
        option = input("Enter your prefarred option(1, 2, 3, 4): ")
        
        
        if option == "1":
         show_balance(balance - amount)
        elif option =="2":
          balance = balance + deposit()
        elif option == "3":
          balance = balance - withdrawal(balance)
        elif option == "4":
          print("Thank you for banking with us!!")
          Running == False
          break
      
        else:
          print("Invalid option. please enter a valid option!!") 
    
  # create a balance check function: 
def show_balance(balance):
    print(f"Current balance is: {balance:.2f}$")
    return balance 

   # create a deposit function:
def deposit():
    amount = float(input("Enter deposit amount: "))
    
    if amount < 1:
        print("Insufficient fund to deposit")
        return amount
    else:
        print(f"You just deposited: {amount:.2f}$ to your account!")
        return amount
    
    #create a withdrawal function:
def withdrawal(balance): 
    amount = float(input("Enter withdraw amount: "))
    
    if amount > balance:
        print("Insufficient fund")
        return 0
    else:
        print(f"Them sum of: {amount}$ has just been withdrawned from your account now!")
        return amount                               
if __name__ =="__main__":
    main()   
        
        