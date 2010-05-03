# -*- coding: utf-8 -*-
from copy import deepcopy
from PyQt4 import QtCore, QtGui

from huesped import HuespedDialog

from ui.admin import Ui_Admin
from unidad import UnidadDialog
from tipo import TipoDialog
from reserva import ReservaDialog
from huesped import HuespedDialog

from models.tipo import Tipo
from models.unidad import Unidad
from models.huesped import Huesped
from models.reserva import Reserva

class Admin(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_Admin()
		self.ui.setupUi(self)

		self.nuevoBut = self.ui.buttonBox.addButton("&Agregar", QtGui.QDialogButtonBox.ActionRole)
		self.modifBut = self.ui.buttonBox.addButton("&Modificar", QtGui.QDialogButtonBox.ActionRole)
		self.elimBut = self.ui.buttonBox.addButton("&Eliminar", QtGui.QDialogButtonBox.ActionRole)

		self.nuevoBut.setIcon(QtGui.QIcon(":/add.png"))
		self.modifBut.setIcon(QtGui.QIcon(":/edit.png"))
		self.elimBut.setIcon(QtGui.QIcon(":/delete.png"))

		QtCore.QObject.connect(self.modifBut, QtCore.SIGNAL("clicked()"),
				self.on_modifBut_clicked)
		QtCore.QObject.connect(self.elimBut, QtCore.SIGNAL("clicked()"),
				self.on_elimBut_clicked)
		QtCore.QObject.connect(self.nuevoBut, QtCore.SIGNAL("clicked()"),
				self.on_nuevoBut_clicked)

	def __init__(self, conn, nombre,mainWin, parent=None):
		super(Admin, self).__init__(parent)

		self.dialog = None
		self.type = None

		self.conn = conn

		self.nombre = nombre
		self.uiMain = mainWin #agregado por Jona

		if nombre == "Huesped":
			self.dialog = HuespedDialog
			self.type = Huesped(self.conn)
		elif nombre == "Reserva":
			self.dialog = ReservaDialog
			self.type = Reserva(self.conn)
		elif nombre == "Tipo":
			self.dialog = TipoDialog
			self.type = Tipo(self.conn)
		elif nombre == "Unidad":
			self.dialog = UnidadDialog
			self.type = Unidad(self.conn)

		self.setup()
		self.loadAll()

		self.ui.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
	
	def loadAll(self):
		self.type.loadAll()
		self.ui.tableView.setModel(self.type.model)
		if self.nombre == "Unidad":
			self.ui.tableView.setColumnHidden(6,True) #Oculto el id del Tipo de la tabla Unidad
		elif self.nombre == "Reserva":
			self.ui.tableView.setColumnHidden(11,True)
			self.ui.tableView.setColumnHidden(12,True)
		self.ui.tableView.resizeColumnsToContents()

	@QtCore.pyqtSlot()
	def on_modifBut_clicked(self):
		if self.ui.tableView.currentIndex().row() == -1:
			QtGui.QMessageBox.information(self, "Advertencia", "Debe seleccionar una fila para poder modificar",
			QtGui.QMessageBox.Ok)
			return

		row = self.type.model.record(self.ui.tableView.currentIndex().row())
		
		if self.nombre == "Tipo":
			id = row.field(0).value().toInt()[0]
			nombre = row.field(1).value().toString()
			alta = row.field(2).value().toInt()[0]
			baja = row.field(3).value().toInt()[0]
			desc = row.field(4).value().toString()
			diag = self.dialog(self.conn, id,nombre,alta,baja,desc,mainWin=self.uiMain)
		elif self.nombre == "Unidad":
			id = row.field(0).value().toInt()[0]
			numero = row.field(1).value().toString()
			tipo = row.field(6).value().toInt()[0]
			capacidad = row.field(3).value().toInt()[0]
			desc = row.field(4).value().toString()
			estado = row.field(5).value().toString()
			diag = self.dialog(self.conn, id,numero,tipo,capacidad,desc,estado,mainWin=self.uiMain)
		elif self.nombre == "Reserva":
			id = row.field(0).value().toInt()[0]
			unidad = row.field(11).value().toInt()[0]
			huesped = row.field(12).value().toInt()[0]
			inicioPreres = row.field(3).value().toString()
			finPreres = row.field(4).value().toString()
			inicioRes = row.field(5).value().toString()
			finRes = row.field(6).value().toString()
			horaCheckIn = row.field(7).value().toString()
			horaCheckOut = row.field(8).value().toString()
			estado = row.field(9).value().toString()	
			temporada = row.field(10).value().toString()	
			diag = self.dialog(self.conn, id, unidad, huesped, inicioPreres, finPreres, inicioRes, finRes, horaCheckIn, horaCheckOut, estado, temporada, mainWin=self.uiMain)
		elif self.nombre == "Huesped":
			id = row.field(0).value().toInt()[0]
			dni = row.field(1).value().toString()
			apellido = row.field(2).value().toString()
			nombre = row.field(3).value().toString()
			tel = row.field(4).value().toString()
			cel = row.field(5).value().toString()
			direccion = row.field(6).value().toString()
			localidad = row.field(7).value().toString()
			diag = self.dialog(self.conn, id,dni,apellido,nombre,tel,cel,direccion,localidad,mainWin=self.uiMain)
		diag.exec_()
		self.loadAll()
	
	@QtCore.pyqtSlot()
	def on_elimBut_clicked(self):
		print "elim"
		if self.ui.tableView.currentIndex().row() == -1:
			QtGui.QMessageBox.information(self, "Advertencia", "Debe seleccionar una fila para poder eliminar",
			QtGui.QMessageBox.Ok)
			#self.uiMain.statusBar.showMessage("Debe seleccionar una fila antes de eliminar",3000)
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

	@QtCore.pyqtSlot()
	def on_nuevoBut_clicked(self):
		if self.nombre == "Huesped":
			self.uiMain.title.setTitle("Nuevo Huesped")
			self.uiMain.widgets.insertWidget(2, HuespedDialog(self.conn,mainWin=self.uiMain)) #modif
		
		elif self.nombre == "Reserva":
				self.uiMain.title.setTitle("Nueva Reserva")
				self.uiMain.widgets.insertWidget(2, ReservaDialog(self.conn,mainWin=self.uiMain)) #modif
		
		elif self.nombre == "Unidad":
				self.uiMain.title.setTitle("Nueva Unidad")
				self.uiMain.widgets.insertWidget(2, UnidadDialog(self.conn,mainWin=self.uiMain)) #modif
		
		elif self.nombre == "Tipo":
				self.uiMain.title.setTitle("Nuevo Tipo")
				self.uiMain.widgets.insertWidget(2, TipoDialog(self.conn,mainWin=self.uiMain)) #modif
		self.uiMain.widgets.setCurrentIndex(2)
