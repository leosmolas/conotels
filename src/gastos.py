from PyQt4 import QtCore, QtGui

from ui.gastos import Ui_GastosDialog
# from db.unidad import SARASA

class GastosDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_GastosDialog()
		self.ui.setupUi(self)

		self.okBut = self.ui.buttonBox.addButton("Guardar", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)

	def __init__(self, parent = None):
		super(GastosDialog, self).__init__(parent)

		self.setup()

	def save(self):
		# db.save
		print "hola"
	
	def clear(self):
		self.ui.gastoSpin.setValue(0)
		self.ui.descripcionLine.setText("")

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		self.save()
