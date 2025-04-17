import random
import time

operator=["*","+","-"]
min_value=8
max_value=20
total_problem=10



def probgenerator():
    left=random.randint(min_value,max_value)
    right=random.randint(min_value,max_value)
    ope=random.choice(operator)
    express=str(left)+" "+ope+" "+str(right)
    ans=eval(express)
    return express,ans
print("Maths Quiz Problem : Medium Level")
print("Total 10 Question,Let's see how much time you take for this quiz to solve! ")
input("Press 'Enter' to start ")
print("------------------------")
start_time=time.time()
wrong=0

for i in range(total_problem):
    express,ans=probgenerator()
    while True:
        guess=int(input("Problem #"+str(i+1)+ ": "+express+" = " ))
        if guess==ans:
            break
        wrong+=1
        print("Wrong Answer,Try again")

end_time=time.time()
total_time=round(end_time-start_time)

print("you solved total problem in",total_time,"seconds")
print("wrong answer:",wrong,"times")


