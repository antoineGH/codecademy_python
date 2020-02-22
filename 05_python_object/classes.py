# Check Variable Type
def check_type(obj):
  print(type(obj))
  
my_dict = {}
my_list = []

check_type(5)
#>>> <class 'int'>
check_type(my_dict)
#>>> <class 'dict'>
check_type(my_list)
#>>> <class 'list'>

# Define a new class 
# pass avoid IndentationError when the body is blank
class ClassName:
	pass

# Instantiation
# A class must be instantiated 
class ClassName :
  pass

object1 = ClassName()
object2 = ClassName()

# Object-Oriented Programming
# A class instance is called an object.
# Instantiation takes a class and turns it into an object

# Print class instantiation
print(type(object1))
# >>> <class '__main__.ClassName'>

# Class Variables
# Class variable are available for each instance of the class. 
# object.variable 

class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# >>> "Rockstar"

# Methods
# Methods are functions that are defined as part of a class. 

class Dog():
  dog_human_year = 7

  # Method takes one argument 'self'
  def time_explanation(self):
    print("Dogs live {} years in 1 human year.".format(self.dog_human_year))

pitbull = Dog()
# Call the .time_explanation() method on our new object 'pitbull'
pitbull.time_explanation()
# >>> "Dogs live 7 years in 1 human year."

# Methods with Arguments
class DistanceConverter:
  kms_in_a_mile = 1.609

  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
kms_in_10_miles = converter.how_many_kms(10)

print(kms_in_5_miles)
print(kms_in_10_miles)

# Example 
class Circle :
  pi = 3.14
  def area(self, radius):
    area = Circle.pi * radius ** 2
    return area
  
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

# Constructors
# Methods that are used to prepare an object being instantiated are called constructors.
# __init__ method is used to initialize a newly created object. It is called every time the class is instantiated.

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)

# Instance Variables
# Class is a schematic for a data type / an object is an instance of a class

class FakeDict:
  pass

# Instantiate two different objects from FakeDict class
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

# Assign instance variables to these objects
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# >>> "This works! This too!"

# Example

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle’s Ices"

print("Object 1:{object1}\nAttribut 'store_name':{attribut1_object1}\nObject 2:{object2}\nAttribut 'store_name':{attribut1_object2}".format(attribut1_object1 = alternative_rocks.store_name, attribut1_object2 = isabelles_ices.store_name, object1 = alternative_rocks , object2 = isabelles_ices))

# Attribute Functions

# The getattr() method returns the value of the named attribute of an object.
# If not found, it returns the default value provided to the function.
# getattr(object, name[, default])

# The hasattr() method returns true if an object has the given named attribute and false if it does not.
# hasattr(object, name)

class Person:
    age = 28
    name = "Antoine"

person = Person()

# Example 1 : getattr() when named attribute is found

print('The age is:', getattr(person, "age"))
# >>> The age is: 28
print('The age is:', person.age)
# >>> The age is: 28

# Example 2 : getattr() when named attribute is not found

# when no default value is provided
print('The sex is:', getattr(person, 'sex'))
# >>> The sex is: AttributeError: 'Person' object has no attribute 'sex'

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))
# >>> The sex is: Male

# Example 3 : hasattr() 

print('Person has age?:', hasattr(person, 'age'))
# >>> True
print('Person has sex?:', hasattr(person, 'sex'))
# >>> False

# Self

class CarBrands:
    def __init__(self, brand, color, horsepower):
        self.brand = brand
        self.color = color
        self.horsepower = horsepower

peugeot_red = CarBrands ("Peugeot car","Red","125CC")
citroen_yellow = CarBrands("Citroen car", "Yellow","200CC")

print(getattr(peugeot_red,"brand", "No Attributes")) # Peugeot car
print(getattr(peugeot_red,"wheels", "No Attributes")) # No Attributes

print(hasattr(peugeot_red, "brand")) # True
print(hasattr(peugeot_red, "wheels")) # False

print(peugeot_red.brand)
print(peugeot_red.color)
print(citroen_yellow.brand)
print(citroen_yellow.color)
print(citroen_yellow.horsepower)
print(citroen_yellow.horsepower)

# Example  

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = diameter / 2
    
  def circumference(self):
    circumference = 2 * Circle.pi * self.radius
    return circumference 
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# Everything is an Object
# dir() function to investigate an object’s attributes

class ClassName:
  pass

object1 = ClassName()
object1.attribute1 = "Attribute1_Value"

dir(object1)
# >>> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
#  '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#   '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute1']

# Python automatically adds a number of attributes to all objects that get created. 
# Our attribute1 is in that list

# String representation 

# __repr__ is a method that gives the string representation of the class to be.
#  __repr__ can only have one parameter, self, and must return a string.

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
    
  def __repr__(self):
    return "Circle with radius {radius}".format(radius = self.radius)
    
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
# Use __init__
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# Use __repr__
print(medium_pizza)
print(teaching_table)
print(round_room)

# Review

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    
  def add_grade(self, grade):
    if type(grade) is Grade:
        self.grades.append(grade)
    
class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
      
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
print(pieter.grades)
