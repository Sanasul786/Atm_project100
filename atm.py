class atm(object):
    def __init__ (self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
    def check_balance(self):
        print("Your balance is 50000")
    def cash_withdraw(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawn amount "+str(amount)+".Your remaining balance is "+str(new_amount))
def main():
    card_number =input("Insert your card number:-")
    pin_number =input("Enter your pin number:-")
    new_user = atm(card_number,pin_number)
    print("Choose your activity")
    print("1.Balance enquiry      2.Withdrawl")
    activity = int(input("Enter activity number:->"))
    if(activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount = int(input("How much amount would you like to withdraw:->"))
        new_user.cash_withdraw(amount)
    else:
        print("Enter a valid number")
if __name__=="__main__":
    main()

