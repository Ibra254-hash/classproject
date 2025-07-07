def display_menu():
    print("/nwelcome to simple bankig!")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

def deposit(balance):
    amount = float(input("enter amount to deposit:"))
    if amount>0:
        balance += amount
        print(f"Successfully deposited Ksh{amount:,.2f}")
    else:
        print("Invalid amount. Please enter a positive number.")
    return balance

def withdraw(balance):
  try:
      amount = float(input("Enter amount to withdraw:")) 
  except ValueError:
   if amount <=0:
    print("Invalid amount. Please enter a positive number.")
   elif amount > balance:
    print("Insufficient funds!")
   else:
      balance-=amount
      print(f"Withdraw Ksh {amount:,.2f}") 
  except ValueError: 
     print("Invalid input. Please enter a number.")  
     return balance
  
def check_balance(balance):
   print(f"Your current balance is: Ksh {balance:,.2f}")

def main():
   balance=0.0
   while True:
      display_menu()
choice=input("choose an option (1-4):")

if choice =='1':
   balance=deposit('balance') 
elif choice =='2':
   balance= withdraw('balance')
elif choice =='3':
   check_balance('balance')
elif choice =='4':
   print("Thank you using Simple Bank. Goodbye!")