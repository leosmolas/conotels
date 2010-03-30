from PyQt4 import QtCore, QtGui

from ui.reserva import Ui_reservaDialog
# from db.tipo import SARASA

class reservaDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_reservaDialog()
		self.ui.setupUi(self)
		
		#llenar combobox de estado
		#hacer consultas para buscar huespedes y unidades libres para reserva?
		
		
		#unidad, huesped, inicioprereserva, finprereserva,  inicioreserva, finreserva, horacheckin, horacheckout, estado
	def __init__(self, unidad = 0, huesped = "", inicioPrereserva = "", finPrereserva = "", inicioReserva = "", finReserva = "", horaCheckIn = "", horaCheckOut = "", estado = "", mod = 0, parent = None):
		super(reservaDialog, self).__init__(parent)
		self.setup()

		self.modif = (mod == 0)
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
	
	@QtCore.pyqtSlot()
	def on_buttonBox_accepted(self):
		self.save()
	
	@QtCore.pyqtSlot()
	def on_buttonBox_rejected(self):
		self.close()

import sys

app = QtGui.QApplication(sys.argv)
main = reservaDialog()
main = reservaDialog("nroUnidad", "dnihuesped", "fechaIniPreReserva", "fechaFinPreReserva", "fechaIniReserva", "fechaFinReserva", "HoraCheckIn", "HoraCheckOut", "estado", 1)
main.show()
sys.exit(app.exec_())
