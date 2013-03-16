Flask-Wdb
=========

Integrate `Wdb <https://github.com/Kozea/wdb>`_ instead of Werkzeug debugger for Flask applications

- Only enabled when `app.debug = True`
- Disables Werkzeug debugger automatically
- Expose configuration via app.config

Installation
------------
::

    $ pip install flask-wdb

Usage
-----
::

    from flask import Flask
    from flask_wdb import Wdb

    app = Flask(__name__)
    app.debug = True
    Wdb(app)

    app.run()

Configuration
-------------

``WDB_ENABLED`` Enable Wdb (default: app.debug)
``WDB_START_DISABLED`` Disable Wdb until an exception or wdb.set_trace() is encountered (default: False)
``WDB_THEME`` Change theme between 'dark' and 'light' (default: 'dark')