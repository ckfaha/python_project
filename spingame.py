import random

MIN_LINES=1
MAX_LINES=3
MIN_BET=1
MAX_BET=100

ROWS=3
COLS=3

SYMBOLS_COUNT={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

SYMBOLS_VALUES={
    "A":8,
    "B":5,
    "C":3,
    "D":2
}

def slot_machine_spin(rows,cols,symbol):
    all_symbol=[]
    for symbol,symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    column=[]
    for _ in range(cols):
        col=[]
        current_symbol=all_symbol[:]
        for _ in range(rows):
            value=random.choice(current_symbol)
            current_symbol.remove(value)
            col.append(value)
        column.append(col)
    return column

def print_slot_machine(column):
    for row in range(len(column[0])):
        for i,col in enumerate(column):
            if i!=len(column)-1:
                print(col[row], end=" | ")           #didn't und for col[row]

            else:
                print(col[row])
 

def check_winnings(lines,bet,columns,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line] 
        for column in columns:
            symbols_check=column[line]   
            if symbol!=symbols_check:
                break   
        else: 
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)

    
    return winnings,winning_lines


def deposit():
    while True:
        amount=input("Enter Deposit Amount : $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0 :
                break
            else:
               print("Invalid amount ")                                       
        else:                                                                                     
            print("Numbers Only Allowed")                                      

    return amount            

def no_of_lines():
    while True:
        lines=input("Enter Number of lines to bet('1-3') :")
        if lines.isdigit():
            lines=int(lines)
            if lines>=MIN_LINES and lines<=MAX_LINES  :
                break
            else:
               print("Invalid No.of.lines ")
        else:
            print("Numbers Only Allowed")

    return lines

def get_bet():
    while True:
        amount=input("How much do you bet on each line : $")
        if amount.isdigit():
            amount=int(amount)
            if amount>=MIN_BET and amount<=MAX_BET :
                break
            else:
               print(f"Bet amount must between ${MIN_BET}-${MAX_BET} ")
        else:
            print("Numbers Only Allowed")

    return amount            

def spin(balance):
    lines=no_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"You do not have enough balnce to bet on that,Your current balance is ${balance}")

        else:
            break

    print(f"you are betting ${bet} on {lines} line,total bet amount is ${total_bet}")

    slot=slot_machine_spin(ROWS,COLS,SYMBOLS_COUNT)
    print_slot_machine(slot)
    winnings,winning_lines=check_winnings(lines,bet,slot,SYMBOLS_VALUES)
    print(f"You won ${winnings}.")
    print(f"You won on lines:",*winning_lines)
    return winnings-total_bet

def main():
    balance=deposit()
    while True:
        if balance<=0:
            break
        print(f"Your current balance is ${balance}")
        ans=input("press any key to play or 'q' to quit this : ").lower()
        if ans=='q':
            break
        balance+=spin(balance)

main()