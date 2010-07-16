import os
import sys
import getopt
import subprocess
import stat
import shutil
import connection
import exceptions
import win32con


tmpPathConfFile = open("installerConf.dat", "r")
tmpPath=os.path.expandvars(tmpPathConfFile.readline().split("=")[-1].split(";")[0])
tmpPathConfFile.close()

def isBDServiceInstalled():
	res=0
	try:
		'''subprocess.call('reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MySQL',stderr=open(tmpPath+'\\outReg.dat', 'w'))'''
		'''subprocess.Popen('reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MySQL',stderr=open(tmpPath+'\\outReg.dat', 'w'),creationflags = win32con.CREATE_NO_WINDOW)'''
		os.system('reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MySQL > '+tmpPath+'\\outReg.dat')
		file_stats = os.stat(tmpPath+'\\outReg.dat')
		if(file_stats [stat.ST_SIZE]!=0):
			res=1
		'''os.remove(os.path.normcase(tmpPath+"\\outReg.dat"))'''
	except Exception as inst:
		print inst
		
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
	'''subprocess.Popen('NET STOP MySQL',stderr=open(tmpPath+'\\outService.dat', "w"),stdout=open(tmpPath+'\\out.dat', 'w'),creationflags = win32con.CREATE_NO_WINDOW)'''
	os.system('NET STOP MySQL > '+tmpPath+'\\outService.dat')
	file_stats = os.stat(tmpPath+'\\outService.dat')
	if(file_stats [stat.ST_SIZE]!=0):
		os.system('NET START MySQL')
		res=1
	'''os.remove(os.path.normcase(tmpPath+"\\outService.dat"))'''
	return res
	
def checkRoot(passw):
	res=1
	try:
		conn=connection.Connection(dbName="mysql", dbUser="root", dbPass=passw)
		conn.open()
		conn.close()
	except:
		conn.close()
		res=0
	
	return res
	

	