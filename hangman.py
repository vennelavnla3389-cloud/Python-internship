import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
wrong_guesses = 0
max_wrong_guesses = 6

# Display the starting message
print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the complete word has been guessed
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Game over message
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)