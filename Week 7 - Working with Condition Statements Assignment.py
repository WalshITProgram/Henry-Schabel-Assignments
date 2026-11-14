
    
  
#1:
employee_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False, 
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

#2 and 3:
employee_numbers = []
employee_names = []
hourly_wages = []

for value in employee_data:
    if type(value) is int:
        if value not in employee_numbers:
            employee_numbers.append(value)
    elif type(value) is str:
        if value not in employee_names:
            employee_names.append(value)
    elif type(value) is float:
        if value not in hourly_wages:
            hourly_wages.append(value)

print("Employee numbers:")
print(employee_numbers)

print("Employee names:")
print(employee_names)

print("Hourly wages:")
print(hourly_wages)

#4:
total_hourly_rate = []

for wage in hourly_wages:
    total_rate = wage * 1.3
    total_hourly_rate.append(total_rate)

print("Total hourly rates:")
print(total_hourly_rate)

maximum_rate = max(total_hourly_rate)

if maximum_rate > 37.30:
    print("WARNING: Someone's salary may be a budget concern.")

#5:
underpaid_salaries = []

for rate in total_hourly_rate:
    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

print("Underpaid salaries:")
print(underpaid_salaries)

#6:
company_raises = []

for wage in hourly_wages:
    if wage >= 22 and wage < 24:
        new_wage = wage * 1.05
    elif wage >= 24 and wage < 26:
        new_wage = wage * 1.04
    elif wage >= 26 and wage < 28:
        new_wage = wage * 1.03
    else:
        new_wage = wage * 1.02

    company_raises.append(new_wage)

print("Company raises:")
print(company_raises)

#7:
if len(employee_numbers) >= 5 and len(employee_names) >= 5 and len(hourly_wages) >= 5 and maximum_rate > 37.30:
    print("The employee data meets all four conditions.")

