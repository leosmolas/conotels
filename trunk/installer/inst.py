# -*- coding: utf-8 -*-
import os
import sys
import getopt
import subprocess
import stat
import shutil
import check
import commands
from PyQt4.QtCore import *
from PyQt4 import QtCore
from connection import Connection
import color_console as cons
import copy



class Inst(QtCore.QObject):
	def __init__(self):
		QtCore.QObject.__init__(self)
		'''self.connect(self,QtCore.SIGNAL("testSignal()"),self.update)'''
		self.confInstaller()
		
		 

		
	def confInstaller(self):
		'''global tmpPathConfFile,tmpPath,inputConfFileName,outputInstallerFile,inputData,default_colors,default_bg'''
		self.tmpPathConfFile = open("installerConf.dat", "r")
		self.tmpPath=os.path.expandvars(self.tmpPathConfFile.readline().split("=")[-1].split(";")[0])
		self.inputConfFileName=os.path.normcase(self.tmpPath+'\\conf.dat')
		self.inputData = {"inputInstallScript":None,"inputUninstallScript":None,"dirApp":None,"dirMysql":None,"newRootPass":None,"defaultDatabase":None,"applicationDatabase":None,"userRoot":None,"oldRootPass":None}
		self.default_colors = cons.get_text_attr()
		self.default_bg = self.default_colors & 0x0070
		self.readConf()
	

	def setInstColor(self):
		cons.set_text_attr(cons.FOREGROUND_GREEN | self.default_bg |
						cons.FOREGROUND_INTENSITY)
	
	def mysqlDirectoryExists(self):
		res=0
		if(os.path.isdir(self.inputData["dirMysql"])):
			res=1
		return res
	
	def printHeader(self,str):
		cons.set_text_attr(cons.FOREGROUND_RED | self.default_bg |
						cons.FOREGROUND_INTENSITY)
		print str
		cons.set_text_attr(self.default_colors)
	
	def printWarning(self,str):
		cons.set_text_attr(cons.FOREGROUND_YELLOW  | self.default_bg |
						cons.FOREGROUND_INTENSITY)
		print str
		cons.set_text_attr(self.default_colors)
	
	
	def installMysql(self):
		self.printHeader("Instalando MySQL...")
		self.setInstColor()
		if(self.mysqlDirectoryExists()==1):
				self.printWarning('Atencion: se borraran los archivos de este directorio.')
				self.removeMysql()
		os.system('mkdir "'+ self.inputData["dirMysql"]+'"')
		os.system('xcopy "mysql\*.*" "'+ self.inputData["dirMysql"]+'" /e')
		cons.set_text_attr(self.default_colors)


	def installApp(self):
		self.printHeader("Instalando Aplicacion...")
					 
		if(self.appDirectoryExists()==1):
				self.printWarning("EL directorio no esta vacio. Se borrara el contenido.")
				self.removeApp()
		self.setInstColor()
		os.system('mkdir "' + self.inputData["dirApp"]+'"')
		os.system('xcopy "app\*.*" "'+ self.inputData["dirApp"]+'" /e')
		cons.set_text_attr(self.default_colors)
	

	
	def appDirectoryExists(self):
		res=0
		if(os.path.isdir(self.inputData["dirApp"])):
			res=1
		return res
	
	def installService(self):
		self.printHeader("Instalando Servicio MySQL...")
		self.setInstColor()
		os.system('"'+self.inputData["dirMysql"]+'\\bin\\mysqld" --install')
		cons.set_text_attr(self.default_colors)

	
	def runService(self):
		self.printHeader("Iniciando Servicio MySQL...")
		self.setInstColor()
		os.system('NET START MySql')
		cons.set_text_attr(self.default_colors)


	def stopService(self):
		self.printHeader("Deteniendo Servicio MySQL...")
		self.setInstColor()
		os.system('NET STOP MySQL')
		cons.set_text_attr(self.default_colors)
			
	
	def removeMysql(self):
		self.printHeader("Eliminando archivos de MySQL...")
		shutil.rmtree(self.inputData["dirMysql"])
		cons.set_text_attr(self.default_colors)

	

	def removeApp(self):
		self.printHeader("Desinstalando Aplicacion...")
		shutil.rmtree(self.inputData["dirApp"])
		cons.set_text_attr(self.default_colors)

	
	def removeMysqlService(self):
		self.printHeader("Desinstalando Servicio MySQL...")
		os.system('"'+check.findMysqlPath() +'\\mysqld" --remove')
		cons.set_text_attr(self.default_colors)

	
	def removeAppDB(self):
		self.printHeader("Eliminando Base de Datos...")
		self.setInstColor()
		os.system('"'+check.findMysqlPath()+'\\mysql.exe" -u '+self.inputData["userRoot"]+' --password='+self.inputData["newRootPass"]+' '+self.inputData["applicationDatabase"]+ '< '+self.inputData["inputUninstallScript"])
		os.system('NET STOP MySql')
		os.system('NET START MySql')
		cons.set_text_attr(default_colors)

	
	def createShortCut(self):
		self.printHeader("Creando acceso directo en el Escritorio...")
		self.setInstColor()
		if(os.path.isdir(os.path.expandvars("%USERPROFILE%")+"\\Escritorio")):
			print 'SHORTCUT /f:"'+os.path.expandvars("%USERPROFILE%")+'\\Escritorio\Conotels.lnk" /a:c /t:"'+self.inputData["dirApp"]+'\main.exe" /W:"'+self.inputData["dirApp"]+'\\" /I:"'+self.inputData["dirApp"]+'\\icon.ico"'
			os.system('SHORTCUT /f:"'+os.path.expandvars("%USERPROFILE%")+'\\Escritorio\Conotels.lnk" /a:c /t:"'+self.inputData["dirApp"]+'\main.exe" /W:"'+self.inputData["dirApp"]+'\\" /I:"'+self.inputData["dirApp"]+'\\icon.ico"' )
		else:
			os.system('SHORTCUT /f:"'+os.path.expandvars("%USERPROFILE%")+'\\Desktop\Conotels.lnk" /a:c /t:"'+self.inputData["dirApp"]+'\main.exe" /W:"'+self.inputData["dirApp"]+'\\" /I:"'+self.inputData["dirApp"]+'\\icon.ico"'  )
		cons.set_text_attr(self.default_colors)
	
	def confRoot(self):
		self.printHeader("Configurando usuario root...")
		self.setInstColor()
		conn=Connection(dbName=self.inputData["defaultDatabase"], dbUser=self.inputData["userRoot"], dbPass=self.inputData["oldRootPass"])
		conn.open()
		conn.update("UPDATE "+self.inputData["defaultDatabase"]+".user SET Password=PASSWORD("+self.mysqlString(self.inputData["newRootPass"])+") WHERE User='"+self.inputData["userRoot"]+"';")
		conn.close()
		os.system('NET STOP MySql')
		os.system('NET START MySql')
		cons.set_text_attr(self.default_colors)

			
	def confDB(self):
		self.printHeader("Configurando base de datos de la aplicacion...")
		self.setInstColor()
		'''
		conn=Connection(dbName=inputData["defaultDatabase"], dbUser=inputData["userRoot"], dbPass=inputData["newRootPass"])
		'''
		print '"'+check.findMysqlPath()+'\\mysql.exe" -u '+self.inputData["userRoot"]+' --password='+self.inputData["newRootPass"]+' '+self.inputData["defaultDatabase"]+ '< '+self.inputData["inputInstallScript"]
		os.system('"'+check.findMysqlPath()+'\\mysql.exe" -u '+self.inputData["userRoot"]+' --password='+self.inputData["newRootPass"]+' '+self.inputData["defaultDatabase"]+ '< '+self.inputData["inputInstallScript"])
		os.system('NET STOP MySql')
		os.system('NET START MySql')
		cons.set_text_attr(self.default_colors)
	


	
	def readConf(self):

		self.inputConfFile = open(self.inputConfFileName,"r")

		for line in self.inputConfFile.readlines():
			if(line.find("dirMysql")==0):
				self.inputData["dirMysql"]=line.split("=")[-1].split(";")[0]	
			if(line.find("newRootPass")==0):
				self.inputData["newRootPass"]=line.split("=")[-1].split(";")[0]	
			if(line.find("defaultDatabase")==0):
				self.inputData["defaultDatabase"]=line.split("=")[-1].split(";")[0]
			if(line.find("applicationDatabase")==0):
				self.inputData["applicationDatabase"]=line.split("=")[-1].split(";")[0]
			if(line.find("userRoot")==0):
				self.inputData["userRoot"]=line.split("=")[-1].split(";")[0]	
			if(line.find("oldRootPass")==0):
				self.inputData["oldRootPass"]=line.split("=")[-1].split(";")[0]	
			if(line.find("inputUninstallScript")==0):
				self.inputData["inputUninstallScript"]=line.split("=")[-1].split(";")[0]	
			if(line.find("dirApp")==0):
				self.inputData["dirApp"]=line.split("=")[-1].split(";")[0]	
			if(line.find("inputInstallScript")==0):
				self.inputData["inputInstallScript"]=line.split("=")[-1].split(";")[0]	
			
			
		'''for key in self.inputData.keys():
			if(self.inputData[key]==None):
				print "Parametros de archivo de configuracion incorrectos"
				sys.exit()'''


	def mysqlString(self,str):
		return "'"+str+"'"
			
	@QtCore.pyqtSlot()
	def update(self):
		print "Llego la senal"
		
	

	def install(self):
		
	
		if(not check.isBDServiceInstalled()):
			self.emit(QtCore.SIGNAL("installSignal(int,str)"),10,str("Instalando MySQL..."))
			self.installMysql()
			self.emit(QtCore.SIGNAL("installSignal(int,str)"),14,str("Instalando Servicio MySQL..."))
			self.installService()
			self.emit(QtCore.SIGNAL("installSignal(int,str)"),28,str("Iniciando Servicio MySQL..."))
			self.runService()
			self.emit(QtCore.SIGNAL("installSignal(int,str)"),42,str("Configurando usuario root..."))
			self.confRoot()
			

		else:
			if(not check.isBDServiceRunning()):
				self.emit(QtCore.SIGNAL("installSignal(int,str)"),56,str("Iniciando Servicio MySQL..."))
				self.runService()
				

		self.emit(QtCore.SIGNAL("installSignal(int,str)"),60,str("Instalando Aplicacion..."))
		self.installApp()
		self.emit(QtCore.SIGNAL("installSignal(int,str)"),70,str("Creando acceso directo en el Escritorio..."))
		self.createShortCut()
		self.emit(QtCore.SIGNAL("installSignal(int,str)"),80,str("Configurando base de datos de la Aplicacion..."))
		self.confDB()
		self.emit(QtCore.SIGNAL("installSignal(int,str)"),100,str("Instalacion Finalizada."))
		cons.set_text_attr(self.default_colors)
	
	def uninstall(self):	
		self.removeAppDB()
		self.removeApp()
		self.stopService()
		self.removeMysqlService()
		self.removeMysql()
		'''sys.exit();'''
	
'''
def printHelp():
		print "Modo de uso:"
		print "\t -i o --install: instalar aplicacion."
		print "\t -u o --uninstall: desinstalar aplicacion "
'''

'''if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	try:               
		opts,args = getopt.getopt(sys.argv[1:], "iu", ["install", "uninstall"])

		confInstaller()
		inst=0
		uninst=0
		for o,a in opts:
			if( o in ("-i", "--install")):
				install()
			else:
				uninstall()
		printHelp()
		sys.exit()
	
				
	except getopt.GetoptError:
		printHelp()
		sys.exit()

	sys.exit(app.exec_())
'''