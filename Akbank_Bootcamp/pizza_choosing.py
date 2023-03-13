# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:09:08 2023

@author: elift
"""

class Pizza:
    def __init__(self,description,cost):
        self.description=description
        self.cost=cost
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
#Özel Sbarro® hamuru üzerine nefis Sbarro pizza sosu, mozzarella peyniri, kekik!
    
class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza'nın Standart Malzemeleri: Domates sosu, Zeytin, Biber, Mısır"
        super().__init__(self.description, 100)
        #print(f"\n{self.description} \nPizza fiyatı:{self.cost}" )
        print(f"\n{self.description} ")
        
class MargaritaPizza(Pizza):
    def __init__(self):
        self.description = "Margarita Pizza'nın Standart Malzemeleri:  pizza sosu, mozzarella peyniri,parmesan peyniri, kekik!"
        super().__init__(self.description, 120)
        #print(f"\n{self.description} \nPizza fiyatı:{self.cost}" )
        print(f"\n{self.description} ")
        
        
class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Türk Pizza'nın Standart Malzemeleri: pizza sosu, mozzarella peyniri, sucuk, sosis, pepperoni, mısır, siyah zeytin"
        super().__init__(self.description, 140)
        #print(f"\n{self.description} \nPizza fiyatı:{self.cost}" )
        print(f"\n{self.description} ")
        
class ItalyanPizza(Pizza):
    def __init__(self):
        self.description = "İtalyan Pizza'nın Standart Malzemeleri: Mozzarella peyniri, sosis parçaları, özel tarifimize göre hazırlanmış pepperoni ve parmesan peyniri."
        super().__init__(self.description, 140)
        #print(f"\n{self.description} \nPizza fiyatı:{self.cost}" )
        print(f"\n{self.description} ")
 
"""       
p1=TurkPizza()
print(p1.get_cost())
"""















