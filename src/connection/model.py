import sys
from PyQt4 import QtCore,QtSql
from error import Error

"""
Clase que hereda de QSqlQueryModel implementando metodos para retornar datos especificos de una consulta
"""
class Model(QtSql.QSqlQueryModel):
	
	"""
    Metodo para retornar el contenido de una celda correspondiente a la ultima consulta.
    *Parametros:	1)	columnName:	QString, nombre de la columns.
    				2)	rowIndex:	integer, valor por defecto=0, numero de fila.
    *Retorno:	QString, contenido de la consulta en una dada columna para una fila determinada.
    *Excepciones: nada.
	"""
	def getItem(self,columnName,rowIndex=0):
		if rowIndex<0 or self.rowCount()<=rowIndex:
			raise Error("Error al intentar acceder a la fila "+QtCore.QString.number(rowIndex),"Error de acceso a la tabla.")
		row=self.record(rowIndex)
		if row.isNull(columnName):
			raise Error("Error al intentar acceder a la columna de nombre '"+columnName+"'","Error de acceso a la tabla.")
			
		return  row.value(columnName).toString()
