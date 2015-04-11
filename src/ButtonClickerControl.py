from ButtonClickerModel import ButtonClickerModel
from PyQt4 import QtCore

class ButtonclickerControl():

    def __init__(self, model):
        self.model = model
        self.fselect = {"Button1":self.increment}

    def handle(self, sender):
        self.fselect[sender.text()]()

    def increment(self):
        self.model.incrementClicks()
