flag = 0
tofill = 0
def hangman_fun(dashWord_list,setWord,guess):
    global flag
    global lives
    global tofill
    for x in range(0,len(dashWord_list),1):
        if setWord[x] == guess:
            if dashWord_list[x] == "_":
                dashWord_list[x] = guess
                tofill = tofill - 1
                flag = 1

setWord = input("Enter the word you want your friend to guess: ")
setWord = setWord.lower()
dashWord = input("Enter the word with blanks ( For Example, if the word is manchester, word with blanks should be like ma___e__er): ")
dashWord = dashWord.lower()
lives = int(input("How many lives do you want to give to your friend: "))
x = 0
already_guessed = []

for x in range(0,len(setWord),1):
    if dashWord[x] == "_" :
        tofill = tofill + 1

dashWord_list = list(dashWord)

while lives > 0 and tofill > 0 :
    print(' '.join(dashWord_list))
    print("Lives left - {} and Blanks to fill - {}".format(lives,tofill))
    flag = 0

    guess = input("Guess a letter: ")

    if len(already_guessed) == 0:
        already_guessed.append(guess)
        hangman_fun(dashWord_list,setWord,guess)
    else:
        for i in range(0,len(already_guessed),1):
            if already_guessed[i] == guess:
                print("Already guessed this letter")
                flag = 1
                break
            else:
                already_guessed.append(guess)
                hangman_fun(dashWord_list,setWord,guess)

    if flag == 0:
        lives = lives - 1

if lives > 0:
    print("You have guessed the word ({}) correctly".format(setWord))
else:
    print("You have guessed the word wrongly. The word is {}".format(setWord))     
