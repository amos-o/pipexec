#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pipexec import PipExec
from cleo import Application

application = Application()
application.add(PipExec())

if __name__ == '__main__':
    application.run()