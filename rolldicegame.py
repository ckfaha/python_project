import random


def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    players=int(input("how many players are here to play this game (2 - 4 ) only allowed :"))
    
    if players>=2 and players<=4:
        break

    else:
        print("Invalid no.of players,try again ")
print("who reached the point '20 ' first, he/she is the winner !")
max_score=20
player_score=[0 for _ in range(players)]    # [ 0 ,0 ,0 ,0 ]
while max(player_score)<max_score:
    #      0 .... 51   <    50
    for p_index in range(players):
        print("Player Number",p_index+1,"started:")
        print(p_index+1,", Total Score is :",player_score[p_index],)
        current_score=0
        
        while True:
            rolled=input("do you want to roll this dice ,press(d) : ").lower()
            if rolled !="d":
                break
            value=roll()

            if value==1 or value==2 or value==3 or value==4 or value==5 :
                print("You Rolled " , value ," ,Nice try ")
                current_score+=value
                break

            else:
                current_score+=value
                print("You Rolled :",value,"Bonus dice for '6' comes")

            print("Your Score is :",current_score)

        player_score[p_index]+=current_score
        print("Your total score is :",player_score[p_index])
    
max_score=max(player_score)
winning_index=player_score.index(max_score)
print("The winner is : player",winning_index+1," is the winner with the score of :",max_score)

        