import exceptions

"""
Clase que modela excepciones definidas por el usuario.
La idea es heredar de esta clase para definir excepciones especificas.
"""
class Error(Exception):
	"""
	Metodo para retornar mensaje de error de la excepcion.
	*Parametros: nada.
	*Excepciones: nada.
	*Retorno: nada.
	"""
	def getMsg(self):
		return self.msg

	"""
	Metodo para imprimir el mensaje de error de la excepcion.
	Se ejecuta automaticamante cuando la excepcion no es capturada, 
	antes de interrumpir la ejecucion del programa.
	*Parametros: nada.
	*Excepciones: nada.
	*Retorno: nada.
	"""
	def __str__(self):
		print "",self.msg
		
	pass

"""
Clase que modela una excepcion que puede ocurrir al interactuar con una Base de Datos.
"""
class ConnectionError(Error):
	"""
	*Constructor de la clase.
	*Parametros:
		1)	msg:	string, mensaje de error de la excepcion.
	*Excepciones: nada.
	"""
	def __init__(self, msg):
		self.msg = msg
