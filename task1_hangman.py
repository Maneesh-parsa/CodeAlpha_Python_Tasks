import random

def hangman():
    words = ["python", "code", "alpha", "hangman", "intern"]
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("\nWelcome to Hangman!")

    while attempts > 0 and '_' in guessed:
        print("\nWord:", ' '.join(guessed))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    if '_' not in guessed:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)