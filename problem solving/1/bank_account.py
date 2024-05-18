# this program takes the user requirements like deposit,withdraw,check balance,calculate interest.
# if user enters any one of this option the respective action gets executed

# define "BankAccounts" class that manages these banking ooperations
class BankAccounts:
    def __init__(self, ac_no, balance):
        self.ac_no = ac_no
        self.balance = balance
        
    # create "deposit" method and deposit the user entered amount
    def deposit(self, deposit_amt):
        if deposit_amt > 0:
            self.balance = self.balance + deposit_amt
            print(f"The {deposit_amt} deposited successfully ")
        else:
            print("Invalid  deposit amount!")
            
    # create "withdraw" method and pass parameter to know the withdraw amount ,then cut amount from bank
    def withdraw(self, withdraw_amt):
        if self.balance < withdraw_amt <= 0:
            print("Insufficient funds!")
        else:
            self.balance = self.balance - withdraw_amt
            print(f"The {withdraw_amt} withdrawn")

    #create "calculate_interest" method to check the interest based on the balance they have,
    # if balance is >= 5000 provide 2 % interest ,else 1% interest and credit that amount to user account
    def calculate_interest(self):
        if self.balance >= 5000:
            interest = self.balance * 0.02
            self.balance = self.balance + interest
            print(f"Interest of {int(interest)} rs is added to your balance  ")
        else:
            interest = self.balance*0.01
            self.balance = self.balance + interest
            print(f"Interest of {int(interest)} rs is added to your balance  ")

    # create "check__bal" method to check the balance of the user account
    def check_bal(self):
        print(f"Your current balance is {self.balance}")


#prompt the user to input the 12 digit number
print("Welcome to our Bank🏦")
ac_num = input("Enter the  12 digit account number: ")
user1 = BankAccounts(ac_num, 200)

# now define while loop to repeatedly display the user requirements untill he
# enters quit the loop should keep on execute
while True:
    if len(ac_num)==12:
        user_requirements = int(input(''' Please select the option from the below menu >
                                1 . deposit
                                2 . withdraw
                                3 . calculate_interest
                                4 . check_balance
                                5 . quit
                               Enter the option >  '''))
        if user_requirements == 1:
            user1.deposit(int(input("Enter the amount that you want to deposit >")))
        elif user_requirements == 2:
            user1.withdraw(int(input("Enter the withdraw amount >")))
        elif user_requirements == 3:
            user1.calculate_interest()
        elif user_requirements == 4:
            user1.check_bal()
        elif user_requirements == 5:
            print("Thank You 😊🙏")
            break
        else:
            print("Invalid option !")
            break
    else:
        print("invalid ac number")
        break
