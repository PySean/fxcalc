#!/usr/bin/python
"""
    "main.py", by Everyone
    Hello, world!
"""

import sys
from PyQt4 import QtGui

from ButtonClickerModel import ButtonClickerModel as BCM
from ButtonClickerControl import ButtonClickerControl as BCC
from ButtonClickerView import ButtonClickerView as BCV

def main():
    app = QtGui.QApplication(sys.argv)
    model = BCM()
    control = BCC(model)
    view = BCV(control, model)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
