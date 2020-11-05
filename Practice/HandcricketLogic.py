import random

digits = [0,1,2,3,4,5,6]

print("="*10 + " Hand cricket game " + "="*10)
print("\nLet's play")
print("\nIt's toss time")
toss = ["head", "tail"]
bat_or_bowl = ["bat", "bowl"]
toss_result = random.choice(toss)
print("\nhead or tail")
user_toss_input = input()

what_is_user_doing = None
what_is_cpu_doing = None

if user_toss_input == toss_result :
    print("\n Its {} and you have won the toss".format(toss_result))
    print("bat or bowl?")
    chosen = input()
    chosen_action = chosen
    print("\nYou will {} first".format(chosen_action))
    if chosen_action == "bat":
        what_is_user_doing = "bat"
        what_is_cpu_doing = "bowl"
    else:
        what_is_user_doing = "bowl"
        what_is_cpu_doing = "bat"

else:
    print("You have lost the toss")
    cpu_action = random.choice(bat_or_bowl)
    print("\nCPU will {} first".format(cpu_action))

    if cpu_action == "bat":
        what_is_user_doing = "bowl"
        what_is_cpu_doing = "bat"
    else:
        what_is_user_doing = "bat"
        what_is_cpu_doing = "bowl"

print("\nStart")

cpu_score = 0
user_score = 0
flag = None



#cpu batting first
if what_is_cpu_doing == "bat":
    while True :
        while flag != "out":
            print("CPU's current score", cpu_score)
            print("Your choice ")
            hand_digit = int(input())
            if hand_digit > 6 or hand_digit < 0:
                print("Wrong choice")
                continue
            cpu_digit = random.choice(digits)
            print("CPU choice")
            print(cpu_digit)
            if hand_digit != cpu_digit:
                cpu_score += cpu_digit
                continue

            if hand_digit == cpu_digit:
                print("\nCPU is out")
                flag = "out"
                print("Your target is {} runs".format(cpu_score+1))
                break

        if flag == "out":
            while user_score <= cpu_score:
                print("User current score", user_score)
                print("Your choice ")
                hand_digit = int(input())
                if hand_digit > 6 or hand_digit < 0:
                    print("Wrong choice")
                    continue
                cpu_digit = random.choice(digits)
                print("CPU choice")
                print(cpu_digit)

                if hand_digit != cpu_digit:
                    user_score += hand_digit
                    continue

                if hand_digit == cpu_digit :
                    print("\nYou are out")
                    print("You have scored {} runs".format(user_score))
                    break


        if cpu_score == user_score:
            print("Its a tie")
            print("User score:", user_score)
            print("CPU score:", cpu_score)
            break

        if cpu_score > user_score:
            print("CPU has won the game by {} runs".format(cpu_score - user_score))
            print("User score:", user_score)
            print("CPU score:", cpu_score)
            break

        if cpu_score <= user_score:
            print("Congratulations you have won the game")
            print("User score:", user_score)
            print("CPU score:", cpu_score)
            break

    print("THANKS FOR PLAYING")

#user batting first
else:
    flag = None
    while True :
        while flag != "out":
            print("User current score", user_score)
            print("Your choice ")
            hand_digit = int(input())
            if hand_digit > 6 or hand_digit < 0:
                print("Wrong choice")
                continue
            cpu_digit = random.choice(digits)
            print("CPU choice")
            print(cpu_digit)
            if hand_digit != cpu_digit:
                user_score += hand_digit
                continue

            if hand_digit == cpu_digit:
                print("\nYou are out")
                flag = "out"
                print("You have to defend {} runs".format(user_score+1))
                break

        if flag == "out":
            while cpu_score <= user_score:
                print("CPU's current score", cpu_score)
                print("Your choice ")
                hand_digit = int(input())
                if hand_digit > 6 or hand_digit < 0:
                    print("Wrong choice")
                    continue
                cpu_digit = random.choice(digits)
                print("CPU choice")
                print(cpu_digit)

                if hand_digit != cpu_digit:
                    cpu_score += cpu_digit
                    continue

                if hand_digit == cpu_digit :
                    print("\nCPU is out")
                    break


        if cpu_score == user_score:
            print("Its a tie")
            print("User score:", user_score)
            print("CPU score:", cpu_score)
            break

        if cpu_score > user_score:
            print("CPU has won the game")
            print("User score:", user_score)
            print("CPU score:", cpu_score)
            break

        if cpu_score <= user_score:
            print("Congratulations you have won the game")
            print("User score:", user_score)
            print("CPU score:", cpu_score)
            break

    print("THANKS FOR PLAYING")









