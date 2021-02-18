import random
from hangman import stages
from hangman import word_list

lives = 6

chosen_word = random.choice(word_list)

display = []
for i in chosen_word:
    display += "_"
print(display)

endgame = False

while not endgame:
    guess = input("Guess a letter:" ).lower()
    word_length = int(len(chosen_word))
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            endgame = True
            print('dead')
    print(f"{' '.join(display)}")

    if "_" not in display:
        endgame = True
        print("You win")

    print(stages[lives])
        
