from ButtonClickerModel import ButtonClickerModel
from PyQt4 import QtCore

class ButtonClickerControl():

    def __init__(self, model):
        self.model = model
        self.fselect = {"ClickButton":self.increment}

    def handle(self, sender):
        self.fselect[sender.text()]()

    def increment(self):
        self.model.incrementClicks()
