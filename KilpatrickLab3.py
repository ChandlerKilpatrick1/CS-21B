
"""
Program 3 : KilpatrickBank
Programmer: Chandler Kilpatrick
Due: 1/28/20
CS 21 B, Winter 2020
Description: This program creates a class BankAccount which can preform several transactions. 
""" 

import KilpatrickBank

account = KilpatrickBank.BankAccount(1000.00)
print("$ " + str(account.get_balance()))

account.deposit(500.00)
print("$ " + str(account.get_balance()))

account.withdraw(2000.00)
print("$ " + str(account.get_balance()))

account.add_interest(0.01, 1)
print("$ " + str(account.get_balance()))

account.add_interest(0.02, 2)
print("$ " + str(account.get_balance()))

account.deposit(125000.99)
print("$ " + str(account.get_balance()))

account.withdraw(0.99)
print("$ " + str(account.get_balance()))

account.withdraw(126500.00)
print("$ " + str(account.get_balance()))

account.withdraw(10.00)
print("$ " + str(account.get_balance()))

account.add_interest(.01, 3)
print("$ " + str(account.get_balance()))








