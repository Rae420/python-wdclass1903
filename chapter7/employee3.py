class Developer(Employee):
    
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang
        
        
d1 = Developer('Shugbomi', 'Adewale', 1000, 'PHP')        
d2 = Developer('Sam', 'Haruna', 1200, 'Python')

print(d2.salary())
print(d2.full_name())

class Manager(Employee):
    
    def __init__(self, first_name, last_name, pay, prog_lang, employee):
        super().__init__(first_name, last_name, pay, prog_lang)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employee:
            self.employee.remove(emp)
                

    def show_employee(self):
        for emp in self.employee:
            print(emp.full_name())
            

m1 = Manager('Benedict', 'Uwazie', 5000, 'Python', [])
print(m1.salary())
m1.add_emp(d1)
m1.add_emp(d2)
m1.add_emp(d3)
m1.remove_emp(d2)
m1.show_employee()

m2 = Manager('Adebayo', 'Alabi', 10000, 'PHP', [d1, d2, d3])
print('Here are the Developers', m2.last_name, 'is Managing')
m2.show_employee()