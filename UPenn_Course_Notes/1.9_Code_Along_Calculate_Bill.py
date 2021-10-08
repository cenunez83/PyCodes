"""Write code to calculate the total bill at a restaurant (meal + tax + tip)

1. Prompt the user for the bill amount, the sales tax, and the tip percentage.
2. Print out the total bill amount in the format: "The total bill is $..."

Make sure you: 

3. Apply the tip after you add the tax amount.
4. Round the total bill amount to two decimal places. 

For example: 
The meal is $30; the sales tax is 6%; the tip is 18%. This should print "The total bill is $37.52" """

#Prompt for meal amount, tax, and tip.
bill = float(input("What is the meal amount?"))
tax = float(input("What is the sales tax (as a percentage)?"))
tip = float(input("What tip amount would you like to leave (as a percentage)?"))

#Calculate and add tax
tax_amount = (bill * tax) / 100

#Calculate and add tip 
tip_amount = ((bill + tax_amount) * tip) / 100

#calculate total bill
total = bill + tax_amount + tip_amount 
total = str(round(total, 2))


#print the final bill
print("The total bill is $" + total)

#OR you can leave the total as a float:

bill = float(input("What is the meal amount?"))
tax = float(input("What is the sales tax (as a percentage)?"))
tip = float(input("What tip amount would you like to leave (as a percentage)?"))

#Calculate and add tax
tax_amount = (bill * tax) / 100

#Calculate and add tip 
tip_amount = ((bill + tax_amount) * tip) / 100

#calculate total bill
total = bill + tax_amount + tip_amount 
total = round(total, 2)


#print the final bill
print("The total bill is $" , total) #this prints a space between the dollar sign and the value. 
print("The total bill is $" , total, sep = '') #this removes the space.