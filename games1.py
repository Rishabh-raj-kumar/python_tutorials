import random

lists=["scissor","paper","rock"];

while True:
   computer=random.choice(lists);
   user=random.choice(lists);

   print("computer move : "+computer)
   print("Player move : "+user)

   if computer == "scissor" : 
       if user == "rock":
         print("You win")
       elif user == "paper":
         print("You Lose")
   elif computer == "paper" or user == "rock":
    print("You lose")
   elif computer == "rock" or user == "paper":
    print("You win")

    play=input("Enter a choice to play game : (yes/no)").lower()
    if play !="yes":
      break;
print('bye😊')
