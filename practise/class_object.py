#!/usr/bin/python3

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def say_hi(self):
#         print("Hello, my name is ", self.name)

# p = Person('Swaroop')
# p.say_hi()

class Robot:
    """"Represents a robot, with a name"""

    population = 0

    def __init__(self, name):
        """"initializes the data"""
        self.name = name
        print("(Initializing {})".format(self.name))

        #when this person is created, the robot
        #adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {} robots working".format(Robot.population))
    
    def say_hi(self):
        """Greeting by the Robot,
        
        Yeah they can do that!"""

        print("Greetings, my master calls me {}".format(self.name))


        
    @classmethod
    def how_many(cls):
        """Print the current population"""

        print("We have {:d} robots".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()


droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print('\nRobots can do the same work here')

print("\nRobots have finished their work here")

droid1.die()
Robot.how_many()
droid2.die()
Robot.how_many()

        
        
        
    