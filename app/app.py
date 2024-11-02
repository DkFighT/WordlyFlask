from flask import Flask, render_template, url_for, request, jsonify
import random

app = Flask(__name__)


def get_word():
    with app.open_resource('static/labels.txt') as f:
        mass = f.readlines()
        word = (random.choice(mass)).decode('utf8')
    return word[:-2]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game_screen():
    word = get_word()
    return render_template('game.html', secure_word=word)

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()