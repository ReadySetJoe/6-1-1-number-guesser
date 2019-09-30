import random

input("Okay, I've got you this time! Level 3! Same as before, you think of a number between 0 and 100 and I'll guess it. But now I've gotten a little smarter :) Press Enter when you've thought of your number")

d = {0:"first",1:"second",2:"third",3:"fourth",4:"fifth and final"}
ll = 0
ul = 100
guess = 50 + random.randint(-5,5)
for i in range(5):
  result = input("For my " + d[i] + " guess, is it " + str(guess) + "? (Enter 'H' if I was too high, 'L' if I was too low, or just hit Enter if I guessed it!")
  if result == 'L':
    print("Okay, I'll try to guess higher next time!")
    ll = guess
    guess = round((ll+ul)/2)
  elif result == 'H':
    print("Okay, I'll try to guess lower next time!")
    ul = guess
    guess = round((ul+ll)/2)

  elif result == '':
    print("AWWWW HELL YEAH WAHOO! I'M A GENIUS")
    exit()
  else:
    print("aww c'mon, I can't guess it if you won't tell me how I did :(")
print("Dang :( let's play again!")