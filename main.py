from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "<h1>Hello World!</h1><br><a href='/index'>Перейти на вторую страницу</a>"

@app.route('/index/<x>/<y>')
def index(x, y):
    return f'Результат {float(x) + float(y)}'


if __name__ == '__main__':
    app.run()
