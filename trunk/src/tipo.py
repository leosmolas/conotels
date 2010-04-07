from PyQt4 import QtCore, QtGui

from ui.tipo import Ui_tipoDialog
from models.tipo import Tipo

class TipoDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_tipoDialog()
		self.ui.setupUi(self)
		self.okBut = self.ui.buttonBox.addButton("Ok", QtGui.QDialogButtonBox.ActionRole)
		self.cancelBut = self.ui.buttonBox.addButton("Cancel", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.cancelBut, QtCore.SIGNAL("clicked()"),
				self.on_cancelBut_clicked)

		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		
	def __init__(self,nombre = "", costoTempAlta = 0, costoTempBaja = 0, mod = 0, parent = None):
		super(TipoDialog, self).__init__(parent)
		self.setup()

		self.model = Tipo()

		self.modif = (mod != 0)
		self.nombre = nombre
		self.costoTempAlta = costoTempAlta
		self.costoTempBaja = costoTempBaja

	def __del__(self):
		self.model.__del__()
		
	def clear(self):
		self.ui.nombreLine.setText("")
		self.ui.costoTempBajaSpin.setValue(0)
		self.ui.costoTempAltaSpin.setValue(0)

	def save(self):
		if self.modif:
			print "modify"
		else:
			print "new tipo"
			self.model.save(nombre=self.ui.nombreLine.text(),
				costoTemporadaAlta=self.ui.costoTempAltaSpin.value(),
				costoTemporadaBaja=self.ui.costoTempBajaSpin.value())
	
	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		self.save()
		self.clear()
		
		QtGui.QMessageBox.information(self, "Guardado con exito", 
			"Los datos se han guardado con exito!")

		if self.modif:
			self.close()
	
	@QtCore.pyqtSlot()
	def on_cancelBut_clicked(self):
		self.clear()
		if self.modif:
			self.close()
