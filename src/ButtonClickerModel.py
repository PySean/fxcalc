from PyQt4.QtCore import QObject,pyqtSignal

class ButtonClickerModel(QObject):
   newClicks = pyqtSignal(name='newClicks')

   def __init__(self):
      super().__init__()
      self.clicks = 0

   def incrementClicks(self):
      self.clicks += 1
      self.newClicks.emit()

   def getClicks(self):
      return self.clicks

   def getClickUpdates(self,func):
      self.newClicks.connect(func)

