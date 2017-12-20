#Create a program that lets the user input their total bill at a restaurant, and returns the total cost of the bill including a tip. Use 15% of the total bill as the tip calculation.
#For example, if the total bill is KSh 1000, the tip is 0.15 * 1000 = KSh 150, so the total cost of the bill returned to the user is 1000 + 150 = KSh 1150.
#Once you're finished, take this a step further and let the user enter their level of satisfaction with their service and factor that value into the tip percentage. For example, if they received good service, the tip is 15%; great service is 20%; terrible service is 0%.

print("Total Bill?")
bill = float(input())

tip = 0.15 * bill

print(bill+tip)
