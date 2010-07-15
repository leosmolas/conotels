from PyQt4 import QtCore, QtGui

import re

from ui.tipo import Ui_tipoDialog
from models.tipo import Tipo

class TipoDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_tipoDialog()
		self.ui.setupUi(self)
		
		self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/house.png")))
		
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
		
	def __init__(self, conn, id = -1, nombre = "", costoTempAlta = 0.00, costoTempBaja = 0.00, desc = "", mainWin = None,parent = None):
		super(TipoDialog, self).__init__(parent)

		self.conn = conn

		self.id = id
		self.model = Tipo(conn)
		self.nombre = nombre
		self.modif = (id != -1)

		self.setup()

		#        self.nombre = nombre
		#        self.costoTempAlta = costoTempAlta
		#        self.costoTempBaja = costoTempBaja
		
		if self.modif:
			self.setWindowTitle(QtGui.QApplication.translate("tipoDialog", u"Editar Tipo de Unidad", None, QtGui.QApplication.UnicodeUTF8))
			self.ui.nombreLine.setText(nombre)
			self.ui.costoTempBajaSpin.setValue(costoTempBaja)
			self.ui.costoTempAltaSpin.setValue(costoTempAlta)
			self.ui.descEdit.setPlainText(desc)
		
		self.uiMain = mainWin #modif por Jona
		
	def clear(self):
		self.ui.nombreLine.setText("")
		self.ui.costoTempBajaSpin.setValue(0)
		self.ui.costoTempAltaSpin.setValue(0)
		self.ui.descEdit.setPlainText("")

	def save(self):
		if self.ui.nombreLine.text() != "":
			if (self.modif and self.ui.nombreLine.text() == self.nombre) or self.model.checkname(nombre = self.ui.nombreLine.text()) == 0:
				self.model.save(id=self.id,nombre=self.escape(unicode(self.ui.nombreLine.text())),
					costoTemporadaAlta=self.ui.costoTempAltaSpin.value(),
					costoTemporadaBaja=self.ui.costoTempBajaSpin.value(),
					descripcion=self.escape(unicode(self.ui.descEdit.toPlainText())))
				self.uiMain.statusBar.showMessage("Los datos se han guardado con exito!",3000)
				return True
			else:
				QtGui.QMessageBox.information(self, "Error", "El nombre ya existe!")
				return False
		else:
			#self.uiMain.statusBar.showMessage("El campo Nombre no puede ser vacio!",3000)
			QtGui.QMessageBox.information(self, "Error", u"El campo Nombre no puede ser vacio!")
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
		#self.clear()
		#if self.modif:
		#	self.close()
		self.clear()
		if self.modif:
			self.close()
		else:
			self.uiMain.widgets.removeWidget(self.uiMain.widgets.widget(2))
			self.uiMain.title.setTitle("Administrar tipos")
			self.uiMain.widgets.setCurrentIndex(1)
			self.uiMain.widgets.widget(1).loadAll()

	def on_backBut_clicked(self):
		self.clear()
		if self.modif:
			self.close()
		else:
			self.uiMain.widgets.removeWidget(self.uiMain.widgets.widget(2))
			self.uiMain.title.setTitle("Administrar tipos")
			self.uiMain.widgets.setCurrentIndex(1)
			self.uiMain.widgets.widget(1).loadAll()

	@QtCore.pyqtSlot()
	def keyPressEvent(self, event):
		keyEvent = QtGui.QKeyEvent(event)
		if(event.type()==QtCore.QEvent.KeyPress) and ((keyEvent.key() == QtCore.Qt.Key_Return) or (keyEvent.key() == QtCore.Qt.Key_Enter)):
			self.focusNextChild()
			return
		elif keyEvent.key() == QtCore.Qt.Key_Escape:
			print "ESC!!!!"
			keyEvent.accept()
			return
		return super(TipoDialog, self).keyPressEvent(keyEvent)

	def escape(self, str):
		ns = str
		return ns.replace('"', '\\"').replace("'", "\\'")
