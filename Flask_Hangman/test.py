from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

lives = 0
setWord = []
dashWord = []
tofill = 0
flag = 0
already_guessed = []

def hangman_fun(guess):
    global lives
    global tofill
    global flag
    global setWord
    global dashWord

    for x in range(0,len(dashWord),1):
        if setWord[x] == guess:
            if dashWord[x] == "_":
                dashWord[x] = guess
                tofill = tofill - 1
                flag = 1
    
@app.route('/')
def lets_play():
    global already_guessed
    already_guessed = []
    return render_template("lets_play.html")

@app.route('/test')
def home():
    global tofill
    tofill = 0
    return render_template("index.html")

@app.route('/start', methods = ["POST"])
def start():
    return render_template("game_data.html")

@app.route('/check', methods = ["POST"])
def check():
    global lives
    global setWord
    global dashWord
    global tofill
    tofill = 0
    already_guessed = []

    lives = int(request.form["lives"])
    setWord = list(request.form["setWord"])
    setWord = [x.lower() for x in setWord]
    dashWord = list(request.form["dashWord"])
    dashWord = [x.lower() for x in dashWord]

    if(len(setWord) != len(dashWord)):
        return render_template("game_data.html", jsol = 1)
    else:
        for x in range(0,len(dashWord),1):
            if dashWord[x] == "_" :
                tofill = tofill + 1

    return render_template("game_main.html", lives=lives, tofill=tofill, dashWord=dashWord)

@app.route('/work', methods = ["POST"])
def work():
    global lives
    global setWord
    global dashWord
    global tofill
    global already_guessed
    global flag
    test = 0
    flag = 0
    guess = request.form["GUESS"]
    guess = guess.lower()
    
    if len(already_guessed) == 0:
        already_guessed.append(guess)
        hangman_fun(guess)
    else:
        for i in range(0,len(already_guessed),1):
            if already_guessed[i] == guess:
                flag = 1
                test = 1
                break

    if test == 0:
        already_guessed.append(guess)
        hangman_fun(guess)

    if test == 1:
        return render_template("game_main.html", jsol = 1, lives=lives, setWord=setWord, tofill=tofill, dashWord=dashWord, flag = flag, already_guessed = already_guessed, check = 1)

    if flag == 0:
        lives = lives - 1

    if lives > 0 and tofill > 0:
        return render_template("game_main.html", lives=lives, setWord=setWord, tofill=tofill, dashWord=dashWord, flag = flag, already_guessed = already_guessed, check = 2)
    else:
        return render_template("game_over.html", lives=lives, setWord=setWord)
    

if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug=True)