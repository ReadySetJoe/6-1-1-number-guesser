import random

x = random.randint(0,100)
# print(x)
guess = int(input("Hello! Let's play a game! Try to guess my number!\n(Type a number bewteen 0 and 100 and hit 'Enter')"))

for i in range(1,5):
  if guess < x:
    guess = int(input("Nope, too low! Try again! (attempt #" + str(i+1) + " of 5)"))
  elif guess > x: 
    guess = int(input("Nope, too high! Try again! (attempt #" + str(i+1) + " of 5)"))
  else:
    print("HOLY SHIT YOU GOT IT THAT'S INSANE THE NUMBER WAS TOTALLY " + str(x) + "!!!!!")
