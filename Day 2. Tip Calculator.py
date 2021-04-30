print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?: "))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15?: "))
people = float(input("How many people to split the bill?: "))
payment = total_bill * (100 + percent) / 100 / people
print(f"Each person should pay: ${payment:.2f}")
