# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:07:15 2020

@author: elison
"""
AI_NAME = 'Big papi'
username = 'Elison'
trust_level = 0
age = None
gender = None
email=None
bank_account = None

print( f'Hello, {username}, mi name is {AI_NAME}' )

# Change names
answer = input('Would you like to change your user name?(y/n)')
if answer == 'y':
	username = input(f'({username})New Name:')

answer = input(f'Would you like to change my name({AI_NAME})?(y/n)')
if answer == 'y':
	AI_NAME = input(f'({AI_NAME})New Name:')

n
# Ask user input
print("I will ask for some data, leave it blank if you don't want to tell me.")

str_age = input('Age:')
if( str_age != ''):
	trust_level = trust_level + 1
	age = int(str_age)

str_gender = input('Gender(m or f):')
if( str_gender != ''):
	if str_gender == 'm':
		gender = 'Male'
		trust_level = trust_level + 1
	elif str_gender == 'f':
		gender = 'Female'
		trust_level = trust_level + 1
	else:
		print(f'({str_gender}) does not exist in my database ')

str_email = input('E-mail:')
if str_email != '':
	trust_level = trust_level + 1
	email = str_email

# Check for trust level
if trust_level >=2:
	answer = input( 'Can I have your phone number? (y/n)' )
	if answer== 'y':
		trust_level = trust_level + 1
		phone_number = input( 'Phone number:' )

if trust_level >=3:
	answer = input( 'Can I have your bank account? (y/n)' )
	if answer== 'y':
		trust_level = trust_level + 1
		bank_account = input( 'Account number:' )

# Selection of the response
if trust_level < 3:
	print( f'Well I cannot work like this {username}. Come again when you are not so paranoic')
elif trust_level <5:
	print( f"That's all, {username}. I look forward to work with you.")
else:
	# Trust level is high
	print( f"Thank you master {username}. Please let me know if you need anything, anytime." )
	print( '...')

# Internal configuration
print('--------------------------------')
print( f"{AI_NAME}'s configuration" )
print('--------------------------------')
if gender != None:
	if gender =='Male':
		print( 'TODO: Ask for favorite beard length' )
	elif gender =='Female':
		print( 'TODO: Ask for favority hair length' )
if age != None and age < 17:
	print( 'REPORT USE TO: Contacts MOM and DAD ' )

if bank_account != None:
	print( 'WATCH: Autopayment options for services' )
