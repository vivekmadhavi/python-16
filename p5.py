def greet(fn):
	def inner():
		print("*" * 50)
		fn()
		print("*" * 50)
	return inner

@greet
def welcome():
	print("Good Morning")
def bye():
	print("have a good day")

welcome()

bye()