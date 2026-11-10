from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from db_manager import len_rows_loans, get_loans
from new_loan_window import New_loan_window
from new_payment_window import New_payment_window
from history_payment_window import History_payment_window


class Loans_window(QMainWindow):
	def __init__(self, data):
		super(Loans_window, self).__init__()

		self.data = data
		self.client_id = data["id"]
		self.client_name = data["name"]
		uic.loadUi("ui/loans_window.ui", self)
		self.label.setPixmap(QPixmap("background/dollar_loans.jpg"))
		self.loan_table = QTableWidget()
		self.loan_table.setColumnCount(6)
		self.loan_table.setRowCount(len_rows_loans())
		self.loan_table.setHorizontalHeaderLabels(["id", "amount", "issue date", "term months", "interest rate", "status"])
		for row in range(len(get_loans(self.client_id))):
			for col in range(len(get_loans(self.client_id)[row])):
				self.loan_table.setItem(row, col, QTableWidgetItem(str(get_loans(self.client_id)[row][col])))

		self.verticalLayout.addWidget(self.loan_table)

		self.setWindowTitle(self.client_name)
		self.setFixedSize(800, 600)
		self.back_button.clicked.connect(self.open_main_window)
		self.new_loan_button.clicked.connect(self.open_new_loan_window)
		self.payment_button.clicked.connect(self.open_new_payment_window)
		self.history_payment_button.clicked.connect(self.open_history_payment_window)

	def open_main_window(self):
		self.hide()

	def open_new_loan_window(self):
		self.win = New_loan_window(self.data)
		self.win.show()

	def open_new_payment_window(self):
		items = [el.text() for el in self.loan_table.selectedItems()]
		if len(items) != 6 or 'closed' in items:
			QMessageBox.warning(self, "Ошибка", "Выбери займ для его погашения!")
		else:
			row = self.loan_table.currentRow()
			data = {
				"id": self.loan_table.item(row, 0).text(),
				"amount": self.loan_table.item(row, 1).text()
			}
			self.win = New_payment_window(data)
			self.win.show()

	def open_history_payment_window(self):
		self.win = History_payment_window(self.data)
		self.win.show()