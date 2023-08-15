from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET'])
def add_film():
    return render_template('add_film.html')


if __name__ == '__main__':
    app.run(debug=True)