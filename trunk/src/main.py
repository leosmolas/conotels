# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from ui.mainwin import Ui_MainWindow

from unidad import UnidadDialog
from tipo import TipoDialog
from reserva import ReservaDialog
from huesped import HuespedDialog
from gastos import GastosDialog
from admin import Admin
from grilla import GrillaDialog

from connection.connection import Connection

import icons_rc

class MainWindow(QtGui.QMainWindow):
	def setup(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.statusBar = QtGui.QStatusBar(self)
		self.setStatusBar(self.statusBar)
		#self.statusBar.showMessage("prueba",3000)
		self.ui.statusBar = self.statusBar;
		
		self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewUnitBut.setText("Administrar unidades")
		self.addNewUnitBut.setIcon(QtGui.QIcon(":/property.png"))
		self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewUnitBut.setText("Administrar reservas")
		self.addNewUnitBut.setIcon(QtGui.QIcon(":/diaryplain.png"))
		self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewUnitBut.setText("Administrar tipo")
		self.addNewUnitBut.setIcon(QtGui.QIcon(":/tools.png"))
		self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewUnitBut.setText("Administrar huesped")
		self.addNewUnitBut.setIcon(QtGui.QIcon(":/people.png"))
		self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		'''self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewTypeBut.setText("Nueva reserva")
		self.addNewTypeBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewTypeBut.setText("Nuevo huesped")
		self.addNewTypeBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)'''

		self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewTypeBut.setText("Administrar gastos")
		self.addNewTypeBut.setIcon(QtGui.QIcon(":/purse.png"))
		self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewTypeBut.setText("Grilla")
		self.addNewTypeBut.setIcon(QtGui.QIcon(":/purse.png"))
		self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		QtCore.QObject.connect(self.ui.menuAdministracion, QtCore.SIGNAL("triggered(QAction *)"),
				self.changeToAction)

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)

		self.conn = Connection(dbName="conotels", dbUser="root", dbPass="")
		self.conn.open()

		self.setup()

		self.ui.options.currentItemChanged.connect(self.changeView)
		self.ui.options.setViewMode(QtGui.QListView.IconMode)
		self.ui.options.setCurrentRow(0)

	def changeToAction(self, action):
		self.ui.widgets.removeWidget(self.ui.widgets.currentWidget())
		if action.text() == "Nueva unidad":
			self.ui.title.setTitle(action.text())
			self.ui.widgets.insertWidget(1, UnidadDialog(self.conn))
		elif action.text() == "Nuevo Tipo":
			self.ui.title.setTitle(action.text())
			self.ui.widgets.insertWidget(1, TipoDialog(self.conn))
		self.ui.widgets.setCurrentIndex(1)

	def __del__(self):
		self.conn.close()

	def changeView(self, current, previous):
		if not current:
			current = previous

		selected = self.ui.options.row(current)

		self.ui.widgets.removeWidget(self.ui.widgets.currentWidget())
		if selected == 0:
			self.ui.title.setTitle("Administrar unidades")
			self.ui.widgets.insertWidget(1, Admin(self.conn, "Unidad",self.ui))
		elif selected == 1:
			self.ui.title.setTitle("Administrar reservas")
			self.ui.widgets.insertWidget(1, Admin(self.conn, "Reserva",self.ui))
		elif selected == 2:
			self.ui.title.setTitle("Administrar tipos")
			self.ui.widgets.insertWidget(1, Admin(self.conn, "Tipo",self.ui))
		elif selected == 3:
			self.ui.title.setTitle("Administrar huespedes")
			self.ui.widgets.insertWidget(1, Admin(self.conn, "Huesped",self.ui))
		elif selected == 4:
			self.ui.title.setTitle("Gastos")
			self.ui.widgets.insertWidget(1, GastosDialog(self.conn))
		elif selected == 5:
			self.ui.title.setTitle("Grilla")
			self.ui.widgets.insertWidget(1, GrillaDialog(self.conn))
		self.ui.widgets.setCurrentIndex(1)

import sys

app = QtGui.QApplication(sys.argv)
#app.setStyle(QtGui.QWindowsVistaStyle())
app.setStyle("windowsvista")
main = MainWindow()
main.show()
sys.exit(app.exec_())
