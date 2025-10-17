import random

words_list = ['apple', 'banana', 'cherry', 'strawberry', 'orange', 'watermelon']
word = random.choice(words_list)

if __name__ == "__main__":
    print(f"word: {word}")
    
    print("Welcome to Hangman!")
    print("Enter a Letter to Guess")
    guessed_letters = set()
    attempts = 6
    
    while attempts > 0:
        guess = input("You guess: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                break
            
            else:
                for letter in word:
                    if letter in guessed_letters:
                        print(letter, end=' ')
                    else:
                        print('_', end=' ')
                print()
            
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=' ')
                else:
                    print('_', end=' ')
            print()