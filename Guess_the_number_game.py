import random

top_range = input("Enter the length of numbers! ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Enter larger number than 0!")
        quit()

else:
    print("Enter a number next time!")
    quit()

random_number = random.randint(0, top_range)
guess = 0

while True:
    guess +=1
    user_guess = input("Guess The Number! ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please, type a number next time!")
        continue

    if user_guess == random_number:
        print("Right!")
        print("You got it in" , guess , "guesses!")
        break
    # elif user_guess > random_number:
    #     print("You above the range of number!")
    elif user_guess > top_range:
        print("You above the length of numbers")
    else:
        print("Wrong!")

    # print("You got it in" , guess , "guesses!")