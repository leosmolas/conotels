from PyQt4 import QtCore, QtGui

from ui.mainwin import Ui_MainWindow
# from db.unidad import SARASA

import icons_rc

class MainWindow(QtGui.QMainWindow):
	def setup(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.addNewBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewBut.setText("Agregar nueva unidad")
		self.addNewBut.setIcon(QtGui.QIcon(":/add.png"))

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setup()

		self.options.currentItemChanged.connect(self.changePage)

	def changeView(self, current, previous):
		if not current:
			current = previous

		self.widgets.setCurrentIndex(self.options.row(current))

#   @QtCore.pyqtSlot()
#   def on_buttonBox_accepted(self):
#      self.save()
#   
#   @QtCore.pyqtSlot()
#   def on_buttonBox_rejected(self):
#      self.close()

import sys

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
