import random

#have user choose
top_of_range = input("Type a number: ")

#validation for number input >0
if top_of_range.isdigit:
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please choose a number greater than 0 next time")
        quit()
else:
    print("Please type in a digit next time")
    quit()

#create random number for game and keep track of number of guesses
random_number = random.randint(0, top_of_range)
guesses = 0

#User guess random number with validation, keeping track of guesses
while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit:
        user_guess = int(user_guess)
    else:
        print("Please type in a digit next time")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")
        

print("You got it in", guesses, "guesses!")

