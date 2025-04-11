import random


try :
    number_guess=int(input("Enter a number :"))
    if number_guess<=0:
        print("Please Enter The Number Larger Than Zero ")
        quit()

    random_number=random.randint(0,number_guess)    #user_guess.isdigit() this method check the value is number or not if cond is true then if cond executes
    guess=0
    print
    while True:
        guess+=1
        user_guess=int(input("Guess the number:"))
        if user_guess==random_number:
            print("Your guess is right :) ")
            break
        else:
            print("You are wrong ,Try Again ")

    print(guess,"time to guess the correct one")
         


except Exception as e:
    print("Numbers only",e)