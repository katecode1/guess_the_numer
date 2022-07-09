import random 
start = input('Guess from :')
end = input('Guess to :')
start = int(start)
end = int(end)
r  =  random.randint(start,end)
count = 0
while True:
	count += 1 # count = count + 1 
	num = input('Hey! guass a number : ')
	num = int(num)
	if num == r:
		print('Correct!')
		print('guess',count,'times')
		break
	elif num > r:
		print('Greater than the ans')
	elif num < r:
		print('Less than the ans')
	print('guess',count,'times')