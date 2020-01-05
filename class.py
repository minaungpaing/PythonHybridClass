def scope_test():
	def do_local():
		spam =" local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	# def do_global():
	# 	global spam
	# 	spam = "global spam"

	spam = "test spam"
	do_local()
	print("After local assignment:",spam)
	do_nonlocal()
	print("After nonlocal assignment:",spam)
	# do_global()
	# print("After global assignment:", spam)

scope_test()
# print("In global scope:",spam)

# def say_hello():
# 	print('Hello World')

# say_hello()

# def print_max(a,b):
# 	if a > b :
# 		print(a,'is maximum')
# 	elif a == b :
# 		print(a ,'is equal to ',b)
# 	else:
# 		print(b ,'is maximum')

# print(20 > 10 )
# print(20 == 10 )
# print(20 < 10 )
# print(bool("Hello World"))
# print(bool(20))
# print_max(3,4)

#local variable

# def func(x):
# 	print('x is',x)
# 	x = 2
# 	print('Changed local x to ',x)


# func(x)
# print('x is still',x)
# def func(y):
# 	print('y is',y)
# 	y = 50
# 	print('Changed local y to ',y)

# def funx(y):
# 	print('y is ',y)
# 	y= x+ y
# 	print('Y is Changed x + y',y)

# y = 20
# x = 40
# func(y)
# funx(y)
# print('y is still',y)

# # Global Statement

# def fung():
# 	global x

# 	print('x is',x)
# 	x = 2 
# 	print('Changed global x to',x)
# x = 50
# fung()
# print('Value of x is:',x)


# def do_global():
# 	global spam
# 	spam = "global spam"

# spam ="test spam"
# do_global()
# print("After global assignment:",spam)

# x=5 
# def func():
# 	nonlocal x
# 	print('x is',x)

	
# 	print("Value of x is:",x)
# x=10
# func()
# print("Real value or x is ",x)	