class UserNotFound(Exception):
    def __init__(self, msg="Username not found"):
        Exception.__init__(self, msg)


class WrongPassword(Exception):
    def __init__(self, msg="Invalid password"):
        Exception.__init__(self, msg)


username = {"Rahul": 'ryadav', "Lakshit": "ltandon", "Sajal": "sgupta"}

try:
    user = input("Enter user name: ")
    if user not in username:
        raise UserNotFound
    password = input("Enter password: ")
    if password not in username.values():
        raise WrongPassword
    print("User logged in!!")
except UserNotFound as e:
    print(e)
except WrongPassword as e:
    print(e)
