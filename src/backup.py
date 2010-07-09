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
	os.system('"'+check.findMysqlPath()+'\\bin\\mysqldump.exe" '+ "--opt --password="+password+" --user="+user+" "+db+" >"+fileOut)

	
def loadDatabase(db,user,password,fileOut):
	print '"'+check.findMysqlPath()+'\\bin\\mysql.exe" '+ "-h localhost --password="+password+" --user="+user+" "+db+" < "+fileOut
	os.system('"'+check.findMysqlPath()+'\\bin\\mysql.exe" '+ " --password="+password+" --user="+user+" "+db+" < "+fileOut)
	

