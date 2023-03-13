# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:00:36 2023

@author: elift
"""
from pizza_choosing import *
from sauce_choosing import *
import csv
import datetime
import pandas as pd


def menu() :
    print("\nPİZZA SİPARİŞ SİSTEMNE HOŞGELDİNİZ\n\n      ")
    with open("menu.txt" , "r",encoding="utf-8") as menu:
        print(menu.read())


def main():
    menu()


    pizza_choice = int(input('\nLütfen istediğiniz pizzanın numarası giriniz: ')) #Kullanıcıdan alınan input'u pizza_choice değerine atıyoruz

    pizza = None # Pizza değişkeni oluşturuyoruz

    if pizza_choice == 1: # Kullanıcının girdiği değere göre alt sınıfları çalıştırıyoruz.
        pizza = ClassicPizza()
    elif pizza_choice == 2:
        pizza = MargaritaPizza()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    elif pizza_choice == 4:
        pizza = ItalyanPizza()
    else:
        print("Lütfen geçerli bir pizza numarası giriniz")
    
    sauce_choice=None
    
    sauce_choice = int(input('Pizzanızın üzerine ilave eklemek istediğiniz sosu seçiniz: ')) # Kullanıcının sos seçmesini istiyoruz.
    
    if sauce_choice == 11:
        pizza = Zeytin(pizza)
        
    elif sauce_choice == 12:
        pizza = Mantar(pizza)
    elif sauce_choice == 13:
        pizza = KeciPeyniri(pizza)
    elif sauce_choice == 14:
        pizza= Et(pizza)
    elif sauce_choice == 15:
        pizza = Sogan(pizza)
    elif sauce_choice == 16:
        pizza = Misir(pizza)
    else :
        print("geçersiz seçim")
    
    
    print("**********************************************")
    print("Seçilen pizza numarası: " , pizza_choice)
    print("Toplam ödecek tutar" ,pizza.get_cost()) 
    
    print("***********************************************")
    if input("Siparişi Onaylıyor Musunuz? Evet/Hayır\n").lower()=="evet":
    
        name=input("İsminizi Giriniz:")
        tc_no=input("TC Kimlik Numarası Giriniz:")
        card_number=input("Kart Numaranızı Giriniz:")
        card_pin=input("Kart Şifrenizi Giriniz:")
        order={
            "Username":name,
            "TC":tc_no,
            "Card Number":card_number,
            "Order Description":pizza.get_description(),
            "Order Time":datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Card Pin":card_pin
        }
        with open('Orders_Database1.csv', mode='a', newline='') as file:
            filednames=['Username','TC','Card Number','Order Description','Order Time','Card Pin']
            writer=csv.DictWriter(file,fieldnames=filednames)
            writer.writerow(order)
        print("İyi günler başka bir gün görüşmek üzere!")
    else:
        print("İyi günler başka bir gün görüşmek üzere!")
    

if __name__ == "__main__":
    main()
