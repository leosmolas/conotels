# -*- coding: utf-8 -*-

from PyQt4 import QtCore,QtGui

# 0 - Libre
# 1 - Reserva confirmada
# 2 - Pre Reservado
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
			color = QtGui.QColor(255, 207, 14)
		elif tipo == 2:
			color = QtGui.QColor(111, 183, 231)		
		elif tipo == 3:
			color = QtGui.QColor(34, 227, 99)

		self.setBackground(QtGui.QBrush(color))
