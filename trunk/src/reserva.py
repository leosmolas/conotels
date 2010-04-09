# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui

from ui.reserva import Ui_reservaDialog
# from db.tipo import SARASA
from models.reserva import Reserva

class ReservaDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_reservaDialog()
		self.ui.setupUi(self)
		
		self.okBut = self.ui.buttonBox.addButton("Ok", QtGui.QDialogButtonBox.ActionRole)
		self.cancelBut = self.ui.buttonBox.addButton("Cancel", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_cancelBut_clicked)
		#llenar combobox de estado
		#hacer consultas para buscar huespedes y unidades libres para reserva?
		
		#unidad, huesped, inicioprereserva, finprereserva,  inicioreserva, finreserva, horacheckin, horacheckout, estado
	def __init__(self, id = -1, unidad = 0, huesped = "", inicioPrereserva = "", finPrereserva = "", inicioReserva = "", finReserva = "", horaCheckIn = "", horaCheckOut = "", estado = "", parent = None):
		super(ReservaDialog, self).__init__(parent)
		self.setup()
		
		self.model = Reserva()
		self.modif = (id != -1)
		self.id = id
#        self.unidad = unidad
#        self.huesped = huesped
#        self.inicioPrereserva = inicioPrereserva
#        self.finPrereserva = finPrereserva
#        self.inicioReserva = inicioReserva
#        self.finReserva = finReserva
#        self.horaCheckIn = horaCheckIn
#        self.horaCheckOut = horaCheckOut
#        self.estado = estado
		if self.modif:

	def save(self):
		self.model.save(id=self.id,unidad=self.ui.unidadLine.text(),
				huesped=self.ui.huespedLine.text(),
									inicioPrereserva=self.ui.inicioPreDate.date().toString("YYYY-MM-DD"),
									finPrereserva=self.ui.finPreDate.date().toString("YYYY-MM-DD"),
				inicioReserva=self.ui.inicioDate.date().toString("YYYY-MM-DD"),
				finReserva=self.ui.finDate.date().toString("YYYY-MM-DD"),
				horaCheckIn=self.ui.inTime.time().toString("HH:MM:SS"),
				horaCheckOut=self.ui.outTime.time().toString("HH:MM:SS"),
				estado=self.estadoCombo.itemText(self.estadoCombo.currentIndex()))
	
	def clear(self):
		self.ui.unidadLine.setText("")
		self.ui.huespedLine.setText("")
		self.ui.inicioPreDate.setDate(QtCore.QDate.currentDate)
		self.ui.finPreDate.setDate(QtCore.QDate.currentDate)
		self.ui.inicioDate.setDate(QtCore.QDate.currentDate)
		self.ui.finDate.setDate(QtCore.QDate.currentDate)
		self.ui.inTime.setDate(QtCore.QDate.currentDate)
		self.ui.outTime.setDate(QtCore.QDate.currentDate)
		self.ui.estadoCombo.setCurrentIndex(0)

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		self.save()
		self.clear()

		if self.modif:
			self.close()
	
	@QtCore.pyqtSlot()
	def on_cancelBut_clicked(self):
		self.clear()
		if self.modif:
			self.close()
