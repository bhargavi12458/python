class BankAccount:
    def_init_(self,account_number,balance):
        self._account_number=account_number
        self._balance=balance
        defget_account_number(self):
            return self._account_number
        def get_balance(self):
            return self._balance
        def deposite(self,amount):
            if amount>0:
                self._balance+=amount
                print("deposite successful.")
                else:
                    print("invalid amount for deposit.")
                    def withdraw(self,amount):
                        if amount>0 and amount<=self._balance:
                            self._balance-=amount
                            print("withdrawal successful.")
                            else:
                                print("insufficient funds or invalid amount for withdrawal.")
                                account=BankAccount("1234567890",1000)
                                print("Account Number:",account.get_account_number())
                                print("Balance:",account.get_balance())
                                account.deposite(500)
                                account.withdraw(200)
                                account._account_number="9876543210"
                                account._balance=5000
                                print("Account Number:",account.get_account_number())
                                print("Balance:",account.get_balance())
                                
