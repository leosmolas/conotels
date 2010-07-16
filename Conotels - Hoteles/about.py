from PyQt4 import QtCore, QtGui

from ui.about import Ui_aboutThis

class AboutDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_aboutThis()
		self.ui.setupUi(self)
		
	
	def __init__(self,parent = None):
		super(AboutDialog, self).__init__(parent)
		
		self.setup()