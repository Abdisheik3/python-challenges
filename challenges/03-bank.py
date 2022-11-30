
blc = 0

def balance(blc):
    return print(f"Your balance is {blc} ")

def withdraw(blc):
    withdraw_amount = input("How much would you like to withdraw ")
    blc = blc - int(withdraw_amount)
    return print(blc)

def deposit(blc):
    deposit_amount = input("How much would you like to deposit ")
    blc = blc + int(deposit_amount)
    return print(blc)

bank = True
while(bank):
    user_option = input("1: View balance', 2: Make a withdrawal, 3: Make a deposit, or 4: None. Please enter a number: ")
    if user_option == "1":
        balance(blc)
    elif user_option == "2":
        withdraw(blc)
    elif user_option == "3":
        deposit(blc)
    else: break

print("Thank you")