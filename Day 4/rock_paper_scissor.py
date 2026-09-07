import random
print("Welcome to the rock paper scissor game")
print("============================================================================")
user_input=int(input("please choose \n > rock --> 0 \n > paper --> 1 \n > scissor --> 2 \n > "))


rock_paper_scissor= ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
                     """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
                     """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

num_random=random.randint(0,2)
if num_random == user_input:
    print("IT'S A DRAW")
    print(f"your choice {rock_paper_scissor[user_input]}")
    print(f"computer choice {rock_paper_scissor[num_random]}")
elif (num_random == 0 and user_input == 1) or (num_random == 1 and user_input == 2) or (num_random == 2 and user_input == 0):
    print("YOU WIN")
    print(f"your choice {rock_paper_scissor[user_input]}")
    print(f"computer choice {rock_paper_scissor[num_random]}")
else:
    print("YOU LOSE")
    print(f"your choice {rock_paper_scissor[user_input]}")
    print(f"computer choice {rock_paper_scissor[num_random]}")

