# -*- coding: utf-8 -*-
#!/usr/bin/env python

from PyQt4 import QtCore,QtGui

from progress_ui import Ui_ProgressWidget
from path_ui import Ui_PathWidget
from oldroot_ui import Ui_OldRootWidget
from threading import Thread
import check
import os
import sys
import time
import getopt
import subprocess
import stat
import shutil
import check
import exceptions
import inst
import icons_rc

tmpPathConfFile = open("installerConf.dat", "r")
defaultPath=os.path.expandvars('%HOMEDRIVE%')

tmpPath=os.path.expandvars(tmpPathConfFile.readline().split("=")[-1].split(";")[0])

class WaitThread(Thread):
	def __init__ (self,progress):
		Thread.__init__(self)
		self.progress=progress

	@QtCore.pyqtSlot()
	def update(self,value,str):
		self.progress.updateProgress(value,str)
		
	def run(self):
		self.installer=inst.Inst()
		QtCore.QObject.connect(self.installer,QtCore.SIGNAL("installSignal(int,str)"),self.update)
		self.installer.install()
	
		

	
 
class InstallPathPage(QtGui.QWizardPage):
	def __init__(self, parent,oldPath):
		super(InstallPathPage, self).__init__(parent)
		self.setTitle(u"Ubicacion")
		self.setButtonText(QtGui.QWizard.NextButton,"Siguiente")
		self.setButtonText(QtGui.QWizard.BackButton,'Atras')
		self.setButtonText(QtGui.QWizard.CancelButton,"Cancelar")
		self.setSubTitle(u"Por favor elija la ubicacion en donde se instalara "
			"Conotels.")
		
		self.ui = Ui_PathWidget()
			
		self.ui.setupUi(self)
		self.oldPath=oldPath
		self.connect(self.ui.fileBut, QtCore.SIGNAL("clicked()"), self.fileBut_clicked)

		self.registerField("path", self.ui.pathLine)

	
	def fileBut_clicked(self):
		self.appPath=os.path.normcase(str(QtGui.QFileDialog.getExistingDirectory(self, "Examinar", defaultPath+"\Program Files")+"\Conosoft"))
		
		self.ui.pathLine.setText(self.appPath+'\\Conotels')
	
		os.system('mkdir "'+str(self.ui.pathLine.text())+'"')
		if(self.appPath!=self.oldPath):
			
			os.system('RD "'+self.oldPath+'" /Q /S')
			self.oldPath=self.appPath
			
		self.emit(QtCore.SIGNAL("completeChanged()"))
	
	def isComplete(self):
		return QtCore.QDir().exists(self.ui.pathLine.text())
		

class ProgressBarPage(QtGui.QWizardPage):
	def __init__(self):
		super(ProgressBarPage, self).__init__()
		self.succes=False
		self.finish=0
		self.current = WaitThread(self)
		self.setTitle(u"Instalando")
		self.setSubTitle(u"Esto puede tomar unos minutos...")
		self.setCommitPage(True)
		self.setButtonText(QtGui.QWizard.CommitButton,"Siguiente")
		self.setButtonText(QtGui.QWizard.BackButton,"Atras")
		self.setButtonText(QtGui.QWizard.CancelButton,"Cancelar")
		self.ui = Ui_ProgressWidget()
		self.ui.setupUi(self)
		
	# val = [0, 100]
	def updateProgress(self,value,str):
		self.ui.progressBar.setValue(value)
		if(value==100):
			self.setSubTitle(u"Instalación Finalizada. Puede Continuar.")
			self.finish=1
		self.ui.label.setText(str)
	
			
	def validatePage(self):
		ret = False
		if(self.finish==1):
				ret=True
		return ret
		
	
	
	def initializePage(self):
		
		self.current.start() 
		

