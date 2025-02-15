import random

hangman_stage = ['+---+\n    |\n    |\n    |\n   ===',
                 "+---+\nO   |\n    |\n    |\n   ===",
                 "+---+\nO   |\n|   |\n    |\n   ===",
                 " +---+\n O   |\n/|   |\n     |\n    ===",
                 " +---+\n O   |\n/|\  |\n     |\n    ===",
                 " +---+\n O   |\n/|\  |\n/    |\n    ===",
                 " +---+\n O   |\n/|\  |\n/ \  |\n    ==="]
words = []  # Initialize list

with open("words.txt", "r") as file:  # Ensure the correct filename
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        words.append(line)  # Store words in list
        
word = random.choice(words)

currentGuesses = []
correctGuesses = []
wrongGuesses = []

word_letters = [ch for ch in word]

for x in range(len(word_letters)): # creates empty guess
    currentGuesses.append("_")

counter = 0
while counter < 6:
    inputchoice = input("Do you want to guess a letter or guess the word: ")

    if inputchoice.lower() in ["word","a word"]:
        guess = input("Input your word guess: ")
        if guess == word:
            print("Correct! Good Job!")
        else:
            print("Incorrect")
            counter += 1
            print(hangman_stage[counter])
            print(f"Current Correct Guesses: {' '.join(currentGuesses)}")
            print(f"Current Wrong Guesses: {wrongGuesses}")


    if inputchoice.lower() in ["a letter", "letter"]:
        guess = input("Input your letter guess: ")

        if guess in word and guess not in correctGuesses: # second part prevents repetition
            correctGuesses.append(guess)
            for x in range(len(word_letters)):
                if word_letters[x] == guess:
                    currentGuesses[x] = guess

        else:
            if guess not in wrongGuesses: # prevents repetition
                wrongGuesses.append(guess)
                counter+= 1

        print(hangman_stage[counter])
        madeWord = ''.join(currentGuesses)
        madeWord2 = ' '.join(currentGuesses)
        print(f"Current correct guesses: {madeWord2}")


        if madeWord == word:
            print("Good Job! You found the word and saved Jeff")
            break
        
        print(f"Current wrong guesses: {', '.join(wrongGuesses)}")

print("Sadly you didn't guess the word in time and Jeff has been hung")
print(f"The word was {word}")




    

