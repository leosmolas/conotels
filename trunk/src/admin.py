from PyQt4 import QtCore, QtGui

from ui.admin import Ui_Admin
from unidad import UnidadDialog
from tipo import TipoDialog
from reserva import ReservaDialog
from huesped import HuespedDialog

class Admin(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_Admin()
		self.ui.setupUi(self)

		self.modifBut = self.ui.buttonBox.addButton("Modificar", QtGui.QDialogButtonBox.ActionRole)
		self.elimBut = self.ui.buttonBox.addButton("Eliminar", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.modifBut, QtCore.SIGNAL("clicked()"),
				self.on_modifBut_clicked)
		QtCore.QObject.connect(self.elimBut, QtCore.SIGNAL("clicked()"),
				self.on_elimBut_clicked)

	def __init__(self, nombre, parent=None):
		super(Admin, self).__init__(parent)

		self.dialog = None

		if nombre == "Huesped":
			self.dialog = HuespedDialog
		elif nombre == "Reserva":
			self.dialog = ReservaDialog
		elif nombre == "Tipo":
			self.dialog = TipoDialog
		elif nombre == "Unidad":
			self.dialog = UnidadDialog

		self.setup()
	
	def __del__(self):
		pass

	@QtCore.pyqtSlot()
	def on_modifBut_clicked(self):
		print "modif"
		diag = self.dialog()
		diag.exec_()
	
	@QtCore.pyqtSlot()
	def on_elimBut_clicked(self):
		print "elim"

		ret = QtGui.QMessageBox.question(self, "Esta seguro?", "Esta seguro que desea eliminar?",
			QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)

		if ret == QtGui.QMessageBox.Ok:
			print "Eliminando"
		else:
			print "Chau chau"
