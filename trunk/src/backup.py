import os
import sys
import getopt
import subprocess
import stat
import shutil
import check
import commands
from PyQt4 import QtCore,QtGui,QtSql

def backupDatabase(db,user,password,fileOut):
	file= fileOut.split('\\')[-1]
	path= fileOut.replace ( fileOut.split('\\')[-1], '' )[:-1]
	mysqlPath=check.findMysqlPath()[:-1]
	mysqldumpExe='"'+mysqlPath+'\\mysqldump.exe"'
	oldCurrDir=os.getcwd()
	os.chdir(path)
	backupQuery=mysqldumpExe+' --opt --password='+password+' --user='+user+' '+db+' > '+file
	os.system(backupQuery)
	os.chdir(oldCurrDir)

	
def loadDatabase(db,user,password,fileIn):

	file= fileIn.split('\\')[-1]
	path= fileIn.replace ( fileIn.split('\\')[-1], '' )[:-1]
	mysqlPath=check.findMysqlPath()[:-1]
	mysqldExe='"'+mysqlPath+'\\mysql.exe"'
	oldCurrDir=os.getcwd()
	os.chdir(path)
	backupQuery=mysqldExe+" --password="+password+" --user="+user+" "+db+' < '+file
	os.system(backupQuery)
	os.chdir(oldCurrDir)

	

