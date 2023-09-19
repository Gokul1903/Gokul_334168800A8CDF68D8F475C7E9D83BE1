#I'm going to creat a program for a BankAccount as a interactive program,That going to get some user input and continue the process.Like a real time example

#main class
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposite in 100s"""
        if amount %100==0:
            self.account_balance += amount
        else:
            print("\nThe amount should be in the multiple of 100's".title())
            

    def withdraw(self, amount):
        """Withdraw the specified amount from the account."""
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"\n---\tWithdrew {amount}\t--- \n")
        else:
            print("\nInsufficient funds\n")

    def display_balance(self):
        """Display the account balance"""
        print(f"\nAccount Holder: {self.account_holder_name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: {self.account_balance:.2f}\n")


#testing the class
account_number=int(input("Enter your account number : "))
account_holder=input("Enter account holder name : ")
a=int(input("Enter your PIN : "))
    
account = BankAccount(account_number, account_holder, initial_balance=0)

    # Displaying initial account balance
account.display_balance()

#class for access BankAccount class
class process:
    def depo(self):
        dep=int(input("""\nEnter the Amount you want to deposite "AMOUNT SHOULD BE IN THE MULTIPLE OF 100" : """))

        account.deposit(dep)
        if dep %100==0:
            print(f"\n---\tDeposited {dep}\t---\n")

    # Displaying updated account balance
    def dis(self):
        account.display_balance()


    # Withdrawing money
    def withd(self):
        wit=int(input("\nEnter the Amount to Withdraw : "))
        if wit %100==0:
            account.withdraw(wit)
        else:
            print("\nThe amount should be in the multiple of 100's\n".title())
        
#object creation
obj=process()
#User input for user convenience
while(1):
    print("Enter 1 for deposite\nEnter 2 for Withdraw\nEnter 3 for checking Balance\nEnter 4 for Exit")
    op=(input("Enter your choice : "))
    if op=="1":
        obj.depo()
    elif op=='2':
        obj.withd()
    elif op=='3':
        obj.dis()
    elif op =='4':
        break
        
    else:
        print("\nInvalid choice\n")
    
   
