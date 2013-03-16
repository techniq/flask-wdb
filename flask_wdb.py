from flask import Flask
from wdb import Wdb as _Wdb


class Wdb(object):

    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(self.app)

    def init_app(self, app):
        if app.config.get('WDB_ENABLED', app.debug):

            start_disabled = app.config.get('WDB_START_DISABLED', False)
            theme = app.config.get('WDB_THEME', 'dark')

            app.wsgi_app = _Wdb(app.wsgi_app, start_disabled, theme)

            # Patch app.run to disable Werkzeug debugger
            app.run = self._run

    def _run(self, *args, **kwargs):
        kwargs["use_debugger"] = False
        return Flask.run(self.app, *args, **kwargs)
