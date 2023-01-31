from os import system
import time


class ATM:
    def __init__(self):
        self.start()

    def start(self):
        system('clear')
        print('1	New User')
        print('2	Already User')
        login_value = int(input('Enter : '))
        if login_value == 1:
            self.signUp()
        elif login_value == 2:
            self.logIn()
        else:
            print('Enter valid number')
            self.start()

    def signUp(self):
        system('clear')
        print('Sign in Page')
        self.name, self.surname = input(
            'Enter your name and surname : ').split()
        if self.name == ' ' or self.surname == ' ' or self.name.isdigit() or self.surname.isdigit():
            print('Please enter your name and surname correctly !')
            time.sleep(3)
            self.signUp()
        else:
            self.cardnum = input('Enter your card number : ')
            if len(self.cardnum) == 16:
                self.pin = input('Enter your card pin code : ')
                self.balance = int(input('Enter your balance : '))
                if len(self.pin) == 4:
                    with open('db.txt', 'r') as database:
                        db = database.readline().split()
                        if self.name != db[0] or self.surname != db[1] or self.cardnum != db[2] or self.pin != db[3] or self.balance != db[4]:
                            with open('db.txt', 'a') as database:
                                database.write(
                                    f'\n{self.name.capitalize()} {self.surname.capitalize()} {self.cardnum} {self.pin} {self.balance}')
                                self.logged()
                        elif self.name == db[0] and self.surname == db[1] and self.cardnum == db[2] and self.pin == db[3]:
                            print('You are already a user')
                            print('Please try Log in')
                            self.logIn()
                        else:
                            print('Something went wrong !')

    def logIn(self):
        system('clear')
        print('Login Page')
        self.name, self.surname = input(
            'Enter your name and surname : ').split()
        if self.name == ' ' or self.surname == ' ' or self.name.isdigit() or self.surname.isdigit():
            print('Please enter your name and surname correctly !')
            time.sleep(3)
            self.logIn()
        else:
            self.pin = input('Enter your card pin code : ')
            self.balance = input('Enter your balance : ')
            if len(self.pin) == 4:
                with open('db.txt', 'r') as data:
                    for line in data.readlines():
                        if self.name == line.split()[0] and self.surname == line.split()[1] and self.pin == line.split()[3] and self.balance == line.split()[4]:
                            print(f'User : {self.name} {self.surname}')
                            print(f'Pin : {self.pin}')
                            print(f'Balance : {self.balance}')
                            time.sleep(3)
                            self.logged()
            else:
                print('Wrong Data')

    def logged(self):
        system('clear')
        print('1  View Balance')
        print('2  Set new pin')
        print('3  Take cash')
        print('4  Add money')
        print('0  Log Out')
        self.val = int(input('Enter : '))
        if self.val == 1:
            print(f'Your balance is {self.balance}')
            log = int(input('Enter 0 to return back : '))
            if log == 0:
                self.logged()
        elif self.val == 2:
            print(f'Your old pin code is {self.pin}')
            new_pin = input('Enter new pin : ')
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print(f'Your new Password is {self.pin}')
                log = int(input('Enter 0 to return back : '))
                if log == 0:
                    self.logged()
            else:
                for i in range(3):
                    new_pin = input('Enter new pin : ')
                    if i == 2:
                        print('Your card have been blocked')
                        break
        elif self.val == 3:
            self.takeCash()
        elif self.val == 4:
            print('How much you want to add ?')
            pay = int(input('Enter amount : '))
            self.balance += pay
            log = int(input('Enter 0 to return back : '))
            if log == 0:
                self.logged()
        elif self.val == 0:
            self.logOut()
        else:
            print('Please choose one of options')
            log = int(input('Enter 0 to return back : '))
            if log == 0:
                self.logged()

    def takeCash(self):
        system('clear')
        print(f'Your balance is {self.balance}')
        cash = int(input('Enter how much you want : '))
        if cash <= self.balance:
            self.balance -= cash
            print(f'Left : {self.balance}')
            log = int(input('Enter 0 to return back : '))
            if log == 0:
                self.logged()
        else:
            print('You entered more than your balance')
            self.takeCash()

    def logOut(self):
        system('clear')
        print('Good Bye')
        time.sleep(3)
        system('clear')


ATM()
