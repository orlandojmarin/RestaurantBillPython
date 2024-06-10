# Write a program that computes the tax and tip on a restaurant bill. The
# program should ask the user to enter the charge for the meal. The tax should
# be 6.75 percent of the meal charge. The tip should be 20 percent of the total 
# after adding the tax. Display the meal charge, tax amount, tip amount, and
# total bill on the screen.

# variables
tax_percentage = 0.0675
tip_percentage = 0.20

# ask user for the meal price
meal_price = float(input("How much did your meal cost?\n"))

# calculate the tax, which is 6.75% of the meal charge
meal_tax = meal_price * tax_percentage

# calculate the meal total, which is the meal price plus the meal tax
meal_total = meal_price + meal_tax

# use the meal total to calculate a 20% tip
meal_tip = meal_total * tip_percentage

# calculate the total bill
total_bill = meal_total + meal_tip

# print the results
print(f"The meal price is ${meal_price:.2f}")

print(f"The tax on the meal is ${meal_tax:.2f}")

print(f"The tip for the meal is ${meal_tip:.2f}")

print(f"The total bill is ${total_bill:.2f}, Orlando! We take credit cards and Venmo!")

