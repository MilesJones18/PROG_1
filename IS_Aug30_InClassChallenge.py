'''Ask user for different expenses, add up the expenses, average them. Print out the average in dollars to 2 decimals and total.'''

car_pay = float(input("What is your montly car payment?: "))
rent = float(input("What is your monthly rent?: "))
phone = float(input("What is your monthly phone payment: "))

total = car_pay + rent + phone
average = total / 3.0

print(f"Your total is: ${total:,.2f}" "\n",f"Your average payment is: ${average:,.2f}" "\n")

