import random

#Generate random number in between 1 and 100
n = random.randint(1,100)

#prompt the user enter a number
guess = int(input("Enter the number between 1 and 100:"))

#continue the loop until user guessing the correct number:
while guess !=n:
    if guess <n:
        print("Too Low")
    elif guess >n:
        print("Too high")

    #Prompt the user to guess again
    guess = int(input("Enter the number again: "))

print("you guessed the right!!")

