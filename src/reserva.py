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
	def __init__(self, unidad = 0, huesped = "", inicioPrereserva = "", finPrereserva = "", inicioReserva = "", finReserva = "", horaCheckIn = "", horaCheckOut = "", estado = "", mod = 0, parent = None):
		super(ReservaDialog, self).__init__(parent)
		self.setup()
		
		self.model = Reserva()
		self.modif = (mod != 0)
		self.unidad = unidad
		self.huesped = huesped
		self.inicioPrereserva = inicioPrereserva
		self.finPrereserva = finPrereserva
		self.inicioReserva = inicioReserva
		self.finReserva = finReserva
		self.horaCheckIn = horaCheckIn
		self.horaCheckOut = horaCheckOut
		self.estado = estado

	def __del__(self):
		pass
		
	def save(self):
		if self.modif:
			# db.save
			print "modify"
		else:
			# db.addNew
			print "new"
			self.model.save(unidad=self.ui.unidadLine.text(),
					huesped=self.ui.huespedLine.text(),
                                        inicioPrereserva=self.ui.inicioPreDate.date().toString("YYYY-MM-DD"),
                                        finPrereserva=self.ui.finPreDate.date().toString("YYYY-MM-DD"),
					inicioReserva=self.ui.inicioDate.date().toString("YYYY-MM-DD"),
					finReserva=self.ui.finDate.date().toString("YYYY-MM-DD"),
					horaCheckIn=self.ui.inTime.time().toString("HH:MM:SS"),
					horaCheckOut=self.ui.outTime.time().toString("HH:MM:SS"),
					estado=self.estadoCombo.itemText(self.estadoCombo.currentIndex()))
	
	def clear(self):
		self.ui.unidadLine = 0
		self.ui.huespedLine = ""
		self.ui.inicioPreDate.setDate(QtCore.QDate.currentDate)
		self.ui.finPreDate  = ""
		self.ui.inicioDate = ""
		self.ui.finDate = ""
		self.ui.inTime = ""
		self.ui.outTime
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

#import sys

#app = QtGui.QApplication(sys.argv)
#main = reservaDialog()
#main = reservaDialog("nroUnidad", "dnihuesped", "fechaIniPreReserva", "fechaFinPreReserva", "fechaIniReserva", "fechaFinReserva", "HoraCheckIn", "HoraCheckOut", "estado", 1)
#main.show()
#sys.exit(app.exec_())
