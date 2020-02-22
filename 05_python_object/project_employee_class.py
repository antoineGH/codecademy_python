# https://www.youtube.com/watch?v=rq8cL2XMM5M

class Employee:
    instanced_count = 0
    annual_raise = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.pay = pay
        self.mail = first.lower() +"."+ last.lower()+"@gmail.com"
        Employee.instanced_count += 1

    def full_name(self):
        return "First Name: {}\nLast Name: {}\nMail: {}\nPay: {}".format(self.first, self.last, self.mail, self.pay)

    def apply_raise(self):
        self.pay = self.annual_raise * self.pay 

    # Define a Class Method to apply the method on the class itself not on the instance
    @classmethod
    def set_annual_raise(cls, amount):
        cls.annual_raise = amount

    # Alternative Constructors from string
    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split("-")
        return cls(first, last, pay)

emp_1 = Employee("bastien", "ratat", 20000)
emp_2 = Employee("antoine", "ratat", 30000)
emp_3 = Employee("catherine", "ratat", 50000)

emp_str_4 = "martin-licis-5000"
emp_str_5 = "thor-ragnarok-2000"
emp_str_6 = "kevin-durand-6000"

emp_4 = Employee.from_string(emp_str_4)
emp_5 = Employee.from_string(emp_str_5)
emp_6 = Employee.from_string(emp_str_6)

# Set annual raise variable with a class method applied on Employee
Employee.set_annual_raise(1.05)

print(emp_1.full_name())
print(emp_2.full_name())
print(emp_3.full_name())
print(emp_4.full_name())
print(emp_5.full_name())
print(emp_6.full_name())

print(Employee.instanced_count)

print(emp_1.pay)
print(emp_2.pay)
print(emp_3.pay)

emp_2.annual_raise = 10.80

emp_1.apply_raise()
emp_2.apply_raise()
emp_3.apply_raise()

print(emp_1.pay)
print(emp_2.pay)
print(emp_3.pay)

print(Employee.__dict__)
print(emp_1.__dict__) # Doesn't contain annual_raise attribute (use the one defined in the class)
print(emp_2.__dict__) # Contains annual_raise attribute (use the one defined in the object prior to the one define in the class)
