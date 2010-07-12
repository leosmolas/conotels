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

	backupQuery=os.path.normcase('"'+check.findMysqlPath()+'\\mysqldump.exe"')+ ' --opt --password='+password+' --user='+user+' '+db+' > auxFile.sql'
	os.system(backupQuery)
	os.system('copy auxFile.sql "'+ fileOut+'"')
	os.system('del auxFile.sql')
	
def loadDatabase(db,user,password,fileOut):
	os.system('copy "'+ fileOut+'" auxFile.sql')
	os.system('"'+check.findMysqlPath()+'\\mysql.exe" '+ " --password="+password+" --user="+user+" "+db+' < auxFile.sql' )
	os.system('del auxFile.sql')
	

