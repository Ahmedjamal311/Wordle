import random

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def is_valid_guess(guess, guesses):
    return guess in guesses

def evaluate_guess(guess, word):
    result = [''] * 5
    word_char_used = [False] * 5
    guess_char_used = [False] * 5

    for i in range(5):
        if guess[i] == word[i]:
            result[i] = f"\033[32m{guess[i]}"
            word_char_used[i] = True
            guess_char_used[i] = True

    for i in range(5):
        if not guess_char_used[i]:
            for j in range(5):
                if guess[i] == word[j] and not word_char_used[j]:
                    result[i] = f"\033[33m{guess[i]}"
                    word_char_used[j] = True
                    break
            else:
                result[i] = f"\033[0m{guess[i]}"

    return ''.join(result) + "\033[0m"


def wordle(guesses, answers):
    print("Welcome to Wordle! You have 6 tries to guess a five letter word")
    secret_word = random.choice(answers)

    tries = 1
    maxTries = 6

    while tries <= maxTries + 1:
        guess = input("Enter Guess #" + str(tries) + ": ").lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        
        if not is_valid_guess(guess, guesses):
            print("Invalid word. Please enter a real English word.")
            continue

        if guess == secret_word:
            if tries == 1:
                print("Congratulations! You guessed the word in " + str(tries) + " try!")
            else:
                print("Congratulations! You guessed the word in " + str(tries) + " tries!")
            break

        tries += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)

        if tries == maxTries + 1:
            print("You Lost. The secret word was: " + str(secret_word))
            check = input("Would you like to play again? (Yes or No): ")
            if check.lower() == "yes":
                print("")
                wordle(guesses, answers)
            else:
                print("Goodbye")
                break  
    
    if tries <= maxTries:
            check = input("Would you like to play again? (Yes or No): ")
            if check.lower() == "yes":
                print("")
                wordle(guesses, answers)
            else:
                print("Goodbye")
                return  

guesses = load_dictionary("Wordle\guesses.txt")
answers = load_dictionary("Wordle\correct.txt")

wordle (guesses, answers)