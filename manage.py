#!/usr/bin/env python
from flask.ext.script import Manager
from flask_spirits.manage import user

from gpgcom.main import app


manager = Manager(app)

manager.add_command('user', user.manager)

if __name__ == '__main__':
    manager.run()
