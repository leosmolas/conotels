#!/usr/bin/env python

from PyQt4 import QtCore,QtGui

from progress_ui import Ui_ProgressWidget
from path_ui import Ui_PathWidget
from oldroot_ui import Ui_OldRootWidget

class InstallPathPage(QtGui.QWizardPage):
	def __init__(self, parent):
		super(InstallPathPage, self).__init__(parent)
		self.setTitle(u"Ubicacion")
		self.setSubTitle(u"Por favor elija la ubicacion en donde se instalara "
			"Conotels.")
		
		self.ui = Ui_PathWidget()
		self.ui.setupUi(self)

		self.connect(self.ui.fileBut, QtCore.SIGNAL("clicked()"), self.fileBut_clicked)

		self.registerField("path", self.ui.pathLine)
	
	def fileBut_clicked(self):
		self.ui.pathLine.setText(QtGui.QFileDialog.getExistingDirectory(self, "Examinar", "C:\\Archivos de Programa\\"))
		self.emit(QtCore.SIGNAL("completeChanged()"))
	
	def isComplete(self):
		return QtCore.QDir().exists(self.ui.pathLine.text())

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
	def __init__(self, parent):
		super(OldRootPage, self).__init__(parent)
		self.wiz = parent
		self.setTitle(u"MySQL")
		self.setSubTitle(u"Datos del motor MySQL de base de datos")
		
		self.ui = Ui_OldRootWidget()
		self.ui.setupUi(self)

		self.exists = self.existsMysql()
	
		self.ui.errorLabel.setVisible(False)
		self.ui.existsLabel.setVisible(self.exists)
		self.ui.basicLabel.setVisible(not self.exists)

		self.registerField("oldpass", self.ui.passLine)
		self.registerField("pass", self.ui.passLine)
	
	def validatePage(self):
		ret = False
		# si existe otro mysql:
		if self.exists:
			##############################
			# aca se corrobora si el password esta bien
			correct = (self.ui.passLine.text() == "hola!!")
			##############################
			if correct:
				ret = True
			else:
				self.ui.errorLabel.setVisible(True)
				self.ui.passLine.setText("")
				ret = False

		if ret:
			self.wiz.genConf()
		return ret
	
	def existsMysql(self):
		############################
		# aca se corrobora si existe una instalacion de mysql
		############################
		return True

class Wizard(QtGui.QWizard):
	def __init__(self):
		super(Wizard, self).__init__()

		self.path = self.createInstallPathPage()
		self.password= self.createOldRootPage()
		self.progress = self.createProgressBarPage()

		self.addPage(self.createIntroPage())
		self.addPage(self.path)
		self.addPage(self.password)
		self.addPage(self.progress)
		self.addPage(self.createConclusionPage())

		self.setWindowTitle("Instalador de Conotels")
		self.show()

	def createIntroPage(self):
		page = QtGui.QWizardPage()
		page.setTitle("Bienvenido")

		label = QtGui.QLabel("Bienvenido al instalador de Conotels!")
		label.setWordWrap(True)

		layout = QtGui.QVBoxLayout()
		layout.addWidget(label)
		page.setLayout(layout)

		return page

	def createProgressBarPage(self):
		page = ProgressBarPage()

		return page

	def createInstallPathPage(self):
		page = InstallPathPage(self)

		return page

	def createOldRootPage(self):
		page = OldRootPage(self)

		return page

	def createConclusionPage(self):
		page = QtGui.QWizardPage()
		page.setTitle("Felicitaciones")

		label = QtGui.QLabel("El software se ha instalado de forma correcta.")
		label.setWordWrap(True)

		layout = QtGui.QVBoxLayout()
		layout.addWidget(label)
		page.setLayout(layout)

		return page

	def genConf(self):
		data = "dirMysql=C:\\Archivos de programa\\MySQL\\;\n"
		data += "dirApp="+self.path.field("path").toString()+";\n"

		if self.password.exists:
			oldpass = self.password.field("oldpass").toString()
			passw = ""
		else:
			oldpass = ""
			passw = self.passwordBasic.field("pass").toString()
		data += "oldRootPass="+oldpass+";\n"
		data += "newRootPass="+passw+";\n"
		data += "defaultDatabase=mysql;\n"
		data += "applicationDatabase=conotels;\n"
		data += "inputScript=conotels.sql;\n"
		data += "userRoot=root;"
		f = open("conf.dat", "w")
		f.write(data)
		f.close()

if __name__ == '__main__':

	import sys

	app = QtGui.QApplication(sys.argv)
	wizard = Wizard()
	ret = wizard.exec_()
	sys.exit(ret)
