import random
n = random.randint(1,10)
x = None
while True:
  x = int(input("Guess a number between 1 to 10: "))
  if x < n:
    print("Too Low")
  elif x > n:
    print("Too High")
  else:
    print("You did it right")
    x = input("Do you want to play Again? Enter Yes/No :  ")
    if x == "Yes":
      n = random.randint(1,10)
      x = None
    else:
      print("Thank you")
      break
