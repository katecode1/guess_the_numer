import random 
r  =  random.randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1 
	num = input('Hey! guass a number : ')
	num = int(num)
	if num == r:
		print('Correct!')
		break
	elif num > r:
		print('Greater than the ans')
	elif num < r:
		print('Less than the ans')
	print('guess',count,'times')