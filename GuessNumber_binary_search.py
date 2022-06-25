# binary search

import random

min_num = 1
max_num = 1000
secret_num = random.randint(min_num, max_num)

low = min_num
high = max_num+1
guesses = []
i = 50
guess = high//2

while i >= 0:
    if guess < secret_num:
        low = guess
        guess = (low+high)//2
    elif guess > secret_num:
        high = guess
        guess = (low+high)//2
    else:
        print(f"You got it, Secret number was {secret_num}")
        break
    print(f"Your guess: {guess}")
    guesses.append(comp_int)
    i = i-1
print(f"Computer took {len(guesses)} guesses!!!")
print()
