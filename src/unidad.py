# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui

from ui.unidad import Ui_unidadDialog
from models.unidad import Unidad
from models.tipo import Tipo

class UnidadDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_unidadDialog()
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

		tipoModel = Tipo(self.conn)
		tipoModel.loadAll()

		self.ui.tipoCombo.setModel(tipoModel.model)
		self.ui.tipoCombo.setModelColumn(1)

	def __init__(self, conn, id = -1, numero = 0, tipo = -1, capacidad = 0, 
	descripcion = "", estado = '',mainWin = None, parent = None):
		super(UnidadDialog, self).__init__(parent)

		self.id = id
		self.conn = conn
		self.model = Unidad(conn)
		self.modif = (id != -1)

		self.setup()

		self.ui.numeroLine.setText(str(numero))
		self.ui.tipoCombo.setCurrentIndex(0)
		self.ui.noDisponibleCheck.setChecked(estado == 'No Disponible')

		if tipo != -1:
			comboModel = self.ui.tipoCombo.model()
			found = False
			i = 0
			while not found and i<comboModel.rowCount():
				if comboModel.data(comboModel.index(i,0)).toInt()[0] == tipo:
					found = True
				else:
					i+=1
			self.ui.tipoCombo.setCurrentIndex(i)


		self.ui.capacidadSpin.setValue(capacidad)
		self.ui.descripcionText.setPlainText(descripcion)

		self.uiMain = mainWin #modif por Jona

		# VER COMBOBOX ESTADO!!!

#        self.numero = numero
#        self.tipo = tipo
#        self.capacidad = capacidad
#        self.descripcion = descripcion
#        self.estado = estado

	def save(self):
		if self.ui.numeroLine.text() != "":
			if self.ui.tipoCombo.count() > 0:
				if self.modif or self.model.checkname(nombre = self.ui.numeroLine.text()) == 0:
					comboModel = self.ui.tipoCombo.model()
					estad = "Libre"
					if self.ui.noDisponibleCheck.checkState() == QtCore.Qt.Checked:
						estad = "No Disponible"
					self.model.save(id=self.id,nombre=self.ui.numeroLine.text(),tipo=comboModel.data(comboModel.index(self.ui.tipoCombo.currentIndex(),0)).toInt()[0],
						capacidad=self.ui.capacidadSpin.value(),
						descripcion=self.ui.descripcionText.toPlainText(),
						estado=estad)
					self.uiMain.statusBar.showMessage("Los datos se han guardado con exito!",3000)
					return True
				else:
					QtGui.QMessageBox.information(self, "Advertencia","El numero de la Unidad ya existe!")
					return False
			else:
				#self.uiMain.statusBar.showMessage("Debe seleccionar una opción del campo Tipo!",3000)
				QtGui.QMessageBox.information(self, "Advertencia","Debe seleccionar una opción del campo Tipo!")
				return False
		else:
			QtGui.QMessageBox.information(self, "Advertencia","El campo Nombre no puede ser vacio!")
			return False
	
	def clear(self):
		self.ui.numeroLine.setText("")
		self.ui.tipoCombo.setCurrentIndex(0)
		self.ui.capacidadSpin.setValue(0)
		self.ui.descripcionText.setPlainText("")

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
		self.uiMain.title.setTitle("Administrar unidades")
		self.uiMain.widgets.setCurrentIndex(1)
		self.uiMain.widgets.widget(1).loadAll()
