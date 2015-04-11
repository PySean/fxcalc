"""
    "ButtonClickerViewer.py", by Sean Soderman
    A simple window with a button for clicking. 
    Registers the button with a listener for incrementing.
"""
from PyQt4 import QtGui, QtCore
from ButtonClickerControl import ButtonClickerControl
from ButtonClickerModel import ButtonClickerModel

class ButtonClickerView(QtGui.QMainWindow):
    def __init__(self, controller, model): 
        super(ButtonClickerView, self).__init__()
        self.controller = controller
        self.model = model
        self.initUI()

        self.model.getClickUpdates(self.refreshUI)

    def initUI(self):
        inc_button = QtGui.QPushButton('ClickButton', self)
        self.inc_label = QtGui.QLabel('0', self)
        self.inc_label.move(20, 20)
        inc_button.clicked.connect(self.buttonClicked)
        self.show()
        
    def buttonClicked(self):
        sender = self.sender()
        self.controller.handle(sender)

    def refreshUI(self):
        self.inc_label.setText(str(self.model.getClicks()))
