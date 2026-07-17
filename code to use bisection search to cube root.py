#code to use bisection search to find the cube 
#root of positive cubes to within some epsilon

cube = 27
epsilon = 0.01
low = 0
high = cube
guess = (high + low)/2.0
numGuesses=0
while abs(guess**3 - cube) >= epsilon:
	if guess**3 < cube :
		low = guess
	else:
		high = guess
	guess = (high + low)/2.0
	numGuesses += 1
print('numGuesses =', numGuesses)
print(guess, 'is close to the cube root of', cube)
