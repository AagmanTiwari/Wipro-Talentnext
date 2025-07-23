"""
Tech Module: Python Fundamentals
Project: 1

Create a python program that asks the user how far they want to travel. 
If they want to travel less than three miles tell them to ride Bicycle. If 
they want to travel more than three miles, but less than threehundred miles, 
tell them to ride Motor-Cycle. If they want to travel three hundred miles or 
more tell them to driver Super-Car.

Sample Output :
How far would you like to travel in miles? 2500
Output : I suggest Super-Car to your destination

"""

miles = int(input("How far would you like to travel in miles?"))

if miles <= 3:
    print("I suggest you to ride Bicycle")

elif 3 < miles < 300:
    print("I suggest you to ride with Motor-Cycle")

elif 300 <= miles:
    print("I suggest you to drive Super-Car")


'''

project: 2

Let's assume you are planning to use your Python skills to build a PBLApp for 
Mobile.You decide to host your application on servers running in the cloud. You 
pick a hosting providerthat charges $0.51 per hour. You will launch your service
using one server and want to knowhow much it will cost to operate per day,per week,
per month.

Write a Python program that displays the answers to the following questions:

1.How much does it cost to operate one server per day?
2.How much does it cost to operate one server per week?
3.How much does it cost to operate one server per month?
4.How many days can I operate one server with $918?

'''
# Charges by hosting provider for Cost per hour 
costPerHour = 0.51

costPerDay = costPerHour * 24
costPerWeek = costPerDay * 7
costPerMonth = costPerDay * 30 # assuming month is of 30 days
daysWithAmount = 918 / costPerDay

print(f"cost to operate one server per day ${costPerDay}")
print(f"cost to operate one server per Week ${costPerWeek}")
print(f"cost to operate one server per Month ${costPerMonth}")
print(f"cost to operate one server per Month ${costPerMonth}")
print(f"I can operate one server with $918 to {daysWithAmount} days")

