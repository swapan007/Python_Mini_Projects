#STONE PAPER SCISSOR GAME BY SWAPAN CHETRI

#imp functions


def game_rules():
      print("WELCOME TO THE GAME STONE PAPER SCISSOR \n -->Here Are Some Rules:: \n 1-> You can play with your friends or with computer \n"
          " 2-> You have 10 chances to play with computer or with your friends \n 3-->The most winner will win the game"
      "\n POINTS GAINING RULES: \n"
      "-> stone + stone= Draw \n"
      "-> stone + paper = Paper Wins \n"
      "-> stone + scissor = stone wins \n"
      "-> papaer + paper = draw \n"
      "-> paper + scissor = scissor wins \n"
      "-> paper + stone= paper wins \n"
      "-> scissor + scissor = draw \n"
      "-> scissor + stone = stone wins \n"
      "-> scissor + paper = scissor wins"
      " \n IMP POINT:: Draw= 0 point gain otherwise the winner will get 1 point for winning each chance \n "
      "the most point scorer will win the game BEST OF LUCK!!!")
############################################################################################################
def with_computer():
      import random
      list1 = ["stone", "paper", "scissor"]
      computer_points=0
      user_points=0
      i=1
      while i<=10:
            user_input=input("CHOOSE ANY ONE FOR THE FOLLOWING: \n 1-> stone \n 2-> paper \n 3-> scissor\n")
            a = random.choice(list1)
            try:
                user_input=int(user_input)
                if user_input==1:
                      if a=="stone":
                            print("DRAW!!")
                      elif a=="paper":
                            print("COMPUTER WINS!!")
                            computer_points=computer_points+1
                      else:
                            print("You win!!")
                            user_points=user_points+1

                elif user_input == 2:
                        if a == "paper":
                              print("DRAW!!")
                        elif a == "scissor":
                              print("COMPUTER WINS!!")
                              computer_points = computer_points + 1
                        else:
                              print("You win!!")
                              user_points = user_points + 1

                elif user_input == 3:
                        if a == "scissor":
                              print("DRAW!!")
                        elif a == "stone":
                              print("COMPUTER WINS!!")
                              computer_points = computer_points + 1
                        else:
                              print("You win!!")
                              user_points = user_points + 1
                else:
                    print("INVALID INPUT!!")
                    continue
                i=i+1
                j=11-i
                print(f"computer points={computer_points}\n user points={user_points}\n no of chances left={j}")
            except:
                print("invalid input!!")
      if user_points > computer_points:
          print(f"CONGRATULATIONS!! YOU WIN!!\nyour score is->{user_points}")
      elif computer_points > user_points:
          print(f"COMPUTER WINS!!\nyour score is->{computer_points}")
      else:
          print("DRAW!!")

######################################################################################################################
def with_friend():
    user_2_points = 0
    user_1_points = 0
    i=1
    while i <= 10:
        user_input = input("U1: CHOOSE ANY ONE FOR THE FOLLOWING: \n 1-> stone \n 2-> paper \n 3-> scissor\n")
        user_input2= input("U2: CHOOSE ANY ONE FOR THE FOLLOWING: \n 1-> stone \n 2-> paper \n 3-> scissor\n")
        try:
            user_input = int(user_input)
            a=int(user_input2)

            if user_input == 1:
                if a == 1:
                    print("DRAW!!")
                elif a == 2:
                    print("USER 2 WINS!!")
                    user_2_points = user_2_points + 1
                else:
                    print("USER 1 WINS!!")
                    user_1_points = user_1_points + 1
            elif user_input == 2:
                if a == 2:
                    print("DRAW!!")
                elif a == 3:
                    print("USER 2 WINS!!")
                    user_2_points = user_2_points + 1
                else:
                    print("USER 1 WINS!!")
                    user_1_points = user_1_points + 1
            elif user_input == 3:

                if a == 3:
                    print("DRAW!!")
                elif a == 1:
                    print("USER 2 WINS!!")
                    user_2_points = user_2_points + 1
                else:
                    print("USER 1 WINS!!")
                    user_1_points = user_1_points + 1
            else:
                print("INVALID INPUT!!")
                continue
            i+=1
            j =11-i
            print(f"User 2 points={user_2_points}\nuser 1 points={user_1_points}\nno of chances left={j}")

        except:
            print("invalid input!!")
    if user_1_points > user_2_points:
        print(f"CONGRATULATIONS!! USER 1 YOU WIN!!\nyour score is->{user_1_points}")
    elif user_2_points >user_1_points:
        print(f"CONGRATULATIONS!! USER 2 YOU WIN!!\nyour score is->{user_2_points}")
    else:
        print("DRAW!!")
#########################################################################################################################
while True:
    input1=input("ENTER YOUR CHOICE::\n1-> GAME RULES\n2-> PLAY WITH COMPUTER\n3-> PLAY WITH FRIEND\n")
    try:
        input1=int(input1)
        if input1==1:
            game_rules()

        elif input1==2:
            with_computer()

        elif input1==3:
            with_friend()

        else:
            print("WRONG INPUT!!")
            continue
        a = input("DO YOU WANT TO GO TO HOME SCREEN:: y/n\n")
        if a != "y":
            break
    except:
        print("INVALID INPUT!!")
        continue



