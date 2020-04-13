#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cleo import Application

from .command import PipexecCommand


application = Application()
application.add(PipexecCommand())

if __name__ == '__main__':
    application.run()
