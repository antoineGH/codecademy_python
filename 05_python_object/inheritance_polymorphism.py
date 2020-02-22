# Inheritance
# We can inherit from the original class

class BaseClass:
    pass

class ChildClass(BaseClass):
    pass

# Example

class User:
  is_admin = False
  def __init__(self, username):
    self.username = username

class Admin(User):
  is_admin = True


# Defined User as base class. 
# Created the subclass Admin that inherit from User 
# Admin has the same constructor as User. 
# Only the class variable is_admin is set differently between the two.

# Exceptions
# issubclass() returns True if the first argument is a subclass of the second argument
# issubclass(object, classinfo)

issubclass(Admin, User) # True, Admin is a subclass of User
issubclass(User, Admin ) # False, User is not a subclass of Admin


# Have CandleShop raise your OutOfStock exception when CandleShop.buy() (self.stock[color] < 1

# Define your exception up here:
class OutOfStock(Exception):
    pass

# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] < 1:
        raise OutOfStock
    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

print(issubclass(OutOfStock,Exception))
candle_shop.buy('green')

# Overriding Methods
# An overridden method is one that has a different definition from its parent class

class User:
  def __init__(self, username, permissions):
    self.username = username
    self.permissions = permissions

  def has_permission_for(self, key):
    if self.permissions.get(key):
      return True
    else:
      return False

class Admin(User):
    # Override method 'has_permission_for' with a different definition than 'has_permission_for' for User
  def has_permission_for(self, key):
    return True

# Example 
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text
      
class Admin(User):
  def edit_message(self, message, new_text):
    message.text = new_text

# Super
# The super() builtin returns a proxy object that allows you to refer parent class by 'super'.
# It allows us to invoke a method of an object's parent class
# 

class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    
dog1 = Dog()
# Dog has four legs.
# Dog is a warm-blooded animal.
# Class Dog inherit from Mammal
# Class Dog print "Dog has four legs." and inherit method __init__ from Mammal that prints "is a warm-blooded animal."

# Example 

class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")
    super().__init__(NonWingedMammalName)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")
    super().__init__(NonMarineMammalName)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')

# Dog has 4 legs.
# Dog can't swim.
# Dog can't fly.
# Dog is a warm-blooded animal.
# Dog is an animal.
# Class Dog inherit from NonMarineMammal and NonWingedMammal, that inherit from Mammal that inherit from Animal

# Bat can't swim.
# Bat is a warm-blooded animal.
# Bat is an animal.
# NonMarineMammal inherit from Mammal, that inherit from Animal

Dog.__mro__ # Allows us to check which method is inherited.

# Example 

class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions
    
class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40

# Interface 
# When two classes have the same method names and attributes, we say they implement the same interface.
# Below, Insurance and Vehicle Insurance have the same interface

class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

# Subclass of InsurancePolicy
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001

# Subclass of InsurancePolicy
class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005

# Polymorphism
# Polymorphism : same syntax doing different actions depending on the type of data.

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list)) # >>>  4
print(len(a_dict)) # >>> 2
print(len(a_string)) # >>> 21

# Polymorphism print 4 as four element in the list, 2 as two element in the dictionary and 21 as the 21 letters in the string.

# Dunder Methods

class Atom:
  def __init__(self, label):
    self.label = label
    
  def __add__(self, other):
    return Molecule([self, other])
  
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
        self.atoms = atoms

# Create object from Atom Class
sodium = Atom("Na")
# Create object from Atom Class
chlorine = Atom("Cl")
# Create a list with the two previsously created objects
salt = Molecule([sodium, chlorine])
# Use the __add__ method defined in Atom to use + operator and add objects together
salt = sodium + chlorine

# Dunder 2

class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
    
  def __len__(self):
    return len(self.lawyers)
  
  def __contains__(self, lawyer):
    if lawyer in self.lawyers:
      return True
    else :
      return False
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
print(d_and_p.__len__()) # >>> 2
print(d_and_p.__contains__("Donelli")) # >>> True
print(d_and_p.__contains__("Antoine")) # >>> False

# Review

class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()
    







