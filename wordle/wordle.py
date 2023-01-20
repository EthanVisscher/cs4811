import random


words = []      # Store all 5 letter words from file into list
viableWords = []
goal = "00000"  # Word to guess
attempt = 0     # Number of attempt currently on
guesses = []    # Previous words guessed
results = []    #
won = True      # Won the game
failed = False  # Failed the game

# Fills words with all 5 letter words
with open("words_alpha.txt") as file:
  for word in file:               # 1 word per line
    word = word.replace("\n", "") # Remove newline char 
    if len(word) == 5:
      words.append(word)


def playWordle():
  global words
  global viableWords
  global goal
  global attempt
  global won
  global failed

  goal = words[random.randint(0, len(words) - 1)]
  viableWords = words
  attempt = 0
  won = False
  failed = False


def makeGuess(word):
  global words
  global goal
  global attempt
  global guesses
  global results
  global won
  global failed

  if word == goal:
    print("You won!")
    won = True
    return
  
  attempt += 1
  if attempt == 6:
    print("You failed!")
    failed = True
    return

  guesses.append(word)
  
  result = ""
  for i in range(5):
    char = word[i]
    if char == goal[i]:
      result += "2"     # Correct spot
    elif char in goal:
      result += "1"     # Incorrect spot
    else:
      result += "0"     # Not in word

  results.append(result)

def giveUp():
  print("You failed!")
  failed = True


def showState():
  print(guesses)
  print(results)

def getNewGuess():
  global words
  global attempt
  global guesses
  global results

  if attempt == 0:
    guess = words[random.randint(0, len(words) - 1)]
  else:
    # Insert smart algorithm
    guess = words[random.randint(0, len(words) - 1)]

  return guess

# Start game
playWordle()

print(goal)

# Make guesses
while True:
  makeGuess(getNewGuess())
  
  # Game over, break out of loop
  if won == True or failed == True:
    break