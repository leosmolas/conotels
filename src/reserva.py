import re
from PyQt4 import QtCore, QtGui

from ui.reserva import Ui_reservaDialog

from models.huesped import Huesped
from models.unidad import Unidad

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
		#hacer consultas para buscar huespedes y unidades libres para reserva?

		self.ui.huespedView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

		QtCore.QObject.connect(self.ui.huespedLine, QtCore.SIGNAL("textChanged(const QString &)"),
			self.update)
		
	def __init__(self, conn, id = -1, unidad = 0, huesped = "", inicioPrereserva = "", finPrereserva = "", inicioReserva = "", finReserva = "", horaCheckIn = "", horaCheckOut = "", estado = "", mod = 0, parent = None):
		super(ReservaDialog, self).__init__(parent)

		self.conn = conn

		self.setup()

		self.huesped = Huesped(self.conn)
		self.huesped.loadAll()
		self.ui.huespedView.setModel(self.huesped.model)

		self.unidad = Unidad(self.conn)
		self.unidad.loadAll()
		self.ui.unidadCombo.setModel(self.unidad.model)
		self.ui.unidadCombo.setModelColumn(1)

		self.modif = (id != -1)
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
			self.ui.unidadCombo.setCurrentIndex(0)
			self.ui.huespedLine.setText("")
			self.ui.inicioPreDate.setDate(QtCore.QDate.currentDate())
			self.ui.finPreDate.setDate(QtCore.QDate.currentDate())
			self.ui.inicioDate.setDate(QtCore.QDate.currentDate())
			self.ui.finDate.setDate(QtCore.QDate.currentDate())
			self.ui.inTime.setTime(QtCore.QTime.currentTime())
			self.ui.outTime.setTime(QtCore.QTime.currentTime())
			self.ui.estadoCombo.setCurrentIndex(0)
		
	def update(self, s):
		filtro = re.escape(str(self.ui.huespedLine.text().replace(' ', '* ')))
		
		self.huesped.filterModel(filtro)
		self.ui.huespedView.setModel(self.huesped.model)

	def save(self):
		if self.ui.numeroLine.text() != "":
			comboModel = self.ui.tipoCombo.model()
			estad = "Libre"
			if self.ui.noDisponibleCheck.checkState() == QtCore.Qt.Checked:
				estad = "No Disponible"
			self.model.save(id=self.id,nombre=self.ui.numeroLine.text(),tipo=comboModel.data(comboModel.index(self.ui.tipoCombo.currentIndex(),0)).toInt()[0],
				capacidad=self.ui.capacidadSpin.value(),
				descripcion=self.ui.descripcionText.toPlainText(),
				estado=estad)
			QtGui.QMessageBox.information(self, "Guardado con exito", "Los datos se han guardado con exito!")
		else:
			QtGui.QMessageBox.information(self, "Advertencia", "El campo Nombre no puede ser vacio!")
	
	def clear(self):
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
