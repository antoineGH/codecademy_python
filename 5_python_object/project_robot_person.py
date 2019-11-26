# https://www.youtube.com/watch?v=WOwi0h_-dfA

class Person():
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting 

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False

class Robot():
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        
    def introduce_self(self):
        print("My name is {name}".format(name = self.name))

r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)

dir(r1)
print(getattr(r1, "name"))
print(getattr(r1, "color"))
print(getattr(r1, "weight"))

dir(r2)
print(getattr(r2, "name"))
print(getattr(r2, "color"))
print(getattr(r2, "weight"))


def get_attributes(object):
    list_attribute = dir(object)
    for attribute in list_attribute:
        if attribute.count("_") == 0:
            print(attribute)

def print_attributes(object):
    list_attribute = dir(object)
    print("Class {object} -".format(object = object))
    for attribute in list_attribute:
        if attribute.count("_") == 0:
            print("{attribute}: {attribute_value}".format(attribute = attribute, attribute_value = getattr(object, attribute)))

get_attributes(r1)
get_attributes(r2)
print_attributes(r1)
print_attributes(r2)

r1.introduce_self()
r2.introduce_self()

p1 = Person("Alice", "agressive", False)
p2 = Person("Becky", "talkative", True)

p1.owned_robot = r2
p2.owned_robot = r1
p1.owned_robot.introduce_self()
p2.owned_robot.introduce_self()

get_attributes(p1)
get_attributes(p2)
print_attributes(p1)
print_attributes(p2)

dir(p1)


