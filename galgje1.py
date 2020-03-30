# Importeer alle modules
import random
import time
import os
import platform
from sys import exit

clear = lambda: os.system('cls')

# Definieer de woordenlijst en de goed- en foutgeraden letters.
words = [
  "banaan", 
  "huis", 
  "tafel",
  "voorzichtige",
  "toneelspelen",
  "erdoor",
  "gestreden",
  "vanwege",
  "namens",
  "weerspiegelt",
  "werkzaamheden"
]
goedGeradenLetters = []
foutGeradenLetters = []

levens = 0

def vraagOpnieuwBeginnen():
  geenAntwoordGegeven = True
  while(geenAntwoordGegeven):
    antwoord = input("Wil je opnieuw beginnen? (j/n) ").lower()
    if antwoord == "j":
      geenAntwoordGegeven = False
    elif antwoord == "n":
      exit()

def resetGame():
  global levens
  global goedGeradenLetters
  global foutGeradenLetters
  del goedGeradenLetters[:]
  del foutGeradenLetters[:]
  levens = 0
  print("\n\n\n")

def quitGame():
  clear()
  print("Tot ziens!")
  time.sleep(1)
  exit()

def guessWord():
  global levens
  global bezig
  global correctWord
  clearScreen()
  printCharacters()
  woordRaad = input("Raad het geheime woord: ").lower()
  # Als er een of meer spaties in zitten
  if woordRaad == "qq":
    quitGame()  
  if woordRaad.count(' ') >= 1:
    print("Sorry, in een woord zitten geen spaties!")
  else:
    # Als het geraden woord juist is
    if word == woordRaad:
      print("Dat is het juiste woord! Gefeliciteerd!")
      vraagOpnieuwBeginnen()
      bezig = False
      correctWord = False
      resetGame()
    else:
      print("Dat is niet goed!")
      levens += 1
      print(asciiGalgje[levens - 1])

def checkCorrectWord():
  # Maak een set met alle letters in het woord, en vergelijk die met de goed geraden letters
  if len(set(word)) == len(goedGeradenLetters):
    return True
  else:
    return False

def printCharacters():
  global word
  global goedGeradenLetters
  print("")
  # Ga door alle karakters in het woord. Als een karakter voorkomt in de lijst met goed geraden letters, print dan de letter uit
  for i in word:
    if i in goedGeradenLetters:
      print(i, end="")
      # Ik gebruik end="" om ervoor te zorgen dat Python geen nieuwe regel print.
    else:
      print("-", end="")
  print("\n")

def titleBar():
  print("GALGJE\n\n")

def clearScreen():
  clear()
  titleBar()
  if(levens == 0):
    print("\n")
  else:
    print(asciiGalgje[levens - 1])
  print("\n")

def printGalgje():
  if (levens < 1):
    print("\n" * 7)
  else:
    print(asciiGalgje[levens - 1])

asciiGalgje = ["""






  ____""",
  """
  |
  |
  |
  |
  |
  |
  |___""",
  """
  |/
  |
  |
  |
  |
  |
  |___""",
  """  _________
  |/
  |
  |
  |
  |
  |
  |___""",
  """  _________
  |/       |
  |     ( ͡° ͜つ ͡°)
  |       /|\\╭∩╮
  |       / \\
  |
  |
  |___"""]

clear()

# Check if user is using Linux or MacOS (Darwin)
if(platform.system() == "Linux" or platform.system() == "Darwin"):
  print("         Dit programma maakt gebruik van een functie (clear) die alleen werkt onder Windows. Het programma zou zich vreemd kunnen gedragen.")
  input('         Druk op ENTER om dit te accepteren...')

while True:

  clear()
  levens = 0
  # Print welkomscherm
  print("Welkom bij galgje!\n" + asciiGalgje[4] + "\n")
  input('Druk op ENTER om te beginnen!...')
  clear()
  titleBar()

  # Bekijk hoeveel woorden er in de woordenlijst zitten
  amountOfWords = len(words)
  # Kies een random woord uit de lijst
  word = words[random.randint(0, amountOfWords - 1)]

  resetGame()

  firstTry = True
  
  bezig = True
  while bezig:

    if(firstTry):
      print("\n"*3)
      firstTry = False
    printCharacters()
    # Vraag om een character in te voeren, en zet het om in lowercase
    character = input("Raad een letter of typ ? om het woord te raden! ").lower()
    

    
    amountOfCharacters = len(character)
 
    
    # Als de speler "QQ" heeft ingevuld
    if character =="qq":
      quitGame()


    if amountOfCharacters == 1:
      if character == "?":
        clearScreen()
        print("Je wilt het geheime woord raden? OK!")
        guessWord()
      # Als de letter in het alfabet zit
      elif character.isalpha():
        # Als de letter al eens is geprobeerd
        if character in goedGeradenLetters or character in foutGeradenLetters:
          print("Sorry, maar je hebt al eens die letter geprobeerd. Probeer het opnieuw.")
          time.sleep(1)
          clear()
          titleBar()
          print(asciiGalgje[levens - 1])
        elif character in word:
          print("Die letter zit in het woord!")
          goedGeradenLetters.append(character)
          time.sleep(1)
          clear()
          titleBar()
          printGalgje()
        else:
          print("Die letter zit niet in het woord!")
          foutGeradenLetters.append(character)
          levens += 1
          time.sleep(1)
          clear()
          titleBar()
          printGalgje()
        

    else:
      print("Sorry, je kan maar een letter invullen. Probeer het opnieuw.\n")
    
    
    if len(set(word)) == len(goedGeradenLetters):
      correctWord = True
    else:
      correctWord = False
    if bezig:
      while(correctWord == True):
        print("Je hebt alle karakters geraden! Probeer nu het woord te raden.")
        guessWord()

    # Als je 5 fouten hebt gemaakt
    if levens >= 5:
      # Geef aan dat je hebt verloren en vraag of de speler opnieuw wilt beginnen
      print("Je hebt verloren! Het geheime woord was", word + ".")
      vraagOpnieuwBeginnen()
      bezig = False
      resetGame()