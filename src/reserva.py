from PyQt4 import QtCore, QtGui

from ui.reserva import Ui_reservaDialog
# from db.tipo import SARASA

class ReservaDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_reservaDialog()
		self.ui.setupUi(self)
		
		self.okBut = self.ui.buttonBox.addButton("Ok", QtGui.QDialogButtonBox.ActionRole)
		self.cancelBut = self.ui.buttonBox.addButton("Cancel", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.cancelBut, QtCore.SIGNAL("clicked()"),
				self.on_cancelBut_clicked)
		#llenar combobox de estado
		#hacer consultas para buscar huespedes y unidades libres para reserva?
		
		#unidad, huesped, inicioprereserva, finprereserva,  inicioreserva, finreserva, horacheckin, horacheckout, estado
	def __init__(self, unidad = 0, huesped = "", inicioPrereserva = "", finPrereserva = "", inicioReserva = "", finReserva = "", horaCheckIn = "", horaCheckOut = "", estado = "", mod = 0, parent = None):
		super(ReservaDialog, self).__init__(parent)
		self.setup()

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
		
	def save(self):
		if self.modif:
			# db.save
			print "modify"
		else:
			# db.addNew
			print "new"
	
	def clear(self):
		print "HOLAAA"
		self.ui.unidadLine.setText("")
		self.ui.huespedLine.setText("")
		self.ui.inicioPreDate.setDate(QtCore.QDate.currentDate())
		self.ui.finPreDate.setDate(QtCore.QDate.currentDate())
		self.ui.inicioDate.setDate(QtCore.QDate.currentDate())
		self.ui.finDate.setDate(QtCore.QDate.currentDate())
		self.ui.inTime.setTime(QtCore.QTime.currentTime())
		self.ui.outTime.setTime(QtCore.QTime.currentTime())
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
