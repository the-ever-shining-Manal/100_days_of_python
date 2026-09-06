print('''
            /;
           / |'-,.
          /  '    `"---,.__
         /  '    ,'     ,  '"--,"|
        /  '    ,     ,'     ,"::|
       /  '   ,'    ,      ,"::::|
      /  '   ,    ,'     ,"::::::L
     /  '  ,'   ,'     ,"::::::::L
    /  '  ,    ,     ,":::::::::J
    k-,._    ,'   _.":::::::::::J
     \.  `"----'"".J::::::::::::|
      \.    .-,    .L:::::::::::|
       \.  (       .J:::::::::::!
        \.  `--     .L:::::::::/
         \.   .-.   .|::::::::/
          \. (   )  .J:::::::/
           \. `-'    .L:::::/
            \.  L    .|::::/
             \. !__  .J:::/
              \.  __  .L:/
               \. L_) .|/
                `-,__,-'    
''')
print("Welcome adventurer\n If you are reading this that means you have chosen to dive into this adventure and peculiar quest\n and your first mission is to FIND THE TREASURE")

user_input=input("narrator: you are dropped into a dark place. you struggle a bit and try to hove around until you find a way out.\n and oh! it looks like you were in a small cabin. you face away from it to look up a head to see two paths that are leading to the forest\n which one are you choosing\n >to the (left)\n >to the (right)\n > ").lower()
if user_input=='left' :
    user_input = input(
        "narrator: you went left, and started walking.weirdly enough it's not as dark in the forest as it was outside. \n"
        "the forest is beautifull with tall tress all around, but then you stumble upon a lack with a sign that has \n{please wait for the monkey to help you pass}. so,\n > do you wait (yes) \n > (no) you are going to swim your self it's not that deep)\n>").lower()
    if user_input == 'yes':
        user_input = input(
            "narrator: after much walking you find yourself in front of a house with 3 doors \none is red the other is blue and the last one is yellow witch one are you choosing\n red \n blue \n yellow .\n >").lower()
        if user_input == 'yellow':
            print("YOU WON")
            print("narrator: you finished your quest successfully and you found the treasure.")
        elif user_input == 'blue':
            print("GAME OVER")
            print("narrator: you died by being eaten by the evil mermaids.")
        elif user_input == 'red':
            print("GAME OVER")
            print("narrator: you died by being burned to death.")
        else:
            print("invalid input")

    else :
        print("GAME OVER")
        print("narrator: an evil fish ate you.")
else:
    print("GAME OVER")
    print("narrator: an evil witch was waiting for you to pass from here, and once she saw you. she cursed you into a small little frog")





