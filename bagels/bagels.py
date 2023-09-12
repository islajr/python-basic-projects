import random

NUM_DIGITS = 3
MAX_GUESSES = 10

print(f"""Bagels, by Archer.
A deductive logic game where you must guess a number based on clues.
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
Pico - One digit is correct but in the wrong position
Fermi - One digit is correct and in the right position
Bagels - No digit is correct""")


def main():
    while True:
        num_guesses = 1
        guess = ""
        secret = getSecretNumber()
        while num_guesses <= MAX_GUESSES:
            # Requesting for input
            print("I've come up with a number. Can you guess it?")
            # while (guess.isdecimal() is False) and (guess != NUM_DIGITS):
            guess = input("> ")
            num_guesses += 1    # incrementing the guess counter

            # comparing guess to secret
            answer = getClues(secret, guess)
            if guess == secret:
                print("You are correct!"
                      "Game is restarting!")
                break
            else:
                print(answer)

            if num_guesses == MAX_GUESSES:
                print(f"""You've run out of guesses, sorry!
                The answer was {secret}.
                Game is restarting""")
                break


def getSecretNumber():
    """Obtains a random 3-digit number"""
    secret = ""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(NUM_DIGITS):
        random.shuffle(numbers)
        secret += str(numbers[i])
    return secret


def getClues(secret, guess):
    """Compares secret to guess to provide appropriate clues"""
    clue = ""
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            clue = "Fermi! "
        if guess[i] in secret:
            clue += "Pico! "

    if len(clue) == 0:
        return "Bagels!"
    else:
        return clue


if __name__ == "__main__":
    main()
