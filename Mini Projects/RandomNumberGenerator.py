import random

target = random.randint(1, 100)

while True:
    guess = input("Guess the number or enter quite for quite : ")
   
    if(guess == "quite"):
        break

    elif(guess == str(target)):
        print("You guess the right number.")
        break

    elif(guess > str(target)):
        print("You guessed the greater number. Guess again!")

    else:
        print("You guessed the smaller number. Guess again!")
    

print("------------Game Over--------------")