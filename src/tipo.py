from PyQt4 import QtCore, QtGui

from ui.tipo import Ui_tipoDialog
from models.tipo import Tipo

class TipoDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_tipoDialog()
		self.ui.setupUi(self)
		
		self.okBut = self.ui.buttonBox.addButton("&Guardar", QtGui.QDialogButtonBox.ActionRole)
		self.cancelBut = self.ui.buttonBox.addButton("&Cancelar", QtGui.QDialogButtonBox.ActionRole)

		self.okBut.setIcon(QtGui.QIcon(":/save.png"))
		self.cancelBut.setIcon(QtGui.QIcon(":/cancel.png"))

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.cancelBut, QtCore.SIGNAL("clicked()"),
				self.on_cancelBut_clicked)

		if not self.modif:
			self.backBut = self.ui.buttonBox.addButton("&Volver", QtGui.QDialogButtonBox.ActionRole)
			self.backBut.setIcon(QtGui.QIcon(":/back.png"))
			QtCore.QObject.connect(self.backBut, QtCore.SIGNAL("clicked()"),
					self.on_backBut_clicked)

		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		
	def __init__(self, conn, id = -1, nombre = "", costoTempAlta = 0, costoTempBaja = 0, mod = 0, mainWin = None,parent = None):
		super(TipoDialog, self).__init__(parent)

		self.conn = conn

		self.id = id
		self.model = Tipo(conn)

		self.modif = (id != -1)

		self.setup()

#        self.nombre = nombre
#        self.costoTempAlta = costoTempAlta
#        self.costoTempBaja = costoTempBaja
		
		if self.modif:
			self.ui.nombreLine.setText(nombre)
			self.ui.costoTempBajaSpin.setValue(costoTempBaja)
			self.ui.costoTempAltaSpin.setValue(costoTempAlta)
			self.ui.descEdit.setPlainText("")
		
		self.uiMain = mainWin #modif por Jona
		
	def clear(self):
		self.ui.nombreLine.setText("")
		self.ui.costoTempBajaSpin.setValue(0)
		self.ui.costoTempAltaSpin.setValue(0)
		self.ui.descEdit.setPlainText("")

	def save(self):
		if self.ui.nombreLine.text() != "":
			self.model.save(id=self.id,nombre=self.ui.nombreLine.text(),
				costoTemporadaAlta=self.ui.costoTempAltaSpin.value(),
				costoTemporadaBaja=self.ui.costoTempBajaSpin.value(),
				descripcion=self.ui.descEdit.toPlainText())
			self.uiMain.statusBar.showMessage("Los datos se han guardado con exito!",3000)
			return True
		else:
			#self.uiMain.statusBar.showMessage("El campo Nombre no puede ser vacio!",3000)
			QtGui.QMessageBox.information(self, "Advertencia","El campo Nombre no puede ser vacio!")
			return False
	
	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		save = self.save()
		if save == True:
			self.clear()		
			if self.modif:
				self.close()
	
	@QtCore.pyqtSlot()
	def on_cancelBut_clicked(self):
		self.clear()
		if self.modif:
			self.close()

	def on_backBut_clicked(self):
		self.uiMain.widgets.removeWidget(self.uiMain.widgets.widget(2))
		self.uiMain.title.setTitle("Administrar tipos")
		self.uiMain.widgets.setCurrentIndex(1)
		self.uiMain.widgets.widget(1).loadAll()
