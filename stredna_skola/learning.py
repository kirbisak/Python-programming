# def func(n):
#     return n + 2

# myList = [1, 3, 5]
# x = map(func , myList)
# #print(list(x)) # -> [3, 5, 7]


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# x = map(mydoubler, (1, 2, 3))
# print(list(x))


from typing import Any


class Student:
   def __init__(self, name, grade) -> None:
      self.name = name
      self.grade = grade

   def get_grade(self):
      return self.grade
   
   def get_name(self):
      return self.name
      


# class Course:
#    def __init__(self, max_students) -> None:
#       self.max_students = max_students
#       self.grades = []
#       self.students = []

#    def add_student(self, student):
#       if len(self.students) < self.max_students:
#          self.students.append(student)
#          return True
#       return False
   
#    def average_grade(self):
#       value = 0
#       for student in self.students:
#          value += student.get_grade()
#       print(value / len(self.students)) 
   
# course = Course(4)

# s1 = Student("Tim", 10)
# s2 = Student("Bill", 6)
# s3 = Student("Jim", 8)

# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)

# course.average_grade()


class Client:
   def __init__(self, account) -> None:
      self.account = account
   
   def account_name(self):
      return self.account

class Bank:
   def __init__(self) -> None:
      self.clients = {}
   
   def creating_account(self, client, balance):
      self.account_name = client
      self.balance = balance
      if self.account_name in self.clients.values():
         print("Already existing")
      else:
         self.clients[self.account_name] = self.balance

   def deposit(self, account_name, amount):
      if account_name in self.clients:
         self.clients[account_name] += amount
      else:
         print("Account not found")
   
   def withdrawal(self, account_name, amount):
      if account_name in self.clients:
         if self.clients[account_name] >= amount:
            self.clients[account_name] -= amount 
         else:
            print("Insufficient funds")
      else:
         print("Account not found")

   
   
   def bank_clients(self):
      return self.clients

x = Bank()

c1 = Client("ac01")
c1_name = c1.account_name()



# x.creating_account("ac01", 20)

# x.deposit("ac01", 40)
# x.withdrawal("ac01", 200)

# print(x.bank_clients())

def ternary_to_decimal(number: str):
   result = 0
   index = len(number) - 1
   for element in number:
      result += int(element) * (3 ** index)
      index -= 1
   return result
   

def ternary_numbers(result, number: str, length: int, total: int):
   if length == 0 and total == 0:
      result.append((ternary_to_decimal(number)))
      return result
   
   if length == 0:
      return result

   if number == '':
      ternary_numbers(result, '2' + number, length - 1, total - 2)
      ternary_numbers(result, '1' + number, length - 1, total - 1)
   else:   
      ternary_numbers(result, number + '2', length - 1, total - 2)
      ternary_numbers(result, number + '1', length - 1, total - 1)
      ternary_numbers(result, number + '0', length - 1, total - 0)
   return result

def hi_albert():
   print(f"Ahoj, {(input())}. Ako sa mas?")

hi_albert()