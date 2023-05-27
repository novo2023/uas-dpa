from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "hello world"

@app.route('/testing')
def testing():
    return "testing"

@app.route('test2')
def test2():
    return "test2"

if __name__ == '__main__':
    app.run()