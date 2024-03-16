from atm_balance import balance
from login import login

class atm:
    def __init__(self):
        self.obj = balance()
        self.transactions = [0,0,0]
    def card(self):
        while True:
            self.c = int(input("Please select a card of your choice from below-\n 1.RuPay\n 2.VISA\n 3.MasterCard\n"))
            if self.c == 1 or self.c == 2 or self.c == 3:
                self.obj = login()
                break

    def options(self):
        while True:
            o = int(input("Please select an action to perform from below-\n 1.Check Balance\n 2.Withdraw Cash\n 3.Cash Deposit\n 4.Last 3 transactions Mini Statements\n"))
            if o == 1 or o == 2 or o == 3 or o == 4:
                if o == 1:
                    self.check_balance()
                    break
                elif o == 2:
                    while True:
                        self.withdrawl = int(input('Enter the withdrawal amount: '))
                        
                        if self.c == 1:
                            if self.withdrawl <= 2000:
                                self.check_balance(self.withdrawl)
                                break
                            else:
                                print('You have crossed your transaction limit')
                        elif self.c == 2:
                            if self.withdrawl <= 5000:
                                self.check_balance(self.withdrawl)
                                break
                            else:
                                print('You have crossed your transaction limit')
                        elif self.c == 3:
                            if self.withdrawl <= 8499:
                                self.check_balance(self.withdrawl)
                                break
                            else:
                                print('You have crossed your transaction limit')
                    break
                elif o==3:
                    self.deposit=int(input('Enter the deposit amount: '))
                    self.check_balance(self.deposit)
                    break
                elif o==4:
                    print("Last 3 transactions Mini Statements:")
                    for transaction in self.transactions[-3:]:
                        print(transaction)
                    break
            else:
                pass

    def check_balance(self,withdrawl=0,deposit=0):
        bal = 100000
        bal=bal-withdrawl
        bal=bal+deposit
        print('The remaining balance is: ', bal)
        self.transactions.append(('Check Balance',withdrawl,deposit,bal))


obj = atm()
obj.card()
obj.options()
