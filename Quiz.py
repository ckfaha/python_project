#Quiz Game 
print("Welcome to my quiz game :) ")

play=input("Do you want to play this game : yes/no ").lower()

if play!="yes":
    quit()
score=0
print("Let's Play :) ")
print("There are 10 questions in this quiz! , Let's See How much you answer the question correctly :) ")

quiz=input("what 'CPU' Stands for ? " ).lower()
if quiz=="central processing unit" :
    print("Correct answer :) ")
    score+=1
else:
    print("Incorrect answer x ")

quiz=input("what 'AI' Stands for ? " ).lower()
if quiz=="artificial intelligence" :
    print("Correct answer :) ")
    score+=1
else:
    print("Incorrect answer x ")

quiz=input("what 'RAM' Stands for ? " ).lower()
if quiz=="random access memory" :
    print("Correct answer :) ")
    score+=1

else:
    print("Incorrect answer x ")

quiz=input("what 'ROM' Stands for ? " ).lower()
if quiz=="read only memory" :
    print("Correct answer :) ")
    score+=1
else:
    print("Incorrect answer x ")

quiz=input("what 'CSK' Stands for in IPL ? " ).lower()
if quiz=="chennai super kings" :
    print("Correct answer :) ")
    score+=1
else:
    print("Incorrect answer x ")

quiz=input("what 'MI' Stands for in IPL ? " ).lower()
if quiz=="mumbai indians" :
    print("Correct answer :) ")
    score+=1
else:
    print("Incorrect answer x ")

quiz=input("what 'RCB' Stands for in IPL ? " ).lower()
if quiz=="royal challengers bengaluru" :
    print("Correct answer :) ")
    score+=1
else:
    print("Incorrect answer x ")

quiz=input("what 'RR' Stands for in IPL ? " ).lower()
if quiz=="rajasthan royals" :
    print("Correct answer :) ")
    score+=1
else:
    print("Incorrect answer x ")

quiz=input("what 'GT' Stands for in IPL ? " ).lower()
if quiz=="gujarat titans" :
    print("Correct answer :) ")
    score+=1
else:
    print("Incorrect answer x ")

quiz=input("what 'SRH' Stands for in IPL ? " ).lower()
if quiz=="sunrisers hyderabad" :
    print("Correct answer :) ")
    score+=1
else:
    print("Incorrect answer x ")

print("You are Totally "+str(score)+"/10 Correct :)")

if score >=8 :
    print("You are Excellent")

elif score >=5 and score < 8 :
    print("Good, You have to Improve!")

else :
    print("Bad Luck * ^ *")