import random

class bank:
    name = []
    sign = []
    pas = []
    balance = 0
    acc_no = []
    no_of_transactions = 0
    
    def open_account(self):
        self.username = input('Name: ')
        obj.name.append(self.username)
        self.address = input('Address: ')
        self.signature = input('Sign: ')
        obj.sign.append(self.signature)
        self.password = input('Password: ')
        obj.pas.append(self.password)
        self.account_no = random.randrange(10000,99999)
        obj.acc_no.append(self.account_no)
        print('\nAccount created successfully\n'
              'Account no. is',self.acc_no)
        print('Minimumm balance to be maintained is Rs. 5000\n')
               
    def deposit_money(self):
        ac = int(input('A/C no.: '))
        if ac in obj.acc_no:
            am = int(input('Amount: '))
            v = input('Password: ')
            if v in obj.pas:
                obj.balance += am
                obj.no_of_transactions += 1
                print('A/C no.',obj.acc_no,'credited by ₹',am)
                print('A/C bal: ₹',obj.balance)
            else:
                print('Invalid password!')
        else:
            print('Please open an account first!')
            
    def withdraw_money(self):
        q = int(input('A/C no.: '))
        if q in obj.acc_no:
            l = int(input('Amount: '))
            w = input('password: ')
            if w in obj.pas:
                subtract = obj.balance - l
                try:
                    if subtract < 5000:
                        print(int(a))
                    else:
                        obj.balance -= l
                        obj.no_of_transactions +=1
                        print('A/C no.',obj.acc_no,'debited by ₹',l)
                        print('A/C bal: ₹',obj.balance)
                except:
                    amt = obj.balance - 5000
                    print('Minimum Balance!')
                    print('A/C bal: ₹',obj.balance)
                    print('You can withdraw only ₹',amt)            
            else:
                print('Invalid password!')
        else:
            print('Please open an account first!')
        
    def change_name(self):
        y = input('Existing name: ')
        if y in obj.name:
            z = input('New name: ')
            u = input('Password: ')
            if u in obj.pas:
                obj.name = z
                print('Successfully changed the owner name.')
            else:
                print('Invalid password!')
        else:
            print('Invalid username!')

    def trans_bal(self):
        print('No. of transactions are',obj.no_of_transactions,'& closing balance is ₹',obj.balance,'\n')

obj = bank()
   
while True:
    print('\n1. Open a Bank Account\n'
      '2. Perform transaction for an account\n'
      '3. Exit the application\n')
    
    n = input('Main-menu choice: ')

    if n == '1':    
        obj.open_account()
        
    elif n == '2':
        print('\n')
        while True:
            
            print('1. Deposit money\n'
                  '2. Withdraw money\n'
                  '3. Change name\n'
                  '4. Display number of transaction & closing balance\n'
                  '5. Exit sub-menu\n')
            
            p = int(input('Sub-menu choice: '))
        
            if p == 1:
                obj.deposit_money()
            elif p == 2:
                obj.withdraw_money()
            elif p == 3:
                obj.change_name()
            elif p == 4:
                obj.trans_bal()
            elif p == 5:
                break
            else:
                print('Wrong input!')
            
    elif n == '3':
        print('Do you want to exit the application?\n')
        i = input('yes/no: ')
        if i == 'y' or i == 'yes':
            break
        elif i == 'n' or i == 'no':
            pass
        else:
            print('Wrong input!')
    else:
        print('Wrong input!')
    
    

