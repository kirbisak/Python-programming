# # https://www.w3schools.com/python/python_classes.asp

# class myClass:
#     name = "Simon"

# # p1 = myClass()
# # print(p1.name)

# class Person:
#     def __init__(self, name, age, message):
#         self.name = name
#         self.age = age
#         self.message = message

#     def __str__(self):
#         return (f"{self.name}({self.age}) - {self.message}")

#     # def print_name(self):
#     #     return (self.name)
#     # def print_age(self):
#     #     return (self.age)

# class osoba:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self) -> str:
#         return (f"My name is {self.name} {self.age}")
#     def set_age(self, age):
#         self.age = age


# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# class Student:
#     def __init__(self, name, age, grade) -> None:
#         self.name = name
#         self.age = age
#         self.grade = grade
    
#     def get_grade(self):
#         return self.grade
    
#     def get_name(self):
#         return self.name

# class Course:
#     def __init__(self, max_students) -> None:
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)
        

    
#     def average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return (value / len(self.students))

# s1 = Student("Simon", 19, 76)
# s2 = Student("Marek", 19, 90)
# s3 = Student("Tom", 24, 98)
# s4 = Student("Tom", 24, 100)
# x = Course(3)

# x.add_student(s1)
# x.add_student(s2)
# x.add_student(s3)
# x.add_student(s4)
# print(x.average_grade())
# print(x.get_students())


class Pet:
    def __init__(self, name, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color 

    def show(self) -> str:
        print (f"My name is {self.name} and I am {self.age} years old and my color is {self.color}")

class Dog(Pet):

    def sound(self):
        print("Bark")

class Cat(Pet):
    def sound(self):
        print("Meow")

class Fish(Pet):
    pass



a = Dog("Jim", 13, "Red")



a.show()
a.sound()