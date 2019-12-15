from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

lives = 0
setWord = []
dashWord = []

@app.route('/')
def lets_play():
    return render_template("lets_play.html")

@app.route('/test')
def home():
    global lives
    global setWord
    global dashWord
    return render_template("index.html")

@app.route('/start', methods = ["POST"])
def start():
    global lives
    global setWord
    global dashWord
    return render_template("game_data.html")

@app.route('/check', methods = ["POST"])
def check():
    global lives
    global setWord
    global dashWord

    lives = int(request.form["lives"])
    setWord = list(request.form["setWord"])
    dashWord = list(request.form["dashWord"])

    return render_template("game_main.html", lives=lives, setWord=setWord, dashWord=dashWord)


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug=True)