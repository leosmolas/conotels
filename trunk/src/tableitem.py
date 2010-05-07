from PyQt4 import QtCore,QtGui

# 0 - Libre
# 1 - Pre Reservado
# 2 - Reserva confirmada
# 3 - Reserva en curso

class TableItem(QtGui.QTableWidgetItem):
	def __init__(self, reserva = -1, tipo = 0, init = False):
		super(TableItem, self).__init__()

		if init:
			self.setText("*")

		self.reserva = reserva
		self.tipo = tipo

		color = QtGui.QColor(255,255,255)
	
		if tipo == 0:
			color = QtGui.QColor(255,255,255)
		elif tipo == 1:
			color = QtGui.QColor(190,190,210)
		elif tipo == 2:
			color = QtGui.QColor(96,187,34)
		elif tipo == 3:
			color = QtGui.QColor(59,107,156)

		self.setBackground(QtGui.QBrush(color))
