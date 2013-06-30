from flask import Flask
from flask_wdb import Wdb

app = Flask(__name__)
app.debug = True
Wdb(app)


@app.route("/")
def main():
    return 'It works'

@app.route("/error")
def error():
    raise Exception("Kaboom!")

if __name__ == "__main__":
    app.run()
