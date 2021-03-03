# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
letters_guessed = []

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    strword = ''.join(letters_guessed)
    
    if strword == secret_word:
      return True
    else:
      return False
      


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    strlist = []
    for c in secret_word:
      if c in letters_guessed:
        strlist.append(c)
      elif c == " ":
        strlist.append(" ")
      else:
        strlist.append("_")
    return ''.join(strlist)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s = "abcdefghijklmnopqrstuvwxyz"
    for c in letters_guessed:
      if c in s:
        s = s.replace(c, "")
    return s 
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * 1 At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * 2 The user should start with 6 guesses

    * 3 Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * 4 Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * 5 The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * 6 After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6                                                                     #1 and #2
    warnings_remain = 3
    while guesses > 0 and len(letters_guessed) != len(secret_word):
      if guesses == 6 :
        print(f"You have {guesses} guesses.")
      else:                                                                      #3
        print(f"You have {guesses} guesses left.")
      print(get_available_letters(letters_guessed))
      
      while True:
        letter = input("Please select a letter: ")[0]                            #4
        if letter.isalpha: 
          break
        else:
          if warnings_remain >= 1:
            warnings_remain -= 1
            print(f"warnings remain: {warnings_remain}")
          else:
            guesses -= 1
            print(f"One guess penalty! Guesses: {guesses}")
            
          
      if letter in secret_word:                                                  #5 and #6
        letters_guessed.append(letter)
        print(get_guessed_word(secret_word,letters_guessed))
      elif letter in "bcdfghjklmnpqrstvwxy": 
        guesses -= 1
      elif letter in "aeiou":
        guesses -= 2

    if guesses == 0:
      print("Better luck next time ;)")

    if is_word_guessed(secret_word, letters_guessed):
       print(f"Congrats you won, the word is {secret_word}") 
    #score
    secretlist = []
    for c in secret_word:
      secretlist.append(c)
    score1 = len(secretlist)
    print(f"Your score is: {guesses*score1}")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i = 0
    new_word = my_word.strip(" ")
    if len(new_word) == len(other_word):
      for c in new_word:
        if c != "_" and c == other_word[i]:
            i += 1
            continue
        elif c == "_":
          i += 1
          continue
        else:
          return False
      return True
    else:
      return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    ''' 
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for item in wordlist:
      if match_with_gaps(my_word,item):
        print(item, end=" ")
    print()
        
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    rounds = 1                                                                    #1 and #2
    warnings_remain = 3
    while guesses > 0 and len(letters_guessed) != len(secret_word):
      print(f"Round {rounds}")
      if guesses == 6 :
        print(f"You have {guesses} guesses.")
      else:                                                                      #3
        print(f"You have {guesses} guesses left.")
      print(get_available_letters(letters_guessed))
      
      while True:
        letter = input("Please select a letter: ")[0]                            #4
        if letter.isalpha and letter != "*":
          rounds += 1 
          break
        elif letter == "*" and rounds != 1:
            print("Possible matches are: ")
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        else:
          if warnings_remain >= 1:
            warnings_remain -= 1
            print(f"warnings remain: {warnings_remain}")
          else:
            guesses -= 1
            print(f"One guess penalty! Guesses: {guesses}")
            
          
      if letter in secret_word:                                                  #5 and #6
        letters_guessed.append(letter)
        print(get_guessed_word(secret_word,letters_guessed))
      elif letter in "bcdfghjklmnpqrstvwxy": 
        guesses -= 1
      elif letter in "aeiou":
        guesses -= 2
      

    if guesses == 0:
      print("Better luck next time ;)")

    if is_word_guessed(secret_word, letters_guessed):
       print(f"Congrats you won, the word is {secret_word}") 
    #score
    secretlist = []
    for c in secret_word:
      secretlist.append(c)
    score1 = len(secretlist)
    print(f"Your score is: {guesses*score1}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
