from flask import Flask

app = Flask(__name__)


def read_file(path):
    f = open(path)
    text = f.read()
    f.close()
    return text

@app.route('/')
def main_page():
    return read_file("index.html")


app.run()
