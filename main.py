import random
import hangman_words
import hangman_art
print(hangman_art.logo)

word = random.choice(hangman_words.word_list)
output = ["_"]*len(word)
lives = 6
print(output)

res = ""
dash = output.count("_")
while lives!=0 and dash!=0:
    guess = input(f"Please guess a letter to complete a word! \n").lower()
    for i in range(len(word)):
        if word[i]== guess:
            output[i]= guess
            dash = output.count("_")
    print(output)
    if guess not in word:
        print("Sorry you guesses a wrong letter. You lose one of your life")
        lives -=1
        print(hangman_art.stages[lives])

res = ""
for i in output:
    res += i
if word == res:
    print("Yayyy! You won the game!")
else:
    print(f"Sorry! Better luck next time!\nThe word you were looking for is {word}")