# class Person:
# 	pass
# 	return "Hello world!"

# p= Person()
# print(p)


# class Person:
# 	def say_hi(self):
# 		print('Hello,How are you?')

# p = Person()
# p.say_hi()

# class Person:
# 	def __init__(self, name):
# 		self.name = name

# 	def say_hi(self):
# 		print('Hello,my name is ', self.name)
# class Person:
# 	def __init__(self, name, age , gender):
# 		self.name = name
# 		self.age = age
# 		self.gender = gender
	

# 	def say_hi(self):
# 		print('Hello,my name is ', self.name)

# 	def say_age(self):
# 		print('Age is ', self.age)

# 	def say_gender(self):
# 		print('Gender is ', self.gender)

# p= Person('MgMg','18','Male');
# p.say_hi()
# p.say_age()
# p.say_gender()

# class Robot:
# 	population = 0

# 	def __init__(self,name):
# 		self.name= name
# 		print("(Initializing {})".format(self.name))

# 		Robot.population += 1

# 	def die(self):
# 		#I am dying.
# 		print("{} is being destroyed!".format(self.name))

# 		Robot.population -= 1

# 		if Robot.population == 0:
# 			print("{} was the last one.". format(self.name))
# 		else:
# 			print("There are still {:d} robots working.".format(Robot.population))

# 	def say_hi(self):
# 		#Greering by the robot,
# 		#Yeah,they can do that,

# 		print("Greeting, my sisters call me {}.".format(self.name))

# 	@classmethod
# 	def how_many(cls):
# 			"""Prints the current population."""
# 			print("We have {:d} robots.".format(cls.population))

# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()

# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()

# droid3 = Robot("Q35")
# droid3.say_hi()
# Robot.how_many()

# droid4 = Robot("RP2")
# droid4.say_hi()
# Robot.how_many()

# print("\nRobots can do some work here.\n")

# print("Robot have finishied their wrok.So let's destroy them")
# droid1.die()
# droid2.die()
# droid3.die()
# droid4.die()

# Robot.how_many()


class SchoolMember:

	def __init__(self,name,age):
		self.name = name
		self.age = age
		print('Initialized SchoolMember : {}'.format(self.name))

	def tell(self):
		print('Name: "{}" Age: "{}"'.format(self.name,self.age),end="")

class Teacher(SchoolMember):

	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		print('(Initialized Student: {}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))

class Student(SchoolMember):

	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		print('(Initialized Student: {}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40 , 30000)
s = Student('Swaroop',25,75)

print()

members = [t,s]
for member in members:
	member.tell();