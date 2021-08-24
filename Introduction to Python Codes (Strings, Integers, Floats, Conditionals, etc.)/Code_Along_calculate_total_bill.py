"""Write code that calculates the total bill at a restaurant (meal + tax + tip).

1. Prompt the user for the bill amount, the sales tax, and the tip percentage.
2. Print out the total bill amount in the format: "The total bill is $..."
3. Make sure to apply the tip after you add the tax amount.
4. Round the total bill amount to 2 decimal places."""

#Create variable that prompt the user for the appropriate info. cast as floats.

bill = float(input("How much is the meal? "))
tax = float(input("What is the sales tax rate percentage? "))
tip = float(input("Enter the tip amount (as a percentage): "))

#Calculate total with tax 
tax_amount = (bill * tax) / 100
total = bill + tax_amount
#Calculate and add tip
tip_amount = (total * tip) / 100
total = total + tip_amount
#round the total to two decimal places
total = round(total, 2)
print("The total bill is $", total, sep = '')
#use the seperator arugment to remove the space between the end of the string and the variable.
