salary = float(input("enter the Salary"))
bill1 = float(input("amount for bill1"))
bill2 = float(input("amount for bill2"))
bill3 = float(input("amount for bill3"))
total_bill = bill1 + bill2 + bill3
print("Total bill" ,total_bill)
per = (total_bill/salary)*100
print(per,"%")