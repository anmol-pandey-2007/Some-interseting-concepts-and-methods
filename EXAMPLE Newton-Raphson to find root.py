#EXAMPLE: Newton-Raphson to find roots
e = 0.01
k = 2265
guess = k/2.0
num_guesses = 0

while abs(guess*guess - k) >= e:
	num_guesses += 1
	guess = guess - (((guess**2) - k)/(2*guess))
print(f'num_guesses = {str(num_guesses)}')
print(f'Square root of {str(k)} is about {str(guess)}')
