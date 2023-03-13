# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:45:22 2023

@author: elift
"""
from pizza_choosing import *

class Decorator:
    def __init__(self, component):
        self.component = component
        
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return Pizza.get_description(self) + ' ' + self.component.get_description()

class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.component = component
        self.description = "Zeytin"
        self.cost = 10
        
class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mantar"
        self.cost = 10

class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Keçi Peyniri"
        self.cost = 15
        
class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Sogan"
        self.cost = 5


class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Et"
        self.cost = 20


class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mısır"
        self.cost = 5

"""
s1=Zeytin(Pizza)
print(s1)
"""