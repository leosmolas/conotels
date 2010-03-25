import sys
from PyQt4 import QtCore,QtGui,QtSql
from error import ConnectionError

"""
Clase de conexion a una Base de Datos
"""
class Connection:
	
	"""
	Constructor de la Clase.
	*Parametros:
		1) 	dbDriver:	string, driver de la Base de Datos.
		2) 	dbHost: 	string, host.
		3)	dbName:		string, nombre de la Base de Datos.
		4)	dbUser:		string, nombre de usuario.
		5)	dbPass: 	string, password del usuario.
	*Excepciones: nada.
	"""
	def __init__(self,dbDriver,dbHost,dbName,dbUser,dbPass):
		#Se crea una instancia de QsqlQueryModel usada para las consultas
		self.model=QtSql.QSqlQueryModel()
			
		#Se crea una instancia QSqlDatabase
		self.db=QtSql.QSqlDatabase()
		
		#Se crea una instancia de QsqlQuery usada para las actualizaciones
		self.updateQuery=QtSql.QSqlQuery(self.db)
		#Se setea el driver de la base de datos
		self.db=QtSql.QSqlDatabase.addDatabase(dbDriver)
		#Se setea el nombre del host
		self.db.setHostName(dbHost)
		#Se setea el nombre de la Base de Datos
		self.db.setDatabaseName(dbName)
		#Se setea el nombre de usuario
		self.db.setUserName(dbUser)
		#Se setea el password del usuario
		self.db.setPassword(dbPass)	
    	
   	"""
    Metodo para abrir la conexion.
    *Parametros: nada.
    *Retorno: nada.
    *Excepciones: Si al intentar abrir la conexion falla, emite una excepcion de la clase ConnectionError.
	"""
	def open(self):
		if not self.db.open():
			msg="Error al intentar abrir la Base de Datos: "+self.db.lastError().text()
			raise ConnectionError(msg)
			
	"""
	Metodo para cerrar la conexion.	
	*Parametros: nada.
	*Retorno: nada.
	*Excepciones: nada.
	"""
	def close(self):
		return self.db.close()
		
	"""
	Metodo que retorna el contenido de la ultima consulta.
	*Parametros: nada.
	*Retorno:	QSqlQueryModel, el resultado de la ultima consulta.
	*Excepciones: nada.
	"""
	def getModel(self):
		return self.model
	
	"""
	Metodo para realizar una consulta.
	*Parametros:
		1)	strQuery:	string, sentencia SQL para la consulta.
	*Retorno:	QSqlQueryModel, el resultado de la consulta.
	*Excepciones: Si la consulta es incorrecta, emite una excepcion de la clase ConnectionError.
	"""
	def query(self,strQuery):
		self.model.setQuery(strQuery,self.db)
		query=self.model.query()
		if not query.exec_():
			msg="Error al intentar realizar la consulta: "+query.lastError().text()
			raise ConnectionError(msg)
		return self.model

	
	"""
	Metodo para realizar actualizaciones (ABM) en la Base de Datos.
	*Parametros:
		1)	strUpdateQuery:	string, sentencia SQL para el ABM.
	*Retorno: nada.
	*Excepciones: Si el ABM falla, emite una excepcion de la clase ConnectionError.
	"""
	def update(self,strUpdateQuery):
		self.updateQuery=QtSql.QSqlQuery(self.db)
		self.updateQuery.prepare(strUpdateQuery)
		if not self.updateQuery.exec_():
			msg="Error al intentar actualizar la Base de Datos: "+self.updateQuery.lastError().text()
			raise ConnectionError(msg)
			
		
	

	