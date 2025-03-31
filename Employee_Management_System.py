from abc import ABC, abstractmethod 

class Employee(ABC):
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self._name=name
        self.__salary=salary

    @abstractmethod        
    def calculate_salary(self):
        pass
    def get_salary(self):
        return self.__salary
    
class Manager(Employee):
    def __init__(self, emp_id, name, salary,department):
        super().__init__(emp_id, name, salary)
        self.department=department

    def calculate_salary(self):
        return self.get_salary()+5000 #bonus
    
    def display(self):
        return f'Manager: {self._name} (ID: {self.emp_id}) - Salary: {self.get_salary()} - Department: {self.department}  '
    
class Company:
    def __init__(self):
        self.employees={}
    
    def add_employees(self,employee):
        self.employees[employee.emp_id]=employee

    def get_employees(self,emp_id):
        try:
            print(f"\nFetching details for Employee ID: {emp_id}...")
            input("\nPress Enter to continue...")     
            return f'Employee: {self.employees[emp_id]._name}, Salary: {self.employees[emp_id].calculate_salary()}'
        except KeyError:
            return 'Employee not found!'
        finally:
            print("Employee Search completed")

    def __del__(self):
        print(f'Company instance deleted!')

company=Company()

input("\nPress Enter to create employees...")
emp1 = Manager(101, "Alice", 50000, "HR")
emp2 = Manager(102, "Bob", 75000, "IT")
emp3 = Manager(103, "John", 85000, "Finance")

input("\nPress Enter to add employees to company...")
company.add_employees(emp1)
company.add_employees(emp2)
company.add_employees(emp3)

print(company.get_employees(101)) 
print(company.get_employees(999))  

input("\nPress Enter to continue for Manager details...")
print(emp2.display())
print(emp3.display())

input("\nPress Enter to exit...")