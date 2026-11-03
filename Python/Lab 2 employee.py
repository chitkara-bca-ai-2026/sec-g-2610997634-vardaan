name=input("enter employe name")
id=int(input("enter employe id "))
salary=float(input("enter employe salary"))
department=input("enter departmemt")
active=input("is the employee active ? (yes or no):") == "yes"
is_active = active=="yes"
print("Name:",name)
print("ID:",id)
print("Salary:",salary)
print("Department:",department)
print("Active:",active)