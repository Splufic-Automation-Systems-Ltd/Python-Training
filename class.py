

# #class
# # terms 
# 	# i. features/attributes 
# 	# ii. methods

# # i. a class with args
# # ii a class without args

# # task
# # crate a person class
# # features; age, sex, name, occupation, height
# class Person(object):
# 	"""
# 		docstring for Person:

# 	"""
# 	def __init__(self, name, age, occupation, height, sex):
# 		# super(Person, self).__init__()
# 		self.name = name
# 		self.age = age
# 		self.occupation = occupation
# 		self.height = height
# 		self.sex = sex

# 	def addSex(self, sex):
# 		self.sex = sex
# 	def addAge(self, age):
# 		self.age = int(age)

# 	def addOccupation(self, occupation):
# 		self.occupation = occupation

# 	def addHeight(self, height):
# 		self.height = float(height)

# 	def walk(self, steps):
# 		print(f'{self.name} just took {steps} steps.')

# person = Person('Tayo', 22, 'Farmer', 5.9, 'Male')
# # person.addSex('Male')
# # person.addHeight(5.8)
# # person.addOccupation('Farmer')
# person.addAge(30)

# age = person.age
# name = person.name
# height = person.height
# occupation = person.occupation
# sex = person.sex

# person.walk(100)
# print(f'I am {name} and {age} years old.\nI am a {occupation}.\
# \nI am {height} and I am {sex}.\nThank you!')

# tayo = Person
# # tayo()


# create a person class that can walk
# features; height, sex, age, name, occupation
# walk takes step ardument 
# shout 
# eat 
# sleep
# sing 

# import random
# class Person(object):
# 	"""docstring for Person"""
# 	def __init__(self, name):
# 		# super(Person, self).__init__()
# 		self.name = name
# 		# self.engine_number = '000222233030'
# 		self.steps = 0
# 		print(self.name, 'has just been initialized.')

# 	def setAge(self, value):
# 		self.age = value

# 	def setSex(self, sex):
# 		self.sex = sex

# 	def setHeight(self, height):
# 		self.height = height

# 	def walk(self, steps):
# 		print(self.name, 'is took ', steps, 'steps.')
# 		r_number = random.randint(0, 100)
# 		self.steps +=  (steps * r_number)


# 	def eat(self, food):
# 		print('I am eating ', food)

# tayo = Person('Tayo')
# comfort = Person('Comfort')


# # set tayo's attributes
# tayo.setAge(12)

# # set comfort's attributes
# comfort.setAge(12)

# #  Game start

# # tayo took 10 steps
# tayo.walk(10)

# # comfort took 30 steps
# comfort.walk(30)

# # tayo took 2 steps
# tayo.walk(2)

# # comfort took 10 steps
# comfort.walk(10)

# # at the end of the day
# # print the steps of each players
# print(f'{tayo.name} took {tayo.steps} steps\n {comfort.name} took {comfort.steps} ')
# if tayo.steps > comfort.steps:
# 	print(f'The winner is {tayo.name}')
# else:
# 	print(f'The winner is {comfort.name}')
# # tayo.setAge(20)
# # tayo.setSex('Male')
# # tayo.setHeight(5.9)
# # print(tayo.name, tayo.age)
# # tayo.walk(20)
# # tayo.eat('Rice')



# inheritance
# Parent
class Parent(object):
	"""docstring for Parent"""
	def __init__(self, name):
		# super(Parent, self).__init__()
		self.name = name
		self.height = 6.0
		# print()

	def getHeight(self):
		print(self.height)
		
class Child(Parent):
	"""docstring for Child"""
	def __init__(self, name):
		super(Parent, self).__init__()
		self.name = name
		self.height = 6.2

	def getHeight(self):
		print(self.height)


child = Child('Tayo')
print(child.name)
child.getHeight()
print('------------------------------------')
parent = Parent('Tolu')
print(parent.name)
parent.getHeight()

