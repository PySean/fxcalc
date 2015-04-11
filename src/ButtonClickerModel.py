from PyQt4.QtCore import QObject,pyqtSignal

class ButtonClickerModel(QObject):
   newClicks = pyqtSignal(name='newClicks')

   def __init__(self):
      super().__init__()
      this.clicks = 0

   def incrementClicks(self):
      self.clicks += 1
      #TODO : Signal

   def getClicks(self):
      return self.clicks
      #TODO : synchronize?
