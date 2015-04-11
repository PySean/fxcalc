from PyQt4.QtCore import QObject

class ButtonClickerModel(QObject):
   def __init__(self):
      super().__init__()
      this.clicks = 0

   def incrementClicks(self):
      self.clicks += 1
      #TODO : Signal

   def getClicks(self):
      return self.clicks
      #TODO : synchronize?
