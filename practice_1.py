#firstgame


print("Welcome to my first project!")
name=input("What is your name? ")
age=int(input("What is your age?"))

print("Hello",name)

coins = 20

if age >=18:
    print("you are old enough to play the game")

    interested = input("Do you want to play,yes or no?(yes/no)")
    if interested =="yes":
        print("you are starting with ",coins,"coins")
        print(" YAY!,Lets play!")

        left_or_right = input("first choice...left or right?(left/right)").lower()
        if left_or_right == "left":
            ans = input("Good!, you picked the right option.Follow the tape and check ontop or behind to find the missing coins (ontop/behind)")

            if ans =="behind":
                print("yay!,you found the tape and won the 20 coins.")

            elif  ans == "ontop":
                print("Oooop! sorry you lost 10 coins already")

                coins -=10
                ans = input("To recover your lost coin,decide on the path to follow,head or tail to claim the remaining 10(head/tail)")
                if ans == "tail":
                    print("GREAT! you win")

                else:
                    print("Try again")

        else:
            print("Try again")

    else:
        print("log out...")

else:
    print("you are not old enough for the game")



























