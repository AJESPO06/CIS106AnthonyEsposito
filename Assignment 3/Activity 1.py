# This program calculates the Weekly, Monthly, and Annual Gross Pay
# References:
# References go here ...
print("Enter hours worked", end='', flush=True)
hoursWorked = float(input())
print("Enter hourly wage")
hourlyWage = float(input())
weeklyPay = hourlyWage * hoursWorked
monthlyPay = hourlyWage * hoursWorked * 4
annualPay = hourlyWage * hoursWorked * 52
print("Weekly pay is " + str(weeklyPay), end='', flush=True)
print(" Monthly pay is " + str(monthlyPay))
print("Annual pay is " + str(annualPay))
