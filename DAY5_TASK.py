import random
'''
#Task1 - get each user 10 games
count1 = 0
count2 = 0

for i in range(1, 11):
    player1 = input(f"Enter your choice - game {i} --> Rock, Paper, Scissors: ").lower().strip()
    player2 = random.choice(["rock", "paper", "scissors"])

    print("Player1:", player1)
    print("Player2:", player2)

    if player1 == player2:
        print("Draw")

    elif (player1 == "rock" and player2 == "scissors"):
        print("Player1 won")
        count1 += 1
        
    elif (player1 == "paper" and player2 == "rock"):
        print("Player1 won")
        count1 += 1
        
    elif (player1 == "scissors" and player2 == "paper"):
        print("Player1 won")
        count1 += 1
        
    else:
        print("Player2 won")
        count2 += 1

    print("Score:", count1, "-", count2)
    print()

    if count1 == 6:
        print("Player1 won the game series!")
        break

    elif count2 == 6:
        print("Player2 won the game series!")
        break

else:
    print("Series end")
    
    if count1 > count2:
        print("Player1 won the game series")
    elif count2 > count1:
        print("Player2 won the game series")
    else:
        print("Series Draw")
'''
#Task2 - get ur choice -> rps,ng,study

def Rps():
    count1 = 0
    count2 = 0

    for i in range(1, 11):
        player1 = input(f"Enter your choice - game {i} --> Rock, Paper, Scissors: ").lower().strip()
        player2 = random.choice(["rock", "paper", "scissors"])

        print("Player1:", player1)
        print("Player2:", player2)

        if player1 == player2:
            print("Draw")

        elif (player1 == "rock" and player2 == "scissors"):
            print("Player1 won")
            count1 += 1
            
        elif (player1 == "paper" and player2 == "rock"):
            print("Player1 won")
            count1 += 1
            
        elif (player1 == "scissors" and player2 == "paper"):
            print("Player1 won")
            count1 += 1
            
        else:
            print("Player2 won")
            count2 += 1

        print("Score:", count1, "-", count2)
        print()

        if count1 == 6:
            print("Player1 won the game series!\n")
            break

        elif count2 == 6:
            print("Player2 won the game series!\n")
            break

    else:
        print("Series end")
        
        if count1 > count2:
            print("Player1 won the game series")
            print()
        elif count2 > count1:
            print("Player2 won the game series")
            print()
        else:
            print("Series Draw")
            print()

def Ng():
    c = 0
    n = 20
    for i in range(3):

        g = random.randint(1, n)

        guess = int(input(f"Guess the number between 1 and {n}: "))

        if guess > 0 and guess <= n:

            print("Guess:", guess)
            print("OG No:", g)

            if guess == g:
                print("You won the game")
                c = 1
                break

            else:
                print("Try again")
                n = n // 2

        else:
            print(f"Please enter a number between 1 and {n}")

    if c == 0:
        print("You lost the game. Go and study")
        print()

def main():
    game=0
    while(game!='3'):
        game=input("""enter the your choose:
                   1.Rock,Paper,Scissors Game
                   2.Guessing Number Game
                   3.You want to Study
                   Enter 1/2/3:""")
        print()
        if(game=='1'):
            Rps()
        elif(game=='2'):
            Ng()
        elif(game=='3'):
            print("You want to Study, go and concentrate in it")
            break
        else:
            print("you want to enter based on the choose 1,2,3")
            continue
main()
    
