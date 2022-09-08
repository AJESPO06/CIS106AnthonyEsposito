# This program calculates the Weekly, Monthly, and Annual Gross Pay
print("Enter hours worked", end='', flush=True)
hoursWorked = int(input())
print("Enter hourly wage")
hourlyWage = int(input())
weeklyPay = hourlyWage * hoursWorked
monthlyPay = hourlyWage * hoursWorked * 4
annualPay = hourlyWage * hoursWorked * 52
print("Weekly pay is " + str(weeklyPay), end='', flush=True)
print(" Monthly pay is " + str(monthlyPay))
print("Annual pay is " + str(annualPay))
