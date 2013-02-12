Flask-Wdb
=========

Integrate Wdb instead of Werkzeug debugger for Flask applications

Usage
-----

    from flask import Flask
    from flask_wdb import Wdb

    app = Flask(__name__)
    app.debug = True
    Wdb(app)

    app.run()