#input should be : guess the number between 1 and 100
#if the chosen number is greater than the guess, print "too high"
#if the chosen number is less than the guess, print "too low"
#if the guess is correct, print "Wowwww, u guessed it right !!"

import random as r
guess = r.randint(1,100)
count = 0
while True :
    i = input("Guess the number between 1 and 100:")
    try:
        a = int(i)
        count += 1
        if a > guess:
            print("Too High!!")
        elif a < guess:
            print("Too Low")
            
        else:
            print(f"You guessed it right, The number is {i} in {count} guesses")
    except ValueError:
        print("Enter a Valid Number")

print("Byee")
