import random

user_win=0
computer_win=0
choice=["rock","paper","scissor"]


while True:
    user_guess=input("Enter 'Rock'/'Paper'/'Scissor' or 'q' to quit the game :").lower()

    if user_guess=="q":
        break

    if user_guess not in choice :
        print("Something Wrong ! Please Type Correctly")
        continue

    random_value=random.randint(0,len(choice)-1)
    computer_choice=choice[random_value]

    if user_guess=="rock" and computer_choice=="scissor":
        print("You Won :)")
        user_win+=1
        print("computer Choice is :",computer_choice)
        print("Your score is :",user_win)
        print("Computer score is :",computer_win)

    
    elif user_guess=="paper" and computer_choice=="rock":
        print("You Won :)")
        user_win+=1
        print("computer Choice is :",computer_choice)
        print("Your score is :",user_win)
        print("Computer score is :",computer_win)

    elif user_guess=="scissor" and computer_choice=="paper":
        print("You Won :)")
        user_win+=1
        print("computer Choice is :",computer_choice)
        print("Your score is :",user_win)
        print("Computer score is :",computer_win)

    else:
        print("Computer Won ! ")
        computer_win+=1
        print("Computer score is :",computer_win)
        print("Your score is :",user_win)

print("Final Result")
print("User Wins",user_win,"times.")
print("Computer Wins",computer_win,"times.")