# receive inputs for total bill and tip percentage
import pyfiglet
server = input("Enter Server's name: ")
meal_price = float(input("Enter your meal amount: "))
tip = int(input("Enter Your tip %: "))
# tax percentage
tax = .06
# Calculation of meal, tip and tax
tip_amt = meal_price * tip / 100
tax_amt = meal_price * tax
total = meal_price + tip_amt + tax_amt

# now ouput the results
print(pyfiglet.figlet_format("Tip Calculator", justify = "center"))
print(pyfiglet.figlet_format("By: Aliyanna", justify = "center"))
print(f" The server is "+ server )
print(f" Your meal is ${meal_price:.2f}")
print(f" Your tip is ${tip_amt:.2f}.")
print(f" Your total with tax is {total:.2f}")