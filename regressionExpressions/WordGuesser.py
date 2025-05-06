import re

def word_guesser(word):
    guessed_letters = set()
    attempts = 6  # Number of incorrect attempts allowed

    while attempts > 0:
        # Display the current state of the word
        masked_word = ''.join(
            letter if re.search(letter, ''.join(guessed_letters), re.IGNORECASE) else '_'
            for letter in word
        )
        print(f"\nWord: {masked_word}")
        
        if '_' not in masked_word:
            print("Congratulations! You've guessed the word!")
            return

        guess = input("Guess a letter: ").lower()

        if not re.match(r'^[a-zA-Z]$', guess):
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if not re.search(guess, word, re.IGNORECASE):
            attempts -= 1
            print(f"Incorrect! Attempts left: {attempts}")
        else:
            print("Good guess!")

    print(f"Out of attempts! The word was: {word}")

# Example usage
if __name__ == "__main__":
    word_guesser("elephant")

