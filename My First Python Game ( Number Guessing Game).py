# This is my First Python Game 
import random
num = random.randint(1,100)
num

print("Hey Buddy! Welcome to this Game:")
print("In this game you have to guess one number between 1-100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")

gusses = [0]
while True:
    guess = int(input("Hey I have one number for you to guess, so try to guess it:"))
    if guess < 1 or guess >100:
        print("OUT OF BOUND ! Please try again:")
        continue
        
    # if the guess is correct
    if guess == num:
        print("Yay! you did it, you take {} guesses to get it right".format(len(gusses)))
        break
        
    # if the guess is incorrect add the guess to the list
    gusses.append(guess)
    
    if gusses[-2]:
        if abs(num-guess) < abs(num-gusses[-2]):
              print("Warmer")
        else:
              print("Colder")
    else:
        if abs(num-guess) <= 10:
            print("Warm")
        else:
            print("Cold")
        
    

