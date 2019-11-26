import math 

### CLASS DECLARATION ---

class Package:
    def __init__(self, nb_class, promotion=0):
        self.nb_class = nb_class
        coeff = (100 - promotion)/100
        if nb_class == 32:
            self.package_name = "Full Package"
            self.price = 180 * nb_class * coeff
        elif nb_class == 16:
            self.package_name = "Half Package"
            self.price = 200 * nb_class * coeff
        else:
            print("Number of class should be 16 or 32")

    def __str__(self):
        return "{} for {} classes, price : {}".format(self.package_name, self.nb_class, self.price)

class Class:
    def __init__(self, class_name, start_time, end_time, location):
        self.class_name = class_name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.students = {}

    def __str__(self):
        return "{}, from {}:{} to {}:{} in {}.\nStudent List : {}".format(self.class_name, str(self.start_time)[:2], str(self.start_time)[2:], str(self.end_time)[:2], str(self.end_time)[2:], self.location, str(self.students.keys())[9:])

    def add_student(self, student):
        self.students[student.name]= student

    def remove_student(self, student):
        self.students.pop(student.name, None)

    def display_students(self):
        students_name = []
        for value in self.students.values():
            students_name.append(value.name)
        return students_name

    def total_classes(self):
        total_classes = 0
        for value in self.students.values():
            total_classes += value.package.nb_class
        return total_classes
        
    def age_average(self):
        count = 0
        sum_age = 0
        for value in self.students.values():
            sum_age += value.age
            count += 1
        age_average = sum_age / count
        return age_average
        
    def total_money(self):
        total_money = 0
        for value in self.students.values():
            total_money += value.package.price
        return total_money

    def total_per_class(self):
        count = 0
        for value in self.students.values():
            count += 1
        #total_per_class = self.total_money()/32
        total_per_class = self.total_money()/(self.total_classes()/count)
        total_per_class_antoine = total_per_class /2
        return [total_per_class, total_per_class_antoine]

    def nb_student(self):
        count = 0
        for value in self.students.values():
            count += 1
        return count

    def recap(self):
        students_name = self.display_students()
        nb_student = self.nb_student()
        age_average = self.age_average()
        total_money = self.total_money()
        total_per_class = (self.total_per_class())[0]
        total_per_class_antoine = (self.total_per_class())[1]

        print("Total Students : {}.".format(nb_student))
        print("Students : {}".format(list(students_name)))
        print("Age average : {} years old.".format(age_average))
        print("Total money : {} RMB.".format(math.trunc(total_money)))
        print("Total per class : {} RMB.".format(math.trunc(total_per_class)))
        print("Total Antoine per class : {} RMB.".format(math.trunc(total_per_class_antoine)))

class Student:
    def __init__(self, name, age, package):
        self.name = name
        self.age = age
        self.package = package

    def __str__(self):
        return "\n{}, {} years old, {} ( {} classes : {}RMB)".format(self.name, self.age, self.package.package_name, self.package.nb_class, self.package.price)

### CLASS INSTANTIATION ---

package_32 = Package(32)
package_16 = Package(16)
package_32_30off = Package(32,30)

leon = Student("Leon", 3, package_32_30off)
sunny = Student("Sunny", 3, package_32)
jayden = Student("Jayden", 3, package_32)
ann = Student("Ann", 3, package_16)
lucas = Student("Lucas", 4, package_32)
chen = Student("Chen", 3, package_32)

class_south_1 = Class("Class South 1", 1030, 1200, "Chengdu South")

class_1_name = [leon, sunny, jayden, ann, lucas, chen]

for name in class_1_name:
    class_south_1.add_student(name)

class_south_1.recap()