import time
def timedecor(func):
	def wrapper(*args,**kwargs):
		start = time.time()
		res = func(*args,**kwargs)
		end = time.time()
		print((end - start),' is the time taken')
		return res
	return wrapper

@timedecor
def hello():
	return

@timedecor
def forloop(r):
	for i in range(0,r):
		print(i)


#decorator is function, used to give extra functionalities to a function without modifying the function



