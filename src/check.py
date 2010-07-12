import os
import sys
import getopt
import subprocess
import stat
import shutil
from connection.connection import Connection

tmpPathConfFile = open("installerConf.dat", "r")
tmpPath=os.path.expandvars(tmpPathConfFile.readline().split("=")[-1].split(";")[0])
tmpPathConfFile.close()

def isBDServiceInstalled():
	res=0
	subprocess.call('reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MySQL',stderr=open(tmpPath+'\\outReg.dat', 'w'))
	file_stats = os.stat(tmpPath+'\\outReg.dat')
	if(file_stats [stat.ST_SIZE]==0):
		res=1
	'''os.remove(os.path.normcase(tmpPath+"\\outReg.dat"))'''
	return res
	
def findMysqlPath():
	os.system('reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MySQL /v ImagePath > "'+tmpPath+'\\outReg.dat"')
	fout=open(tmpPath+'\\outReg.dat','r')
	out= fout.read().split('"')[1].split('mysqld')[0]
	fout.close()
	'''os.system('del '+os.path.normcase(tmpPath+"\\outReg.dat"))'''
	return os.path.normcase(out)
	
	
def isBDServiceRunning():
	res=0
	subprocess.call('NET STOP MySQL',stderr=open(os.path.expandvars("%HOMEDRIVE%")+'\\outService.dat', "w"),stdout=open(tmpPath+'\\out.dat', 'w'))
	file_stats = os.stat(tmpPath+'\\outService.dat')
	if(file_stats [stat.ST_SIZE]==0):
		os.system('NET START MySQL')
		res=1
	'''os.remove(os.path.normcase(tmpPath+"\\outService.dat"))'''
	return res
	
def checkRoot(passw):
	res=1
	
	try:
		conn=Connection(dbName="mysql", dbUser="root", dbPass=passw)
		conn.open()
	except:
		res=0
		
	return res
	

	