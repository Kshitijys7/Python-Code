Eid=int(input('Ennter employee id:'))
Ename=input('Enter employee name:')
Esalary=int(input('Enter employee salary:'))
Bonus=int(input('Enter the monthly bonus:'))

Gross_Salary=Esalary+Bonus

if(Esalary<10000):
    Tax_perct=0
    Tax=0
    Net_Salary=Gross_Salary

elif(Esalary>10000 and Esalary<=20000):
    Tax_perct=5
    Tax=(5/100)*Esalary
    Net_Salary=Gross_Salary-Tax

elif(Esalary>20000 and Esalary<=30000):
    Tax_perct=10
    Tax=(10/100)*Esalary
    Net_Salary=Gross_Salary-Tax

print('Employee id:',Eid)
print('Employee name:',Ename)
print('Employee salary:',Esalary)
print('Employee bonus:',Bonus)
print('Employee Monthly Tax percentage:',Tax_perct)
print('Employee Monthly Tax:',Tax)
print('Employee Gross Salary',Gross_Salary)
print('Employee Net Salary',Net_Salary)

print('Employee id\t\tEmployee name\t\tEmployee salary\t\tMonthly bonus\t\tTax perct\t\tMonthly Tax\t\t\tGross Salary\t\t\tNet Salary')
print({Eid},'\t\t\t',{Ename},'\t\t\t',{Esalary},'\t\t\t',{Bonus},'\t\t\t',{Tax_perct},'\t\t\t',{Tax},'\t\t\t',{Gross_Salary},'\t\t\t',{Net_Salary})