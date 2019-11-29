def wallet(balance=0):
    def deposit(amount=0):
        nonlocal balance
        balance += amount
        return balance

    def spent(amount=0):
        nonlocal balance
        balance -= amount

    def show():
        nonlocal balance
        return balance

    return {'deposit': deposit, 'spent': spent, 'show': show}


n = int(input("Enter number of users: "))
person = list(range(0, n))
for i in range(0, n):
    print("PERSON " + str(i + 1))
    balance1 = int(input("Enter your initial balance: "))
    # deposit1 = int(input("Enter amount to deposit: "))
    # spent1 = int(input("Enter spending amount: "))

    person[i] = wallet(balance1)
    # person[i]['deposit'](deposit1)
    # person[i]['spent'](spent1)
    # print("Wallet balance: " + str(person[i]['show']()))

choice3 = input("\nWould you like to deposit (y/n)?")
if choice3 == 'y':
    user3 = int(input("\nEnter user number to deposit: "))
    deposit1 = int(input("Enter amount to deposit: "))
    person[user3-1]['deposit'](deposit1)
    print("Amount deposited!!")
else:
    print("Thank you!")

choice1 = input("\nWould you like to see your balance(y/n)?")
if choice1 == 'y':
    users = int(input("\nEnter user number to show: "))
    print("PERSON " + str(users) + " balance: " + str(person[users-1]['show']()))
else:
    print("Thank you!")

choice2 = input("\nWould you like to withdraw(y/n)?")
if choice2 == 'y':
    u = int(input("Enter user number: "))
    w = int(input("Enter amount to withdraw: "))
    person[u-1]['spent'](w)
    print("Amount spent!!")
    print("Remaining for Person " + str(u) + " balance: " + str(person[u-1]['show']()))
else:
    print("Thank you!")

choice4 = input("\nWould you like to transfer funds to another person(y/n)?")
if choice4 == 'y':
    u1 = int(input("Enter user number to transfer from: "))
    u2 = int(input("Enter user number to receive money: "))
    w2 = int(input("Enter amount to send: "))
    person[u1-1]['spent'](w2)
    person[u2-1]['deposit'](w2)
    print("Funds Transferred!")
    print("Remaining for Person " + str(u1) + " balance: " + str(person[u1-1]['show']()))
    print("Remaining for Person " + str(u2) + " balance: " + str(person[u2 - 1]['show']()))
else:
    print("Thank you!")