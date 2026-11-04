from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from db_manager import get_payments


class History_payment_window(QMainWindow):
	def __init__(self, data):
		super(QMainWindow, self).__init__()
		uic.loadUi("ui/history_payment_window.ui", self)
		self.client_id = data["id"]
		self.client_name = data["name"]
		self.setWindowTitle("История внесения платежей")
		self.setFixedSize(611, 451)

		self.label_2.setPixmap(QPixmap('background/dollar_history_payment.jpg'))
		self.table = QTableWidget()
		self.table.setColumnCount(3)
		self.table.setRowCount(12)
		self.table.setHorizontalHeaderLabels(["Дата", "Сумма", "Комментарий"])
		self.verticalLayout.addWidget(self.table)

		for row in range(len(get_payments(self.client_id))):
			for col in range(len(get_payments(self.client_id)[row])):
				self.table.setItem(row, col, QTableWidgetItem(str(get_payments(self.client_id)[row][col])))

