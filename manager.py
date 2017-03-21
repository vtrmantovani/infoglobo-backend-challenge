#!/usr/bin/env python
from flask_script import Manager
from ibc import create_app

app = create_app()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