class OldRootPage(QtGui.QWizardPage):
	def __init__(self, parent):
		super(OldRootPage, self).__init__(parent)
		self.wiz = parent
		self.setTitle(u"MySQL")
		self.setSubTitle(u"Datos del motor MySQL de base de datos")
		self.setButtonText(QtGui.QWizard.CommitButton,"Siguiente")
		self.setButtonText(QtGui.QWizard.BackButton,unicode("Atras"))
		self.setButtonText(QtGui.QWizard.CancelButton,"Cancelar")
		
		self.setCommitPage(True)
		self.ui = Ui_OldRootWidget()
		self.ui.setupUi(self)

		self.exists = self.existsMysql()
	
		self.ui.errorLabel.setVisible(False)
		self.ui.existsLabel.setVisible(self.exists)
		self.ui.basicLabel.setVisible(not self.exists)

		self.registerField("oldpass", self.ui.passLine)
		self.registerField("pass", self.ui.passLine)
	
	def validatePage(self):

		ret = True
		# si existe otro mysql:
		if self.exists:
			ret = False
			##############################
			# aca se corrobora si el password esta bien
			correct = (check.checkRoot(str(self.ui.passLine.text()))==1)
		
			##############################
			if correct:
				ret = True
			else:
				self.ui.errorLabel.setVisible(True)
				self.ui.passLine.setText("")
				self.ui.passLine.setFocus()
				ret = False

		if ret:
			self.wiz.genConf()

	
		return ret
	
	

	def existsMysql(self):
		if(check.isBDServiceInstalled()==1):
			return True
		else:
			return False

class Wizard(QtGui.QWizard):


	def __init__(self):
		
		super(Wizard, self).__init__()
		self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/icon.ico")))
		os.system('mkdir "' + defaultPath+"\Program Files"+"\Conosoft\Conotels"+'"')
		''' oldPath se usa para evitar que se borren los directorios cada vez que se cambia de path'''
		self.oldPath=os.path.normcase(defaultPath+'\\Program Files\Conosoft')
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
		page.setButtonText(QtGui.QWizard.NextButton,"Siguiente")
		page.setButtonText(QtGui.QWizard.BackButton,unicode("Atras"))
		page.setButtonText(QtGui.QWizard.CancelButton,"Cancelar")

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
		page = InstallPathPage(self,self.oldPath)

		return page

	def createOldRootPage(self):
		page = OldRootPage(self)

		return page

	def createConclusionPage(self):
		page = QtGui.QWizardPage()
		page.setTitle("Felicitaciones")
		page.setButtonText(QtGui.QWizard.CancelButton,"Cancelar")
		page.setButtonText(QtGui.QWizard.FinishButton,"Finalizar")
		page.setButtonText(QtGui.QWizard.BackButton,"Atras")
		
		page.setFinalPage(True) 
		label = QtGui.QLabel("El software se ha instalado de forma correcta.")
		label.setWordWrap(True)

		layout = QtGui.QVBoxLayout()
		layout.addWidget(label)
		page.setLayout(layout)

		return page

	def genConf(self):
		
		data = "dirMysql="+defaultPath+"\\Program Files\\MySQL\\;\n"
		data += "dirApp="+self.path.field("path").toString()+"\\"+";\n"

		if self.password.exists:
			oldpass = self.password.field("oldpass").toString()
			passw = self.password.field("oldpass").toString()
		else:
			oldpass = ""
			passw = self.password.field("pass").toString()
		data += "oldRootPass="+oldpass+";\n"
		data += "newRootPass="+passw+";\n"
		data += "defaultDatabase=mysql;\n"
		data += "applicationDatabase=conotels;\n"
		data += "inputInstallScript=bd\conotels.sql;\n"
		data += "inputUninstallScript=bd\drop.sql;\n"
		data += "userRoot=root;"
		f = open(tmpPath+'\\conf.dat', "w")
		f.write(data)
		f.close()

if __name__ == '__main__':

	import sys
	app = QtGui.QApplication(sys.argv)
	wizard = Wizard()
	ret = wizard.exec_()
	sys.exit(ret)
