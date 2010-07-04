#!/usr/bin/env python

from PyQt4 import QtCore,QtGui

from progress_ui import Ui_ProgressWidget
from path_ui import Ui_PathWidget
from oldroot_ui import Ui_OldRootWidget

class InstallPathPage(QtGui.QWizardPage):
	def __init__(self):
		super(InstallPathPage, self).__init__()
		self.setTitle(u"Ubicacion")
		self.setSubTitle(u"Por favor elija la ubicacion en donde se instalara "
			"Conotels.")
		
		self.ui = Ui_PathWidget()
		self.ui.setupUi(self)

		self.connect(self.ui.fileBut, QtCore.SIGNAL("clicked()"), self.fileBut_clicked)

		self.registerField("path", self.ui.pathLine)
	
	def fileBut_clicked(self):
		self.ui.pathLine.setText(QtGui.QFileDialog.getExistingDirectory(self, "Examinar", "C:\\Archivos de Programa\\"))
	
	def nextId(self):
		##################
		# Aca se corrobora si ya existe MySQL
		exists = False
		#################

		if exists:
			return 2
		else:
			return 4

class ProgressBarPage(QtGui.QWizardPage):
	def __init__(self):
		super(ProgressBarPage, self).__init__()
		self.setTitle(u"Instalando")
		self.setSubTitle(u"Esto puede tomar unos minutos...")
		
		self.ui = Ui_ProgressWidget()
		self.ui.setupUi(self)

		self.ui.progressBar.setValue(0)

	# val = [0, 100]
	def update(self, val):
		self.ui.progressBar.setValue(val)

class OldRootPage(QtGui.QWizardPage):
	def __init__(self, exists = False, error = False):
		super(OldRootPage, self).__init__()
		self.setTitle(u"MySQL")
		self.setSubTitle(u"Datos del motor MySQL de base de datos")
		
		self.ui = Ui_OldRootWidget()
		self.ui.setupUi(self)

		self.ui.errorLabel.setVisible(error)
		self.ui.existsLabel.setVisible(exists)
		self.ui.basicLabel.setVisible(not exists and not error)

		if exists and not error:
			self.registerField("pass1", self.ui.passLine)
		elif exists and error:
			self.registerField("pass2", self.ui.passLine)
		else:
			self.registerField("pass3", self.ui.passLine)
	
	def nextId(self):
		################
		# Aca se corrobora que le password
		# este bien
		error = True
		################
		if error:
			return 3
		else:
			return 5

def createIntroPage():
	page = QtGui.QWizardPage()
	page.setTitle("Bienvenido")

	label = QtGui.QLabel("Bienvenido al instalador de Conotels!")
	label.setWordWrap(True)

	layout = QtGui.QVBoxLayout()
	layout.addWidget(label)
	page.setLayout(layout)

	return page

def createProgressBarPage():
	page = ProgressBarPage()

	return page

def createInstallPathPage():
	page = InstallPathPage()

	return page

def createOldRootPage(exists, error):
	page = OldRootPage(exists, error)

	return page

def createConclusionPage():
    page = QtGui.QWizardPage()
    page.setTitle("Felicitaciones")

    label = QtGui.QLabel("El software se ha instalado de forma correcta.")
    label.setWordWrap(True)

    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page

def getPassword(p1, p2, p3):
	str1 = p1.field("pass1").toString()
	str2 = p2.field("pass2").toString()
	str3 = p3.field("pass3").toString()
	if str1.size() != 0:
		return str1
	if str2.size() != 0:
		return str2
	if str3.size() != 0:
		return str3

if __name__ == '__main__':

	import sys

	app = QtGui.QApplication(sys.argv)

	wizard = QtGui.QWizard()
	
	path = createInstallPathPage()

	passwordExists = createOldRootPage(True, False)
	passwordError = createOldRootPage(True, False)
	passwordBasic = createOldRootPage(False, False)

	progress = createProgressBarPage()

	wizard.setPage(0, createIntroPage())
	wizard.setPage(1, path)
	wizard.setPage(2, passwordExists)
	wizard.setPage(3, passwordError)
	wizard.setPage(4, passwordBasic)
	wizard.setPage(5, progress)
	wizard.setPage(6, createConclusionPage())

	wizard.setWindowTitle("Instalador de Conotels")
	wizard.show()

	ret = wizard.exec_()

	print path.field("path").toString()
	print getPassword(passwordExists, passwordError, passwordBasic)

	sys.exit(ret)
