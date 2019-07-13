def game():
  box=(" ---- ","|    |","|    |"," ---- ");
  answer=2;
  for i in box:
    toprint="";
    for j in range(5):
      toprint+=i;
    print(toprint)
  print("Which box is the turkey in?")
  guess=int(input("Type a number, 1 through 4..."))
  print("Your guess was: "+str(guess))
  print("and the answer was: "+ str(answer))
  if guess==answer:
    print("Nice!")
    return game();
  else:
    print("Aw.")
    return game();
game();
