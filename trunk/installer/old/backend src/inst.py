import os
import sys
import getopt
import subprocess
import stat
import shutil
import check
import commands
from PyQt4 import QtCore,QtGui,QtSql
from connection import Connection
import color_console as cons
import copy


def confInstaller():
	global tmpPathConfFile,tmpPath,inputConfFileName,outputInstallerFile,inputData,default_colors,default_bg
	tmpPathConfFile = open("installerConf.dat", "r")
	tmpPath=os.path.expandvars(tmpPathConfFile.readline().split("=")[-1].split(";")[0])
	inputConfFileName=os.path.normcase(tmpPath+'\\conf.dat')
	inputData = {"inputInstallScript":None,"inputUninstallScript":None,"dirApp":None,"dirMysql":None,"newRootPass":None,"defaultDatabase":None,"applicationDatabase":None,"userRoot":None,"oldRootPass":None}
	default_colors = cons.get_text_attr()
	default_bg = default_colors & 0x0070
	readConf()
	

def setInstColor():
	cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                     cons.FOREGROUND_INTENSITY)
	
def mysqlDirectoryExists():
	res=0
	if(os.path.isdir(inputData["dirMysql"])):
		res=1
	return res
	
def printHeader(str):
	cons.set_text_attr(cons.FOREGROUND_RED | default_bg |
                     cons.FOREGROUND_INTENSITY)
	print str
	cons.set_text_attr(default_colors)
	
def printWarning(str):
	cons.set_text_attr(cons.FOREGROUND_YELLOW  | default_bg |
                     cons.FOREGROUND_INTENSITY)
	print str
	cons.set_text_attr(default_colors)
	
	
def installMysql():
	printHeader("Instalando MySQL...")
	setInstColor()
	if(mysqlDirectoryExists()==1):
			printWarning('Atencion: se borraran los archivos de este directorio.')
			removeMysql()
	os.system('mkdir "'+ inputData["dirMysql"]+'"')
	os.system('xcopy "..\mysql\*.*" "'+ inputData["dirMysql"]+'" /e')


def installApp():
	printHeader("Instalando Aplicacion...")
					 
	if(appDirectoryExists()==1):
			printWarning("EL directorio no esta vacio. Se borrara el contenido.")
			removeApp()
	setInstColor()
	os.system('mkdir "' + inputData["dirApp"]+'"')
	os.system('xcopy "..\\app\*.*" "'+ inputData["dirApp"]+'" /e')
	cons.set_text_attr(default_colors)
	

	
def appDirectoryExists():
	res=0
	if(os.path.isdir(inputData["dirApp"])):
		res=1
	return res
	
def installService():
	printHeader("Instalando Servicio MySQL...")
	setInstColor()
	os.system('"'+inputData["dirMysql"]+'\\bin\\mysqld" --install')
	cons.set_text_attr(default_colors)

	
def runService():
	printHeader("Iniciando Servicio MySQL...")
	setInstColor()
	os.system('NET START MySql')
	cons.set_text_attr(default_colors)


def stopService():
	printHeader("Deteniendo Servicio MySQL...")
	setInstColor()
	os.system('NET STOP MySQL')
	cons.set_text_attr(default_colors)

			
	
def removeMysql():
	printHeader("Eliminando archivos de MySQL...")
	shutil.rmtree(inputData["dirMysql"])

	

def removeApp():
	printHeader("Desinstalando Aplicacion...")
	shutil.rmtree(inputData["dirApp"])

	
def removeMysqlService():
	printHeader("Desinstalando Servicio MySQL...")
	os.system('"'+check.findMysqlPath() +'\\mysqld" --remove')

	
def removeAppDB():
	printHeader("Eliminando Base de Datos...")
	setInstColor()
	os.system('"'+check.findMysqlPath()+'\\mysql.exe" -u '+inputData["userRoot"]+' --password='+inputData["newRootPass"]+' '+inputData["applicationDatabase"]+ '< '+inputData["inputUninstallScript"])
	os.system('NET STOP MySql')
	os.system('NET START MySql')
	cons.set_text_attr(default_colors)

	
