from tkinter.font import BOLD, ITALIC

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the lost dragon hamlet.")
print("As the storm started while you are in the festival market\n. "
      "you fell in to the storm and it took you on to sailing "
      "ship towards island.")
user_line1 = input("Type left or right").lower()

if user_line1 == "left":
    choice2=input("the sea monsters are rising towards face of the"
                  " water and coming towards the ship\n. "
          "Turn the wheel and move the ship.'swim' or 'fight'").lower()
    if choice2== "swim":
          choice3 = input('which way you want to go "straight"'
                          ' or "east" or "west"')
          if choice3 == "east":
              print("its a room full of fire. Game Over")
          elif choice3 == "west":
              print("You have finally reached the mystical land. "
                    "Now, walk along the golden arrow you to get the "
                    "magical treasure box"
                f"r''''************************  The World of "
                    f"magic...... always has a way to welcome you...."
                    f"\nhave a safe trip and see you again.***************")
          elif choice3=="straight":
              print("you were melted in the hot room. Game Over!")
          else:
              print("you chose a door to black hole. Game Over")
    else:
              print("you entered the lava road. Game Over!")

else:
     print(f" The Giant red jelly fish eat you.Game Over! ")


