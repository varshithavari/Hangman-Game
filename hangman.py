import random

# Hangman visual stages
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """, """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """, """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """, """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """, """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """, """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """, """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Word lists with clues
word_clues = {
    "easy": {
        "cat": "A small domesticated feline.",
        "book": "You read it, often with pages.",
        "fish": "Lives in water, swims with fins.",
        "sun": "The star at the center of our solar system.",
        "tree": "A tall plant with a trunk and branches.",
        "milk": "A white liquid produced by mammals."
    },
    "medium": {
        "python": "A programming language or a snake.",
        "planet": "Orbits a star in space.",
        "bottle": "Holds liquids, made of glass or plastic.",
        "window": "You can see through it in a house or car.",
        "school": "A place where you go to learn.",
        "garden": "A piece of ground for growing flowers or vegetables."
    },
    "hard": {
        "developer": "A person who writes code and builds software.",
        "algorithm": "Step-by-step process to solve a problem.",
        "keyboard": "You use this to type into a computer.",
        "database": "Stores and organizes large amounts of information.",
        "terminal": "A command-line interface for users.",
        "compiler": "Translates code into machine-readable form."
    }
}

# Main game function
def play_game():
    print("\n🎮 Welcome to Hangman!")
    print("Choose difficulty: Easy, Medium, Hard")

    # Get difficulty level
    difficulty = ""
    while difficulty.lower() not in word_clues:
        difficulty = input("Enter difficulty level: ").lower()

    word, clue = random.choice(list(word_clues[difficulty].items()))
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    max_attempts = len(HANGMAN_PICS) - 1
    attempts = 0
    hint_used = False

    print(f"\n🔍 Clue: {clue}")

    while attempts < max_attempts and "_" in guessed_word:
        print(HANGMAN_PICS[attempts])
        print("Word:", " ".join(guessed_word))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        
        guess = input("Enter a letter or type 'hint': ").lower()

        if guess == "hint":
            if not hint_used:
                print(f"🧠 Hint: {clue}")
                # Reveal one random unrevealed letter
                unrevealed_indices = [i for i, ltr in enumerate(guessed_word) if ltr == "_"]
                if unrevealed_indices:
                    idx = random.choice(unrevealed_indices)
                    revealed_letter = word[idx]
                    guessed_word[idx] = revealed_letter
                    guessed_letters.add(revealed_letter)
                    hint_used = True
                    print(f"🎁 Bonus! A letter '{revealed_letter}' has been revealed.")
                else:
                    print("All letters already revealed.")
            else:
                print(f"📌 Clue reminder: {clue}")
                print("⚠️ You've already used the bonus letter reveal.")
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("❌ Wrong!")
            attempts += 1

    # Final result
    print(HANGMAN_PICS[attempts])
    if "_" not in guessed_word:
        print(f"🎉 You won! The word was: {word}")
    else:
        print(f"💀 You lost. The word was: {word}")

# Game loop
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing Hangman!")
        break
