# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:16:41 2018

@author: Dell
"""

class Flower:
    def __init__(self,name,petal,price):
        self._name=name
        self._petal=petal
        self._price=price
        
    def _get_name(self):
        self._name=str(input("enter the name of flower"))
        return self._name
    def get_petal(self):
        self._petal=int(input("enter the number of petals of flower"))
        return self._petal
    def get_price(self):
        self._price=float(input("enter the price of flower"))
        return (self._price)
    def Return_value(self):
        print(Flower._get_name(self),Flower.get_petal(self),Flower.get_price(self))

a=Flower("jasmine",2,3.5)
a.Return_value()