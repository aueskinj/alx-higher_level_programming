#!/usr/bin/python3

# # # class Person:
# # #     def __init__(self, name):
# # #         self.name = name

# # #     def say_hi(self):
# # #         print("Hello, my name is ", self.name)

# # # p = Person('Swaroop')
# # # p.say_hi()

# # # class Robot:
# # #     """"Represents a robot, with a name"""

# # #     population = 0

# # #     def __init__(self, name):
# # #         """"initializes the data"""
# # #         self.name = name
# # #         print("(Initializing {})".format(self.name))

# # #         #when this person is created, the robot
# # #         #adds to the population
# # #         Robot.population += 1

# # #     def die(self):
# # #         """I am dying."""
# # #         print("{} is being destroyed!".format(self.name))

# # #         Robot.population -= 1

# # #         if Robot.population == 0:
# # #             print("{} was the last one".format(self.name))
# # #         else:
# # #             print("There are still {} robots working".format(Robot.population))
    
# # #     def say_hi(self):
# # #         """Greeting by the Robot,
        
# # #         Yeah they can do that!"""

# # #         print("Greetings, my master calls me {}".format(self.name))


        
# # #     @classmethod
# # #     def how_many(cls):
# # #         """Print the current population"""

# # #         print("We have {:d} robots".format(cls.population))


# # # droid1 = Robot("R2-D2")
# # # droid1.say_hi()
# # # Robot.how_many()


# # # droid2 = Robot("C-3PO")
# # # droid2.say_hi()
# # # Robot.how_many()

# # # print('\nRobots can do the same work here')

# # # print("\nRobots have finished their work here")

# # # droid1.die()
# # # Robot.how_many()
# # # droid2.die()
# # # Robot.how_many()

# # class SchoolMember():
# #     """Represents any schoool Member"""
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         print("Initialised SchoolMember:{}".format(self.name))        
# #     def tell(self):
# #         """Tell my details"""
# #         print("Name : '{}' Age: '{}' ".format(self.name, self.age))

    
# # class Teacher(SchoolMember):
# #     """Represents a school member"""
# #     def __init__(self, name, age, salary):
# #         SchoolMember.__init__(self, name, age)
# #         self.salary = salary
# #         print("(Initialised Teacher):{}".format(self.name))
# #     def tell(self):
# #         SchoolMember.tell(self)
# #         print("Salary: {:d}".format(self.salary))

# # class Student(SchoolMember):
# #     """Represents a student"""
# #     def __init__(self, name, age, marks):
# #         SchoolMember.__init__(self, name, age)
# #         self.marks = marks
# #         print("(Initialised name):{}".format(self.name))
# #     def tell(self):
# #         SchoolMember.tell(self)
# #         print("Marks: {:d}".format(self.marks))
# # t = Teacher("Mrs. Kimuhu", 40, 30000)
# # s = Student("Martin", 20, 75)

# # print()

# # member = [t,s]

# # for i in member:
# #     i.tell()

        


# class BankAccount:
#     """Encapsulation"""
#     def __init__(self, acount_holder, balance):
#         self.account_holder = acount_holder
#         self._bank_name = "Secure Bank"
#         self.__balance = balance
    
#     def deposit(self, amount):
#         """public method to deposit money"""
#         if amount > 0:
#             self.__balance += amount
#             print("Deposited".format(amount))
#         else:
#             print("Invalid deposit amount")
    
#     def withdraw(self, amount):
#         """Public method to withdraw money"""
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds or invalid amount")

#     def get_balance(self):
#         """Public method to get the balance"""
#         return self.__balance

# account = BankAccount("Alice", 1000000)

# print(account.account_holder)
# print()
# print(account._bank_name)
# # print(account.__balance)
# print(account.get_balance())
# account.deposit(5000)
# account.withdraw(1200000)
# account.withdraw(12000)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle Started")
    
    def stop(self):
        print("Motorcycle stopped")

vehicle1 = Car()
vehicle1.start()
vehicle1.stop()

vehicle2 = Motorcycle()
vehicle2.start()
vehicle2.stop()

