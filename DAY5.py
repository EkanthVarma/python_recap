'''
random module --> helps to generate random values
ex: OTP generation,Story Generation, Games (Rock Ppaer Scissiors)
Game
'''
import random,time
#random number generation --> OTP (time module helps to use time functions)
a =random.randint(1000,9999)
#print(a)
for i in range(5):
    time.sleep(2) #sleep(seconds) --> helps for a waiting period
    print(random.randint(1000,9999))
    #time.sleep(2)

#Playing a Game (Rock Paper Scissors)
#Two players --> ame -->
player1 = input("Enter one of these --> Rock,Paper,Scissors: ").lower().strip()
player2 = random.choice(["Rock","Paper","Scissors"]).lower()
print("Player1: ",player1)
print("Player2: ",player2)
if player1 == "rock" and player2 == "paper":
    print("Player2 won")
elif player1 == "paper" and player2 == "scissors":
    print("Player2 won")
elif player1 == "scissors" and player2 == "rock":
    print("Player2 won")
elif player1 == player2:
    print("Draw")
else:
    print("Player1 won")

#Get score for each user and declare the winner
#play the game for 10 times --> Task (Push to Github and share it (Tasks))

#Task:2 --> Give user a choice --> Rps(1) / Ng(2) /study(3)

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

#Bussiness Card generator --> name,phonenumber,emailid,websitelink
#segno --. pipi install segno

import segno
#print(dir(segno))
from segno import helpers
qr = helpers.make_mecard(name = "Seera Ekanth Varma",
                         email = "ekanthvarma2005@gmail.com",
                         phone = "+91 7674071873",
                         url = "https://www.linkedin.com/in/ekanthvarmaseera/")
print(qr)
qr.save("mycard.png",scale=10)

#now its your turn -> explore modules (Tuesday --> 15th Sep) -- Instagram, Youtube, Email Automation .....



