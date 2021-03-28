# Needed Modules
import random

# Create a function that determines if the user has won the game
def hasUserWon(word, guesses):

  # Let's use an "Innocent Until Proven Guilty" Algorithm...
  # ...and create a variable that is set to "True"
  won = True

  # Go through each letter in the secret word
  for letter in word:

    # Check if the letter has been guessed
    if(letter not in guesses):

      # If it has NOT been guessed, set the variable we created to False, and stop the loop
      won = False
      break

  return won

# Create a function that displays the secret word
def displaySecretWord(word, guesses):
 
  # Go through each letter in the secret word, and determine HOW we display it
  for letter in word:
 
    # If this letter (from the secret word) has been guessed, display the letter
    if(letter in guesses):
      print(letter, end=" ")
    # Otherwise, display an underscore ( _ )
    else:
      print("_", end=" ")

#Computer chooses a secret word
secretWord = ["Wizard","Saturday","Jump", "travel"]
#put that secret word in a list
guessList = (random.choice(secretWord))
#print(guessList)
correct =[]
strike = 0
while strike < 5 and not hasUserWon(guessList,correct ): 
  # choose letter from user
  letter = "wrong"
  while len(letter) != 1:
    letter = input("Please enter one letter ")
  

  # make sure secret word has the letter
  if letter in guessList:
    correct.append(letter) 
    displaySecretWord(guessList,correct)
    print("This is the right answer " )
    
  else:
    print("This is the wrong letter" )
    strike = strike + 1
    print(strike)
if hasUserWon(guessList, correct ):
  print("You Won!")
else:
  print("You lose!")