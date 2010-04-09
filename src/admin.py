from copy import deepcopy
from PyQt4 import QtCore, QtGui

from ui.admin import Ui_Admin
from unidad import UnidadDialog
from tipo import TipoDialog
from reserva import ReservaDialog
from huesped import HuespedDialog

from models.tipo import Tipo
from models.unidad import Unidad
from models.huesped import Huesped

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
		self.type = None

		self.nombre = nombre

		if nombre == "Huesped":
			self.dialog = HuespedDialog
			self.type = Huesped()
		elif nombre == "Reserva":
			self.dialog = ReservaDialog
		elif nombre == "Tipo":
			self.dialog = TipoDialog
			self.type = Tipo()
		elif nombre == "Unidad":
			self.dialog = UnidadDialog
			self.type = Unidad()

		self.setup()
		self.loadAll()

		self.ui.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
	
	def loadAll(self):
		self.type.loadAll()
		self.ui.tableView.setModel(self.type.model)

	@QtCore.pyqtSlot()
	def on_modifBut_clicked(self):
		print "modif"

		if self.ui.tableView.currentIndex().row() == -1:
			QtGui.QMessageBox.information(self, "Error", "Debe seleccionar una fila antes de modificar",
			QtGui.QMessageBox.Ok)
			return

		row = self.type.model.record(self.ui.tableView.currentIndex().row())
		
		if self.nombre == "Tipo":
			id = row.field(0).value().toInt()[0]
			nombre = row.field(1).value().toString()
			alta = row.field(2).value().toInt()[0]
			baja = row.field(3).value().toInt()[0]
			desc = row.field(4).value().toString()
			diag = self.dialog(id,nombre,alta,baja,desc)
		elif self.nombre == "Unidad":
			id = row.field(0).value().toInt()[0]
			numero = row.field(1).value().toString()
			tipo = row.field(2).value().toInt()[0]
			capacidad = row.field(3).value().toInt()[0]
			desc = row.field(4).value().toString()
			# ESTADOOOO
			diag = self.dialog(id,numero,tipo,capacidad,desc)
#        elif self.nombre == "Reserva":
		elif self.nombre == "Huesped":
			id = row.field(0).value().toInt()[0]
			dni = row.field(1).value().toString()
			apellido = row.field(2).value().toString()
			nombre = row.field(3).value().toString()
			tel = row.field(4).value().toString()
			diag = self.dialog(id,dni,apellido,nombre,tel)
		diag.exec_()
		self.loadAll()
	
	@QtCore.pyqtSlot()
	def on_elimBut_clicked(self):
		print "elim"
		if self.ui.tableView.currentIndex().row() == -1:
			QtGui.QMessageBox.information(self, "Error", "Debe seleccionar una fila antes de eliminar",
			QtGui.QMessageBox.Ok)
			return
		ret = QtGui.QMessageBox.question(self, "Esta seguro?", "Esta seguro que desea eliminar?",
			QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)

		if ret == QtGui.QMessageBox.Ok:
			print "Eliminando"
			row = self.type.model.record(self.ui.tableView.currentIndex().row())
			self.type.delete(row.field(0).value().toString())
			self.loadAll()
		else:
			print "Chau chau"
