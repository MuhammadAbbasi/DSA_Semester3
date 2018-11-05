# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:47:41 2018

@author: Family
"""

class CreditCard:
    def __init__(self,customer,bank,acc,lmt):
        self._customer=customer
        self._bank=bank
        self._acc=acc
        self._lmt=lmt
        self._balance=0
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._acc
    def get_limit(self):
        return self._lmt
    def get_balance(self):
        return self._balance
    def charge(self,price):
        if not isinstance(price,(int,float)):
            raise TypeError("the value must be numeric")
        if price+self._balance>self._lmt:
            return False
        else:
            self._balance+=price
            print("now your balance is :",self._balance )
            return True
    def make_payment(self,amount):
        if not isinstance(amount,(int,float)):
            raise TypeError("the value must be numeric")
        else:    
            self._balance-=amount
            print("now your balance is= ",self._balance)
        
if __name__=='__main__':
    wallet=[]
    wallet.append(CreditCard( 'John Bowman' , 'California Savings' , '5391 0375 9387 5309' , 2500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Federal' , '3485 0399 3395 1954' , 3500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Finance' , '5391 0375 9387 5309' , 5000) ) 
    for val in range(1, 3):
        wallet[0].charge('val')
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    for c in range(3):
        print( 'Customer = ', wallet[c].get_customer())
        print( 'Bank = ', wallet[c].get_bank())
        print( 'Account =' , wallet[c].get_account())
        print( 'Limit =' , wallet[c].get_limit())
        print( 'Balance =' , wallet[c].get_balance()) 
