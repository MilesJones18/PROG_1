# Sentinal Values
patients_weight = int(input("Please enter your weight: "))
num_of_patients = 1
total = 0
while (patients_weight != 0):
    total = total + patients_weight
    print(f"The average of the patients weight is: {total/num_of_patients}")
    num_of_patients += 1
    patients_weight = int(input("Please enter the weight of the next patient or 0 for no more patients: "))


# Using loops for input validation.

hours_worked = int(input("Enter the number of hours worked: "))
hourly_pay = int(input("Enter your hourly pay rate: "))

while(hours_worked < 0):
    print("Error: You cannot work negative hours.")
    hours_worked = int(input("Enter the number of hours worked"))

total = hours_worked * hourly_pay
print(f"Your gross pay for the week is: ${total:,.2f} US Dollars")


# Using the walrus operator to place it on one line

while (score := int(input("Enter your score from 0-100: "))) < 0:
    print("A score cannot be negative")


# Nested loops

for i in range(0, 10):
    print(f"The value of i is: {i} \n")
    for j in range(1, 5):
        print(f"The value of j is: {j} \n")
        for k in range(2, 15):
            print(f"The value of k is: {k}")