salary = float(input("Enter the base salary:"))

if salary < 10000:
    hra = (67/100)*salary
    da = (73/100)*salary
elif salary < 20000:
    hra = (69/100)*salary
    da = (76/100)*salary
else:
    hra = (73/100)*salary
    da = (89/100)*salary
gs = hra+da+salary
print("Gross Salary:",gs)