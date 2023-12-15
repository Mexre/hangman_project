from random import randrange
words = [
    "wolf", "passion", "settlement", "judgment", "sensitive", "shatter", "aisle", "appetite",
    "battery", "cheese", "fitness", "linger", "grounds", "winner", "noble", "candle", "potential", "formal",
    "comfortable", "wealth", "midnight", "fixture", "voucher", "qualified", "helicopter", "characteristic",
    "autonomy", "rehabilitation", "superintendent", "architecture", "contemporary", "observation", "inhabitant"
    ]
hidden = words[randrange(len(words))]

guessed_letters = []
max_rounds = 10
cnt = 0

while cnt <= max_rounds - 1:
    cnt += 1
    if guessed_letters == list():
        print(f"\033[1mguessed letters so far: ")
    else:
        print(f"\nguessed so far: {guessed_letters}")
    print(f"round {cnt} out of {max_rounds}")

    while True:
        letter = input("guess a letter: ")  # user input check
        letter.lower()
        if len(letter) != 1:
            print("Error. Please give ONE letter")
        elif not letter.isalpha():
            print("Error. Letters only please")
        elif letter in guessed_letters:
            print("You have already guessed that letter!")
        else:
            guessed_letters.append(letter)
            break

    print(f"The letter {letter} appears {hidden.count(letter)} times")

    found = True
    for char in hidden:
        if char not in guessed_letters:
            print("_", end="")
            found = False
        else:
            print(char, end="")
    print("")
    if found:
        print("Good job you found the word")    # player won
        break
else:   # player lost
    print("+" + "-"*30 + "+")
    print("|" + "you lost".center(30) + "|")
    print("|" + f"the word was: {hidden}".center(30) + "|")
    print("+" + "-"*30 + "+")
