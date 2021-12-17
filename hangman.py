import random 
import time
import sys

print("Welcome to Hangman By SmashedFrenzy16")
time.sleep(2)
print("Starting Hangman...")
time.sleep(2)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["daffodil", "ocean", "bicycle", "rainbow"]
    word_guesses = []
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def keep_playing():
    global kplaying
    kplaying = input("Do you want to keep playing? (y/n)")
    if kplaying == "y" or kplaying == "Y":
        main()
    elif kplaying == "n" or kplaying == "N":
        sys.exit()
    else:
        print("Sorry that was not recognized, program now exiting.")
        sys.exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is how long the word is: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >=2 or guess <= "9":
        print("Invalid Input, try using letters instead of numbers, and remember to only guess a letter at a time. \n")
        hangman()
    
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    
    elif guess in already_guessed:
        print("Use another letter. \n")
    
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("------\n"
                "|\n"    
                "|\n"
                "|\n"
                "|\n"
                "|\n"
                "-------\n")
            print("Not a letter in the word. " + str(limit-count) + " guesses remaining.")
        
        elif count == 2:
            time.sleep(1)
            print("------\n"
                "|    |\n"
                "|    |\n"
                "|\n"
                "|\n"
                "|\n"
                "-------\n")
            print("Not a letter in the word. " + str(limit-count) + " guesses remaining")
        
        elif count == 3:
            time.sleep(1)
            print("------\n"
                "|    |\n"
                "|    |\n"
                "|    |\n"
                "|\n"
                "|\n"
                "-------\n")
            print("Not a letter in the word. " + str(limit-count) + " guesses remaining")

        elif count == 4:
            time.sleep(1)
            print("------\n"
                "|    |\n"
                "|    |\n"
                "|    |\n"
                "|    0\n"
                "|\n"
                "-------\n")
            print("Not a letter in the word. " + str(limit-count) + " guesses remaining.")
        
        elif count == 5:
            time.sleep(1)
            print("------\n"
                "|    |\n"
                "|    |\n"
                "|    |\n"
                "|    0\n"
                "|    \/\n"
                "|\n"
                "-------\n")
            print("Not a letter in the word. " + str(limit-count) + " guesses remaining.")

        elif count == 5:
            time.sleep(1)
            print("------\n"
                "|    |\n"
                "|    |\n"
                "|    |\n"
                "|    0\n"
                "|    \/\n"
                "|    /\ \n"
                "-------\n")
            print("Unlucky! You got hanged!")
            print("The word was: " + already_guessed + word)
        keep_playing()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        keep_playing()
    elif count != limit:
        hangman()
main()

hangman()


    


        
