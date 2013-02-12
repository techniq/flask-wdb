from flask import Flask
from wdb import Wdb as _Wdb


class Wdb(object):

    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        if app.debug:
            app.wsgi_app = _Wdb(app.wsgi_app)

            # Patch app.run to disable Werkzeug debugger
            app.run = self._run

    def _run(self, *args, **kwargs):
        kwargs["use_debugger"] = False
        return Flask.run(self.app, *args, **kwargs)
