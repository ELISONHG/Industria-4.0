# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:29:30 2020

@author: elison
"""
print("Welcome to the hospital")
Base_NAME = "DR Elison"
username = None 
age = None
address = None
gender = None
weight= None
size = None
height = None
security_number = None
print("what is your name?")
username= input (f"{username}")
print( f'Hello {username}, my name is {Base_NAME}' )

print("perfect, we will create health register") 
answer = input("what is your age?")
age= input(f"({age})")
answer = input("what is your address?")
address= input(f"({address})")
answer = input("what is your gender?")
gender= input(f"({gender})")
answer = input("Can you tell me your weight?(y/n)")
if answer == "y":
    weight= input(f"({weight})New weight:")
answer = input("Can you tell me your size?(y/n)")
if answer == "y":
    size= input(f"({size})New size:")
answer = input("Can you tell me your height?(y/n)")
if answer == "y":
    height= input(f"({height})New height:")
answer = input("what is your security_number?")
security_number= input(f"({security_number})")
print("perfect")
print("Thank you for creating your registration")

print("Good bye.")
