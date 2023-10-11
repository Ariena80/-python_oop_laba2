class Employee:
    pass

employee1 = Employee()
employee1.name = 'John'
employee1.salary = 8000

employee2 = Employee()
employee2.name = 'Arina'
employee2.salary = 18000

employee3 = Employee()
employee3.name = 'Vlad'
employee3.salary = 6000

total_salary = employee1.salary + employee2.salary + employee3.salary
print("Сумма зарплат работников:", total_salary)