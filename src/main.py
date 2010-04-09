from PyQt4 import QtCore, QtGui

from ui.mainwin import Ui_MainWindow

from unidad import UnidadDialog
from tipo import TipoDialog
from reserva import ReservaDialog
from huesped import HuespedDialog
from gastos import GastosDialog
from admin import Admin

import icons_rc

class MainWindow(QtGui.QMainWindow):
	def setup(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewUnitBut.setText("Administrar unidades")
		self.addNewUnitBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewUnitBut.setText("Administrar reservas")
		self.addNewUnitBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewUnitBut.setText("Administrar tipo")
		self.addNewUnitBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewUnitBut.setText("Administrar huesped")
		self.addNewUnitBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

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

		self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		self.addNewTypeBut.setText("Administrar gastos")
		self.addNewTypeBut.setIcon(QtGui.QIcon(":/add.png"))
		self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		QtCore.QObject.connect(self.ui.menuAdministracion, QtCore.SIGNAL("triggered(QAction *)"),
				self.changeToAction)

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setup()

		self.ui.options.currentItemChanged.connect(self.changeView)
		self.ui.options.setViewMode(QtGui.QListView.IconMode)
		self.ui.options.setCurrentRow(0)

	def changeToAction(self, action):
		w = self.ui.widgets.currentWidget()
		self.ui.widgets.removeWidget(w)
		w.__del__()
		if action.text() == "Nueva unidad":
			self.ui.title.setTitle(action.text())
			self.ui.widgets.insertWidget(1, UnidadDialog())
		elif action.text() == "Nuevo Tipo":
			self.ui.title.setTitle(action.text())
			self.ui.widgets.insertWidget(1, TipoDialog())
		self.ui.widgets.setCurrentIndex(1)

	def changeView(self, current, previous):
		if not current:
			current = previous

		selected = self.ui.options.row(current)

		try:
			w = self.ui.widgets.currentWidget()
			self.ui.widgets.removeWidget(w)
			w.__del__()
		except:
			pass

		if selected == 0:
			self.ui.title.setTitle("Administrar unidades")
			self.ui.widgets.insertWidget(1, Admin("Unidad"))
		elif selected == 1:
			self.ui.title.setTitle("Administrar reservas")
			self.ui.widgets.insertWidget(1, Admin("Reserva"))
		elif selected == 2:
			self.ui.title.setTitle("Administrar tipos")
			self.ui.widgets.insertWidget(1, Admin("Tipo"))
		elif selected == 3:
			self.ui.title.setTitle("Administrar huesped")
			self.ui.widgets.insertWidget(1, Admin("Huesped"))
		elif selected == 4:
			self.ui.title.setTitle("Reserva")
			self.ui.widgets.insertWidget(1, ReservaDialog())
		elif selected == 5:
			self.ui.title.setTitle("Huesped")
			self.ui.widgets.insertWidget(1, HuespedDialog())
		elif selected == 6:
			self.ui.title.setTitle("Gastos")
			self.ui.widgets.insertWidget(1, GastosDialog())

		self.ui.widgets.setCurrentIndex(1)

import sys

app = QtGui.QApplication(sys.argv)
#app.setStyle(QtGui.QWindowsVistaStyle())
main = MainWindow()
main.show()
sys.exit(app.exec_())
