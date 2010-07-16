import sys
from PyQt4 import QtCore,QtGui,QtSql,Qt
from GUITest import Ui_Dialog
from connection import Connection
from error import Error
from model import Model
import copy
if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	
	#Creo la conexion a la BD
	conn=Connection("bdtest","QMYSQL","localhost","root","",)
	
	try:
		#Abro la conexion
		conn.open()
	
		#Creo la GUI
		Dialog = QtGui.QDialog()
		
		#Esta linea es necesaria para que al cerrar la conexion no tire error
		Dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		
		ui = Ui_Dialog()
		ui.setupUi(Dialog)
		
		#Muestro el dialogo
		Dialog.show()
		
		#Inserto un nuevo valor en la Base de Datos
		#Notar que si se ejecuta dos veces el programa de prueba, tira una excepcion dado que la persona ya existe en ls bd
		conn.update("insert into persona(cuil,nombre,apellido,direccion) values (9,'Diego','Panqueque Mancovequio','Bala 535')")
	
		#model1=QtSql.QSqlQueryModel()
		#Cargo un QSqlQueryModel con una consulta (1)
		model1=conn.query("select * from persona")
	
		
		#Cargo un QSqlQueryModel con una consulta (2)
		model2=conn.query("select * from empresa")
	
		
		#Cargo un QSqlQueryModel con una consulta (3)
		model3=conn.query("select * from persona where cuil=1")
		
		#Cargo un QSqlQueryModel con una consulta (4)
		model4=conn.query("select * from empresa where id_empresa=1")
		
		
		#Vinculo model1 con la listView,  indico que quiero mostrar la columna "direccion" de la consulta (1) (model1)
		ui.listView.setModel(model1)
		ui.listView.setModelColumn(model1.record().indexOf("direccion"))
		
		        
		#Vinculo model1 con la tableView, de esta manera se muestra el resultado de la consulta (1) en la tableView
		ui.tableView.setModel(model1)
		#Vinculo model2 con la columnView, indico que quiero mostrar la columna "nombre" de la consulta (2) (model2)
		ui.columnView.setModel(model2)
		
		
		#Vinculo model2 con el comboBox
		ui.comboBox.setModel(model2)
		#Indico que quiero mostrar la columna "nombre" de la consulta (2) (model2)
		ui.comboBox.setModelColumn(model2.record().indexOf("nombre"))
		
		#Cargo en lineEdit el valor de la columna "nombres" de la consulta cargada en model4
		ui.lineEdit.setText(model4.getItem("nombre",0))
		#Analogo, pero con el textEdit, en este caso no indico la fila, por lo que implicitamente se asume la 0
		ui.textEdit.setText(model4.getItem("nombre"))
		#Analogo, pero con el plainTextEdit
		ui.plainTextEdit.setPlainText(model4.getItem("nombre"))
		
	
	#Si se produce alguna excepcion, muestro el mensaje por pantalla
	except Error as error:
		print error.getMsg()
	
	finally:
		#Cierro la conexion
		conn.close()
	sys.exit(app.exec_())