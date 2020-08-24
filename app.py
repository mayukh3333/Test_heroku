from flask import Flask, render_template
import flask
import random

app = Flask(__name__)
app = flask.Flask(__name__, template_folder="templates")

def printing():
    return random.randint(2 ,100)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('index.html', test_text = 'I can eat {} bananas'.format(printing()))

if __name__ == "__main__":
    app.run(debug=True)
