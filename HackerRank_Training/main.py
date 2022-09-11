import random
top_of_range = int(input("type a top of range number: "))
random_number = random.randint(0, top_of_range)
bottom_of_range = 0
while True:
    computer_guess = random.randint(bottom_of_range, top_of_range)
    print("random number" +str(random_number))
    if computer_guess == random_number:
        print(computer_guess)
        print("RIGHT NUMBER")
        break
    elif computer_guess > random_number:
        print(computer_guess)
        print("you were above the number")
        top_of_range = computer_guess
    else:
        print(computer_guess)
        print("you were below the number")
        bottom_of_range = computer_guess

