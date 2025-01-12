print("\t\tINCOME TAX CALCULATOR\n")
total_income=int(input("Enter the total income earned: "))
deduction=int(input("Enter the total deduction: "))
tax_income=total_income-deduction
print("\n Taxable income : ",tax_income)

if(tax_income<=300000):
    income_tax=0
elif(300000<tax_income<=700000):
   income_tax = (tax_income - 300000) * 0.05
elif tax_income <= 1000000:
    income_tax = 20000 + (tax_income - 700000) * 0.10
elif tax_income <= 1200000:
    income_tax = 50000 + (tax_income - 1000000) * 0.15
elif tax_income <= 1500000:
    income_tax = 80000 + (tax_income - 1200000) * 0.20
else:
    income_tax = 140000 + (tax_income - 1500000) * 0.30  

print(f" The required tax is: {income_tax:.3f}")

