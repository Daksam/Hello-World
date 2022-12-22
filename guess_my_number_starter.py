import random

x = 1
y = 99

number = int(random.randint(x, y))

print("I am thinking of a number between",x,"and",y,". Try to guess it.")

while True:
    guess = int(input("Enter a guess: "))

    if guess < number:
        print("Your guess is too low. Guess again.")
        
    elif guess > number:
        print("Your guess is too high. Guess again.")
        
    else:
        print("Congrats! Your guess is correct.")
    
        break
