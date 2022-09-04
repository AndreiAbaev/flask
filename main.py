from flask import Flask, render_template
import csv
import city_parser


city_parser.run()
app = Flask(__name__)


@app.route('/')
@app.route('/small')
def small():
    with open('Малые города.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        return render_template('small.html', reader=reader)


@app.route('/medium')
def medium():
    with open('Средние города.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        return render_template('medium.html', reader=reader)


@app.route('/big')
def big():
    with open('Большие города.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        return render_template('big.html', reader=reader)


@app.route('/bigger')
def bigger():
    with open('Крупные города.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        return render_template('bigger.html', reader=reader)


@app.route('/biggest')
def biggest():
    with open('Крупнейшие города.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        return render_template('biggest.html', reader=reader)


@app.route('/millionaire')
def millionaire():
    with open('Города-миллионеры.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        return render_template('millionaire.html', reader=reader)


if __name__ == '__main__':
    app.run()
