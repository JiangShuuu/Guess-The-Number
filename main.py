#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).



from random import randint
from art import logo   #7

EASY_LEVEL_TURNS = 10   #3
HARD_LEVEL_TURNS = 5    #3


#4 Function to check user's guess against actual answer
#turn #6
def check_answer(guess, answer, turns):  #add turns #6
  if guess > answer:
    print("Too high.")
    return turns - 1   #turns -= 1 #6
  elif guess < answer:
    print("Too low.")
    return turns -1    #turns -= 1 #6
  else:
    print(f"You got it! The answer was {answer}.")

#3 Make function to set difficulty

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == "easy":
    #global turns
    #turns = EASY_LEVEL_TURNS
    return EASY_LEVEL_TURNS
  else:
    #turns = HARD_LEVEL_TURNS
    return HARD_LEVEL_TURNS

def game():   #5
  print(logo)  #7
#1 Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"real_ans: {answer}")

  turns = set_difficulty()   #3.1  turns = 0
  

  #5 Repeat the guessing functionality if they get it wrong
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")  #3.1 #6.1

  #2 Let the user guess a number
    guess = int(input("Make a guess: "))
    #check_answer(guess, answer, turns)  #4.1  #6 add turns
    turns = check_answer(guess, answer, turns)  #6.1
    if turns == 0:          #6.2
      print("You've run out of guesses, you lose.")   
      return
    elif guess != answer:   #6.2
      print("Guess again")


game()   #5



#6 Track the number of turns and reduce by 1 if they get it wrong
























# from replit import clear
# import random
# round = True

# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# real_ans = random.randint(0, 100)
# level_choose = input ("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# easy_life = 10
# hard_life = 5

# if level_choose == "easy":
#   print(f"You have {easy_life} attempts remaining to guess the number")
#   user_choose = input ("Make a guess = ")
#   while round :   
#     if int(user_choose) > real_ans and easy_life >= 1:
#       print("Too hight")
#       easy_life -= 1
#       print(f"You have {easy_life} attempts remaining to guess the number")
#       user_choose = input ("Make a guess = ")
#     elif int(user_choose) < real_ans and easy_life >= 1:
#       print("Too low")
#       easy_life -= 1
#       print(f"You have {easy_life} attempts remaining to guess the number")
#       user_choose = input ("Make a guess = ")
#     elif easy_life == 0:
#       print("You lose")
#       round = False
#     else:
#       print("You win")
#       round = False
# elif level_choose == "hard":
#   print(f"You have {hard_life} attempts remaining to guess the number")
#   user_choose = input ("Make a guess = ")
#   while round :
#     if int(user_choose) > real_ans and hard_life > 1:
#       print("Too hight")
#       hard_life -= 1
#       print(f"You have {hard_life} attempts remaining to guess the number")
#       user_choose = input ("Make a guess = ")
#     elif int(user_choose) < real_ans and hard_life > 1:
#       print("Too low")
#       hard_life -= 1 
#       print(f"You have {hard_life} attempts remaining to guess the number")
#       user_choose = input ("Make a guess = ")
#     elif hard_life == 0:
#       print("You lose")
#       round = False
#     else:
#       print("You win")
#       round = False
# else:
#   print("keyin again")