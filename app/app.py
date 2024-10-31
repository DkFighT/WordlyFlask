from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game_screen():
    return render_template('game.html', secure_word='слово')


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()