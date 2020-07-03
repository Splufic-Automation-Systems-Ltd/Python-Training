# ls =[]

# # for i in range(21):
# # 	for j in range(10):
# # 		ls.append(i + j)

# square = []
# # for i in range(1, 10):
# # 	square.append(i ** 2)

# # print(square)
# # generate my list in one line
# # ls = [i * j + k for i in range(21) for j in range(10) for  k in range(1,10)]
# # print the list
# # print (ls)


# def squared(x):
# 	return x ** 2

# # square = [squared(i) for i in range(10)]
# # print(square)


# # adding conditionals
# # using if
# for i in range(1, 10):
# 	if i % 2 == 0 and i % 3 == 0:
# 			square.append(squared(i))

# square = [squared(i) for i in range(1,13) if (i % 2 == 0) if (i % 3 == 0) if i > 6]

# # testing if/else
import math
# square = []
# for i in range(1, 10):
# 	if i % 2 == 0:
# 		square.append(math.sin(i))
# 		continue
# 	square.append(math.cos(i))

# square = [math.sin(i) if i % 2 == 0 else math.cos(i) for i in range(1, 10)]
# print(square)


# fibinacci sequence

terms = []
a = 0
b = 1
for i in range(100):
	if i <= 1:
		terms.append(i)
	else:
		a = terms[i - 2]
		b = terms[i - 1]
		nth_term = a + b
		if nth_term >= 4000000:
			break
		terms.append(nth_term)

# using list comprehension
alpha = float((1 + math.sqrt(5)) / 2)
beta = float((1 - math.sqrt(5)) / 2)
def find_nth_term(n):
	return int(1/ math.sqrt(5) * (math.pow(alpha, n) - math.pow(beta, n)))

terms = [
			i if i <= 1 
			else find_nth_term(i) 
			for i in range(100) 
			if find_nth_term(i) < 4000000
		]                                       
# using map
def add_ten(n):
	return n + 10
print(terms)
terms = list(map(add_ten, terms))

even_terms = [i for i in terms if i % 2 == 0]
print(terms)
# print(even_terms)
# print(sum(even_terms))
# set the range of values that you want
a, b = 10, 19

table = {}
def makeTable(n):
	return [n * i for i in range(1, 13)]

for i in range(a, b):
	table[str(i) + '_terms'] = makeTable(i)

# for key, value in table.items():
# 	print(key, value)


# from functools import reduce
