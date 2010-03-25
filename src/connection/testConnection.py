import sys
from PyQt4 import QtCore,QtGui,QtSql
from GUI import Ui_Dialog
from connection import Connection
from error import ConnectionError
if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	conn=Connection("QMYSQL","localhost","cursos","root","")
	conn.open()
	model=conn.query("select * from empleado")
	Dialog = QtGui.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	ui.tableView.setModel(model)
	ui.tableView.show()
	
	
	try:
		conn.update("insert into empresa values(145,'ConoSoft123')")
	except ConnectionError as inst:
		print inst.getMsg()
	
	Dialog.show()
	conn.close()
	sys.exit(app.exec_())