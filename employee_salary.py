e_name=input("Enter the name of Employee \n")
c_name=input("Enter the company name \n")
salary=float(input("Enter the salary of Employee \n"))
if(salary>50000):
 tax=0.15*salary
 netsalary=salary-tax
 print("The net salary of "+e_name+" worked in " +c_name+ " is",netsalary)
else:
 netsalary=salary
 print("No taxalbe Amount")
 print("The net salary of "+e_name+" worked in " +c_name+ " is",salary)
