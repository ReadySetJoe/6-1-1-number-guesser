import random

input("Okay, level 2! This time, you think of a number between 0 and 100 and I'll guess it. Press Enter when you've thought of your number")

d = {0:"first",1:"second",2:"third",3:"fourth",4:"fifth and final"}
ll = 0
ul = 100
for i in range(5):
  guess = random.randint(ll,ul)
  result = input("For my " + d[i] + " guess, is it " + str(guess) + "? (Enter 'gt' if I was too high, 'lt' if I was too low, or 'eq' if I guessed it!")
  if result == 'lt':
    print("Okay, I'll try to guess higher next time!")
    ll = guess
  elif result == 'gt':
    print("Okay, I'll try to guess lower next time!")
    ul = guess
  elif result == 'eq':
    print("AWWWW HELL YEAH WAHOO! I'M A GENIUS")
    exit()
  else:
    print("aww c'mon, I can't guess it if you won't tell me how I did :(")
print("Dang :( let's play again!")