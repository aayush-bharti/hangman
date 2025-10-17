import random
from english_words import get_english_words_set

# use the built in english words library to get a list of english words
words_list = list(get_english_words_set(['web2'], lower=True, alpha=True))
# choose a random word from the list
word = random.choice(words_list)

if __name__ == "__main__":
    # print(f"word: {word}")
    print("Welcome to Hangman!")
    print("Enter a Letter to Guess")
    
    # set to keep track of guessed letters and attempts
    guessed_letters = set()
    attempts = 6
    
    # as long as there are still attempts left
    while attempts > 0:
        # display the current state of the word
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()
        
        # ask the player to guess a letter or the whole word
        guess_type = input("Do you want to guess a letter or the whole word? (l/w): ").lower()

        # if the player wants to guess a letter
        if guess_type == 'l':
            # store the guess
            guess = input("Your guess: ").lower()
            # validate the input
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            
            # check if the letter has already been guessed
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue
            
            # check if the guessed letter is in the word
            if guess in word:
                # add the letter to the set of guessed letters
                guessed_letters.add(guess)
                print("Good guess!")
                # if all letters are guessed, the player wins
                if all(letter in guessed_letters for letter in word):
                    print(f"Congratulations! You've guessed the word: {word}")
                    break
                
            # else decrease attempts
            else:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
            
        # if the guess type was a word
        elif guess_type == 'w':
            # store the input
            guess = input("Your guess: ").lower()
            # if the guessed word is correct, the player wins
            if guess == word:
                print(f"Congratulations! You've guessed the word: {word}")
                break
            # else decrease attempts
            else:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
        
        # if the input was invalid, prompt again
        else:
            print("Invalid choice. Please enter 'l' to guess a letter or 'w' to guess the whole word.")
            continue

        # print the number of attempts remaining
        print("Attempts Remaining: ", attempts)
        
        # if no attempts left, the game is over
        if attempts == 0:
            print(f"Game Over! The word was: {word}")