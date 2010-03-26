from PyQt4 import QtCore, QtGui

from ui.tipo import Ui_tipoDialog
# from db.tipo import SARASA

class tipoDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_tipoDialog()
		self.ui.setupUi(self)
		
		# Llenar el comboBox de Tipo

	def __init__(self,nombre = "", costoTempAlta = 0, costoTempBaja = 0, mod = 0, parent = None):
		super(tipoDialog, self).__init__(parent)
		self.setup()

		self.modif = (mod == 0)
		self.nombre = nombre
		self.costoTempAlta = costoTempAlta
		self.costoTempBaja = costoTempBaja
		
	def save(self):
		if self.modif:
			# db.save
			print "modify"
		else:
			# db.addNew
			print "new"
	
	@QtCore.pyqtSlot()
	def on_buttonBox_accepted(self):
		self.save()
	
	@QtCore.pyqtSlot()
	def on_buttonBox_rejected(self):
		self.close()

import sys

app = QtGui.QApplication(sys.argv)
main = tipoDialog()
main = tipoDialog("a",1,1,1)
main.show()
sys.exit(app.exec_())
