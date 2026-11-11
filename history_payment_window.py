from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from db_manager import get_payments, len_rows_payments


class History_payment_window(QMainWindow):         # класс окна приложения с историей платежей
	def __init__(self, data):
		super(History_payment_window, self).__init__()
		uic.loadUi("ui/history_payment_window.ui", self)
		self.client_id = data["id"]                     # импорт данных с класса окна для просмотра займов
		self.client_name = data["name"]
		self.setWindowTitle("История внесения платежей")
		self.setFixedSize(611, 451)

		self.label_2.setPixmap(QPixmap('background/dollar_history_payment.jpg'))
		self.table = QTableWidget()
		self.table.setColumnCount(3)                    # 3 колонки в таблице
		self.table.setRowCount(len_rows_payments())     # кол-во строк == кол-ву платежей клиента
		self.table.setHorizontalHeaderLabels(["Дата", "Сумма", "Комментарий"])
		self.verticalLayout.addWidget(self.table)       # отображение таблицы в приложении
		# добавление платежей клиента из БД в таблицу
		for row in range(len(get_payments(self.client_id))):
			for col in range(len(get_payments(self.client_id)[row])):
				self.table.setItem(row, col, QTableWidgetItem(str(get_payments(self.client_id)[row][col])))

