from random  import *

msg = ["m1","m2","m3","m4","m5"]

def gm(num):
	i =1
	while i <=num:
		yield choice(msg)
		i=i+1

for i in gm(5):
	print(i)