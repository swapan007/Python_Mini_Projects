#health management system using file handling in python by swapan chetri

#FUNCTIONS FOR EXERCISE INPUT

def swapan_exercise_input():
    exercise=input("ENTER YOUR EXERCISE HERE::->")
    f=open("swapan_exercise.txt","a")
    f.write(str(date_time()) +"-->"+ exercise + "\n")
    f.close()

def sanjeev_exercise_input():
    exercise=input("ENTER YOUR EXERCISE HERE::->")
    f=open("sanjeev_exercise.txt","a")
    f.write(str(date_time()) +"-->"+ exercise + "\n")
    f.close()

def tathagat_exercise_input():
    exercise=input("ENTER YOUR EXERCISE HERE::->")
    f=open("tathagat_exercise.txt","a")
    f.write(str(date_time())+ "-->" + exercise + "\n")
    f.close()
#FUNCTIONS FOR FOOD INPUT
def swapan_food_input():
    food=input("ENTER YOUR FOOD HERE::->")
    f = open("swapan_food.txt", "a")
    f.write(str(date_time()) + "-->" + food + "\n")
    f.close()

def sanjeev_food_input():
    food=input("ENTER YOUR FOOD HERE::->")
    f = open("sanjeev_food.txt", "a")
    f.write(str(date_time()) + "-->" + food + "\n")
    f.close()

def tathagat_food_input():
    food=input("ENTER YOUR FOOD HERE::->")
    f = open("tathagat_food.txt", "a")
    f.write(str(date_time()) + "-->" + food + "\n")
    f.close()

#EXERCISE RETRIEVAL
def swapan_exercise_retreve():
    with open("swapan_exercise.txt") as f:
        for i in f:
            print(i)

def sanjeev_exercise_retreve():
    with open("sanjeev_exercise.txt") as f:
        for i in f:
            print(i)

def tathagat_exercise_retreve():
    with open("tathagat_exercise.txt") as f:
        for i in f:
            print(i)

#FOOD RETREVE FUNCTIONS
def swapan_food_retreve():
    with open("swapan_food.txt") as f:
        for i in f:
            print(i)


def sanjeev_food_retreve():
    with open("sanjeev_food.txt") as f:
        for i in f:
            print(i)


def tathagat_food_retreve():
    with open("tathagat_food.txt") as f:
        for i in f:
            print(i)

def date_time():
    import datetime
    return datetime.datetime.now()


def swapan_loop():
    print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
    print("1--> EXERCISE \n 2--> FOOD")
    input2 = int(input())
    if input2 == 1:
        print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
        print("1--> INPUT VALUES \n 2--> RETREVE VALUES")
        input3=int(input())
        if input3==1:
            k="y"
            while (k!="n"):
                swapan_exercise_input()
                k=input("YOU WANT TO ADD MORE DATA Y/N")

        elif input3==2:
                swapan_exercise_retreve()

        else:
            print("INVALID INPUT")
            swapan_loop()
    elif input2 == 2:
        print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
        print("1--> INPUT VALUES \n 2--> RETREVE VALUES")
        input3 = int(input())
        if input3 == 1:
            k = "y"
            while (k!="n"):
                swapan_food_input()
                k = input("YOU WANT TO ADD MORE DATA Y/N")

        elif input3 == 2:
                swapan_food_retreve()


        else:
            print("INVALID INPUT")
            swapan_loop()
    else:
        print("INVALID INPUT!!")
        swapan_loop()

#################################################################################
def sanjeev_loop():
    print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
    print("1--> EXERCISE \n 2--> FOOD")
    input2 = int(input())
    if input2 == 1:
        print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
        print("1--> INPUT VALUES \n 2--> RETREVE VALUES")
        input3 = int(input())
        if input3 == 1:
            k = "y"
            while (k!="n"):
                sanjeev_exercise_input()
                k = input("YOU WANT TO ADD MORE DATA Y/N")

        elif input3 == 2:
                sanjeev_exercise_retreve()

        else:
            print("INVALID INPUT")
            sanjeev_loop()
    elif input2 == 2:
        print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
        print("1--> INPUT VALUES \n 2--> RETREVE VALUES")
        input3 = int(input())
        if input3 == 1:
            k = "y"
            while (k!="n"):
                sanjeev_food_input()
                k = input("YOU WANT TO ADD MORE DATA Y/N")

        elif input3 == 2:

                sanjeev_food_retreve()


        else:
            print("INVALID INPUT")
            sanjeev_loop()
    else:
        print("INVALID INPUT!!")
        sanjeev_loop()
###########################################################
def tathagat_loop():
    print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
    print("1--> EXERCISE \n 2--> FOOD")
    input2 = int(input())
    if input2 == 1:
        print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
        print("1--> INPUT VALUES \n 2--> RETREVE VALUES")
        input3 = int(input())
        if input3 == 1:
            k = "y"
            while (k!="n"):
                tathagat_exercise_input()
                k = input("YOU WANT TO ADD MORE DATA Y/N")

        elif input3 == 2:
                tathagat_exercise_retreve()


        else:
            print("INVALID INPUT")
            tathagat_loop()
    elif input2 == 2:
        print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
        print("1--> INPUT VALUES \n 2--> RETREVE VALUES")
        input3 = int(input())
        if input3 == 1:
            k = "y"
            while (k!="n"):
                tathagat_food_input()
                k = input("YOU WANT TO ADD MORE DATA Y/N")

        elif input3 == 2:
                tathagat_food_retreve()
        else:
            print("INVALID INPUT")
            tathagat_loop()
    else:
        print("INVALID INPUT!!")
        tathagat_loop()

while True:
    print("CHOOSE ANY ONE OF THE OPTIONS:: \n")
    print("1--> SWAPAN \n 2--> SANJEEV \n 3--> TATHAGAT")
    input1=int(input())
    if input1==1:
        swapan_loop()

    elif input1==2:
        sanjeev_loop()

    elif input1==3:
        tathagat_loop()
    else:
        print("INVALID INPUT!!")
    k = input("YOU WANT TO GO TO HOME SCREEN?? Y/N")
    if (k=="y"):
        continue
    else:
        break