def createShortCut():
	printHeader("Creando acceso directo en el Escritorio...")
	setInstColor()
	if(os.path.isdir(os.path.expandvars("%USERPROFILE%")+"\\Escritorio")):
		print 'SHORTCUT /f:"'+os.path.expandvars("%USERPROFILE%")+'\\Escritorio\Conotels.lnk" /a:c /t:"'+inputData["dirApp"]+'\main.exe" /W:"'+inputData["dirApp"]+'\\" /I:"'+inputData["dirApp"]+'\\icon.ico"'
		os.system('SHORTCUT /f:"'+os.path.expandvars("%USERPROFILE%")+'\\Escritorio\Conotels.lnk" /a:c /t:"'+inputData["dirApp"]+'\main.exe" /W:"'+inputData["dirApp"]+'\\" /I:"'+inputData["dirApp"]+'\\icon.ico"' )
	else:
		os.system('SHORTCUT /f:"'+os.path.expandvars("%USERPROFILE%")+'\\Desktop\Conotels.lnk" /a:c /t:"'+inputData["dirApp"]+'\main.exe" /W:"'+inputData["dirApp"]+'\\" /I:"'+inputData["dirApp"]+'\\icon.ico"'  )
	cons.set_text_attr(default_colors)

def confRoot():
	printHeader("Configurando usuario root...")
	setInstColor()
	conn=Connection(dbName=inputData["defaultDatabase"], dbUser=inputData["userRoot"], dbPass=inputData["oldRootPass"])
	conn.open()
	conn.update("UPDATE "+inputData["defaultDatabase"]+".user SET Password=PASSWORD("+mysqlString(inputData["newRootPass"])+") WHERE User='"+inputData["userRoot"]+"';")
	conn.close()
	os.system('NET STOP MySql')
	os.system('NET START MySql')
	cons.set_text_attr(default_colors)

		
def confDB():
	printHeader("Configurando base de datos de la aplicacion...")
	setInstColor()
	conn=Connection(dbName=inputData["defaultDatabase"], dbUser=inputData["userRoot"], dbPass=inputData["newRootPass"])
	conn.open()
	conn.update("drop database if exists "+inputData["applicationDatabase"]+";")
	conn.update("create database if not exists "+inputData["applicationDatabase"]+";")
	conn.close()
	os.system('"'+check.findMysqlPath()+'\\mysql.exe" -u '+inputData["userRoot"]+' --password='+inputData["newRootPass"]+' '+inputData["applicationDatabase"]+ '< ..\\bd\\'+inputData["inputInstallScript"])
	os.system('NET STOP MySql')
	os.system('NET START MySql')
	cons.set_text_attr(default_colors)

	
def readConf():

	inputConfFile = open(inputConfFileName,"r")

	for line in inputConfFile.readlines():
		if(line.find("dirMysql")==0):
			inputData["dirMysql"]=line.split("=")[-1].split(";")[0]	
		if(line.find("newRootPass")==0):
			inputData["newRootPass"]=line.split("=")[-1].split(";")[0]	
		if(line.find("defaultDatabase")==0):
			inputData["defaultDatabase"]=line.split("=")[-1].split(";")[0]
		if(line.find("applicationDatabase")==0):
			inputData["applicationDatabase"]=line.split("=")[-1].split(";")[0]
		if(line.find("userRoot")==0):
			inputData["userRoot"]=line.split("=")[-1].split(";")[0]	
		if(line.find("oldRootPass")==0):
			inputData["oldRootPass"]=line.split("=")[-1].split(";")[0]	
		if(line.find("inputUninstallScript")==0):
			inputData["inputUninstallScript"]=line.split("=")[-1].split(";")[0]	
		if(line.find("dirApp")==0):
			inputData["dirApp"]=line.split("=")[-1].split(";")[0]	
		if(line.find("inputInstallScript")==0):
			inputData["inputInstallScript"]=line.split("=")[-1].split(";")[0]	
			
			
	for key in inputData.keys():
		if(inputData[key]==None):
			print "Parametros de archivo de configuracion incorrectos"
			sys.exit()


def mysqlString(str):
	return "'"+str+"'"
			

	

def install():
	
	if(not check.isBDServiceInstalled()):
		installMysql()
		installService()
		runService()
		confRoot()

	else:
		if(not check.isBDServiceRunning()):
			runService()

	
	installApp()
	createShortCut()
	confDB()
	
	sys.exit()
	

	
	
def uninstall():	
	removeAppDB()
	removeApp()
	stopService()
	removeMysqlService()
	removeMysql()
	

	sys.exit();
	
def printHelp():
		print "Modo de uso:"
		print "\t -i o --install: instalar aplicacion."
		print "\t -u o --uninstall: desinstalar aplicacion "

if __name__ == "__main__":
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
