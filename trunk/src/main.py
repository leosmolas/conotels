from PyQt4 import QtCore, QtGui

from ui.mainwin import Ui_MainWindow
# from db.unidad import SARASA

from unidad import UnidadDialog
from tipo import TipoDialog
from reserva import ReservaDialog
from huesped import HuespedDialog

import icons_rc

class MainWindow(QtGui.QMainWindow):
	def setup(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewUnitBut.setText("Agregar nueva unidad")
		self.addNewUnitBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewTypeBut.setText("Agregar nuevo tipo")
		self.addNewTypeBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewTypeBut.setText("Nueva reserva")
		self.addNewTypeBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewTypeBut.setText("Nuevo huesped")
		self.addNewTypeBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setup()

		self.ui.options.currentItemChanged.connect(self.changeView)
		self.ui.options.setViewMode(QtGui.QListView.IconMode)

	def changeView(self, current, previous):
		if not current:
			current = previous

		selected = self.ui.options.row(current)
		self.ui.widgets.removeWidget(self.ui.widgets.currentWidget())

		if selected == 0:
			self.ui.title.setTitle("Unidad")
			self.ui.widgets.insertWidget(1, UnidadDialog())
		elif selected == 1:
			self.ui.title.setTitle("Tipo")
			self.ui.widgets.insertWidget(1, TipoDialog())
		elif selected == 2:
			self.ui.title.setTitle("Reserva")
			self.ui.widgets.insertWidget(1, ReservaDialog())
		elif selected == 3:
			self.ui.title.setTitle("Huesped")
			self.ui.widgets.insertWidget(1, HuespedDialog())

		self.ui.widgets.setCurrentIndex(1)

import sys

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
