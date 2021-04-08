from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Ini Blockchain kata"

if __name__ == '__main__':
    app.run()
