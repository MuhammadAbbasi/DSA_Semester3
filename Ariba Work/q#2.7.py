# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 16:43:36 2018

@author: Dell
"""

class Credit_card:
    def __init__(self,customer,bank,acc,lmt,bal):
        self._customer=customer
        self._bank=bank
        self._acc=acc
        self._lmt=lmt
        self._balance=bal
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_acc(self):
        return self._acc
    def get_limit(self):
        return self._lmt
    def get_bal(self):
        return self._balance
    def charge(self,price):
        if not isinstance(price,(int,float)):
            raise TypeError("the value must be numeric")
        if price+self._balance>self._lmt:
            return False
        else:
            self._balance+=price
            return True
    def make_payment(self,amount):
        if not isinstance(amount,(int,float)):
            raise TypeError("the value must be numeric")
        if amount<0:
            raise ValueError("negative number is not excepted")    
        else:    
            self._balance-=amount
        
if __name__=='__main__':
    wallet=[]
    wallet.append(Credit_card("ariba","hbl",234521,10000,20000))
    wallet.append(Credit_card("ariba","mcb",289521,5000,7000))
    wallet[0].make_payment(100)
    wallet[1].make_payment(2600)
    for val in range(0,2):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
    for c in range (2):
        print ("customer name ",wallet[c].get_customer()," bank ",wallet[c].get_bank()," accountnumber: ",wallet[c].get_acc()," limit is ",wallet[c].get_limit(),"balance is :",wallet[c].get_bal())
      