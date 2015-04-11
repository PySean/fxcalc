"""
    "ButtonClickerViewer.py", by Sean Soderman
    A simple window with a button for clicking. 
    Registers the button with a listener for incrementing.
"""
from PyQt4 import QtGui, QtCore
from ButtonControlClicker import ButtonControlClicker
from ButtonControlModel import ButtonControlModel

class ButtonClickerViewer(QtGui.QMainWIndow):
    def __init__(self, controller, model): 
        super(ButtonClickerViewer, self).__init__()
        self.controller = controller
        self.model = model
        self.initUI()

        self.model.getClickUpdates(self.refreshUI)

    def initUI(self):
        inc_button = QtGui.QPushButton('ClickButton', self)
        self.inc_label = QtGui.QLabel('0', self)
        inc_button.clicked.connect(buttonClicked)
        
    def buttonClicked(self):
        sender = self.sender()
        self.controller.handle(sender)

    def refreshUI(self):
        self.inc_label.setText(str(self.model.clicks))
