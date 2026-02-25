max_attempts  = 5
attempts  = 0
username =  'python'
password  = 1234
amount  = 0
balance  = 5000
transaction_pin  = 4040



 
          

def check_balance(balance):
    print(f"Current balance is: {balance:.2f}$")
    return balance 



def deposit():
    amount  = float(input("Enter deposit amount:"))
    if amount > 1:
        print(f"The sum of: {amount:.2f}$ has been deposited to your account")
        return amount
    
    else:
        print("Amount can't be deposited!!")
        return amount
        
       
    
    
def withdraw(amount):
    amount  = float(input("Enter the amount you want to withdraw: "))
    
    if amount > balance:
        print("Insufficient fund to withdraw!!")
        return 0

    elif amount <= balance:
        print(f"You just withdrew the sum of: {amount:.2f}$ from your account!")
        return amount
        
    else:
        print("Please enter a valid amount!")
        
       
        
            
def transfer(balance):
    bank_name  = input("Enter preferred bank name: ")
    account_number = int(input("Enter the (10)digits recipient account number: "))
    recipient_name = input("Enter recipient's name: ")
    amount  = float(input("Enter the amount you want to transfer: "))
    user_transaction_pin  = int(input("Enter your transfer pin: "))
    
    
            
    if amount <= balance and user_transaction_pin == transaction_pin:
         print("Transfer successful")
         print(f"TRANSFER RECEIPT\nThe  sum of: {amount:.2f}$ has been transferred!!\nRecipient's name: {recipient_name}\nBank name: {bank_name}\nAccount number: ({account_number}).")
         return amount
        
             
         
    else:
        print("Insufficient amount to  transfer\nOr Incorrect transfer pin!!")
        
        return amount         





while attempts < max_attempts:
    try:
        user_name = input("Enter your username: ")   
        user_password = int(input("Enter your password: "))
        if user_name == username and user_password == password:
           print("Login successful...........")
           print("PLease wait__________")
           print("Dashboard is loading>>>>>>>>>>")
           pass
           
           
           
           print("************************")
           print(f"WELCOME TO XAMY9 BANK ")
           print("************************")
           print(f"Hello,{user_name}!!")
        
           print("Please choose an option:")
           print("1. check balance")
           print("2. Deposit fund")
           print("3. withdraw")
           print("4. Transfer fund")
           print("5. Exit")
    
  
  
           option  = input("Choose from the options above(1, 2, 3, 4, 5):")
      
           if option == "1":
              check_balance(balance)  
                
   
           elif option =="2":
              balance+= deposit()
       
           elif option == "3":
              balance -= withdraw(balance)
       
           elif option =="4":
              balance -= transfer(balance)
       
           elif option == "5":
             print("Thank you for banking with us!\nBye!!")
             break
       
           
              
    
        else:
           attempts = attempts + 1
           remaining = max_attempts - attempts
           print(f"Wrong password or username. You have {remaining} attempts left.") 
           
    except ValueError:
      print("Invalid input, Please enter your correct username amd password")
          
if attempts == max_attempts:
           print("Account locked, Maximum attempts exceeded")  
          



         
    
       
       
       
   
                                
