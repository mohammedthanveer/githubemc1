name = input("type your name: ")
print("welcome", name, "to this adventure")

answer = input("you are on a dirt road, it has come to an end and you can go left or right which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("you can swam accross and were eaten by alligator")
    elif amswer == "walk":
        print("you walked for many miles, ran out of water")
    else:
        print("not a valid option.you loose.")

elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross or not(cross/back)?")

    if answer == "back":
        print("you go back to the main road.")
    elif answer == "cross":
        answer = input("you cross the bridge speak with stranger (yes/no)? ")
        
        if answer == "yes":
            print("you talk to the stranger")

        elif answer == "no":
            print("ignore the stranger")
    else:
        print("not a valid option.you loose.")


else:
    print("not a valid option. you loose.")