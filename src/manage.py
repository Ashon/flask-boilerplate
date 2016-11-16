#!/usr/bin/env python3

import flask_script
from application import app


manager = flask_script.Manager(app)


@manager.option('-h', '--host', dest='host', help='hostname')
@manager.option('-p', '--port', dest='port', help='port')
@manager.option('-c', '--conf', dest='config', help='config path')
def run(host, port, config):
    ''' Start server with development mode '''

    if config:
        app.config['CONFIG_PATH'] = config

    app.run(
        host=host, port=port,
        use_debugger=True,
        use_reloader=True
    )


if __name__ == '__main__':
    manager.run()
