import random
import words from words

# def main():
#     startButton = input('Press y to Begin Playing, Press Anything Else to End')
#     gameStart = True
#     while startButton == 'y':
#         pickWord(words)
#         hangman()



def pickWord(words):
    word = random.choice(words) # random word choice

    return word.upper()

def hangman():
    word = pickWord(words)
    lives = 7
    
    while lives > 0 and 
