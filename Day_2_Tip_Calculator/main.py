print("Welcome to the Tip Calculator!")

totol_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

number_of_split = int(input("How many people to split the bill? "))

tip_rate = 1 + tip_percentage/100

payable_amount  = (totol_bill/number_of_split) * tip_rate

payable_amount = "{:.2f}".format(payable_amount)

print(f"Each person should pay: ${payable_amount}")
