### MODULES ---
from datetime import datetime

### CLASS DECLARATION ---

class Performance:
    def __init__(self, weight, rep, rm):
        self.weight = weight
        self.rep = rep
        self.rm = rm

class Gym:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.user = {}

    def __str__(self):
        return "\n--- Gym Properties ---\n- Name: {}\n- Location: {}\n- Users: {}".format(self.name, self.location, list(self.user))

    def add_user(self, user):
        self.user[user.name]=user

    def display_user_name(self):
        print("\nMember of {}:".format(self.name))
        count = 0
        for user_name, user in self.user.items():
            count += 1
            print("{}. {}".format(count, user_name))

class User:
    def __init__(self, name, surname, birthday, weight, size):
        self.name = name
        self.surname = surname
        self.weight = weight
        self.size = size
        self.birthday = datetime(int(birthday[4:]), int(birthday[:2]), int(birthday[3:4]))
        self.age = datetime.today().year - self.birthday.year - ((datetime.today().month, datetime.today().day) < (self.birthday.month, self.birthday.day))
        
    def __str__(self):
        return "\n--- User Properties ---\n- Name: {}\n- Surname: {}\n- Age: {}\n- Weight: {}\n- Size: {}".format(self.name, self.surname, self.age, self.weight, self.size)

    def update_weight(self, new_weight):
        self.weight = new_weight

class Workout:
    def __init__(self, name):
        self.name = name
        self.list_exercises = {}

    def add_exercise(self, exercise, set):
        self.list_exercises[exercise]=set

    def remove_exercise(self, exercise):
        self.list_exercises.pop(exercise, None)

    def update_exercise(self, exercise, new_set):
        self.list_exercises[exercise]=new_set

    def display_exercise(self):
        print("\n--- Workout name: {} ---".format(self.name))
        for exercise, set in self.list_exercises.items():
            print("\n{}\n- Sets: {}".format(exercise.name, set))

class Exercise:
    def __init__(self, name):
        self.name = name
        self.performance = {}

    def add_performance(self, user, weight, rep, rm):
        new_performance = Performance(weight, rep, rm)
        self.performance[user] = new_performance

    def remove_perfomance(self, user):
        self.performance.pop(user, None)

    def display_all_performance(self):
        print("\n--- Performance {} ---".format(self.name))
        for user, performance in self.performance.items():
            print("- {}KG x {} - RM: {}KG".format(performance.weight, performance.rep, performance.rm))

    def display_user_performance(self, user):
        print("\n--- Performance {} - {} ---".format(self.name, user.name))
        for user_dict, performance in self.performance.items():
            if user == user_dict:
                print("- {}KG x {} - RM: {}KG".format(performance.weight, performance.rep, performance.rm))

### CLASS INSTANTIATION --- 

# USER
antoine = User("Antoine", "Ratat", "10061990", 73.4, 176)
bastien = User("Bastien", "Ratat", "05281994", 76.4, 173)
max = User("Maximilien", "Proville", "12281997", 81.4, 180)

# GYM
wordfit = Gym("Word Fit", "Jianshe Road")
commafit = Gym("Comma Fit", "SM Plaza")

# EXERCISE
dev_incl_haltere = Exercise("Developpé Haltère Incliné")
dev_couche_barre = Exercise("Developpé Barre Couché")
ecarte_incl_haltere = Exercise("Ecarté Haltère Incliné")

# WORKOUT
chest_day = Workout("Chest Workout")
chest_day.add_exercise(dev_incl_haltere, 5)
chest_day.add_exercise(dev_couche_barre, 5)
chest_day.add_exercise(ecarte_incl_haltere, 3)

# PERFORMANCE
dev_couche_barre.add_performance(antoine,110,8,120)
dev_couche_barre.add_performance(bastien,90,8,100)

### CODE ---

wordfit_user_list = [antoine, bastien]
commafit_user_list = [antoine, max]

for user in wordfit_user_list:
    wordfit.add_user(user)

for user in commafit_user_list:
    commafit.add_user(user)

wordfit.display_user_name()
commafit.display_user_name()

print(wordfit)
print(commafit)

print(antoine)
print(bastien)

bastien.update_weight(170)
print(bastien)

chest_day.display_exercise()

dev_couche_barre.display_all_performance()
dev_couche_barre.display_user_performance(antoine)
dev_couche_barre.display_user_performance(bastien)