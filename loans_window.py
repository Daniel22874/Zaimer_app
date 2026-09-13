from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidget
from PyQt5 import uic
from db_manager import len_rows_loans


class Loans_window(QMainWindow):
	def __init__(self, data):
		super(Loans_window, self).__init__()
		self.client_id = data["id"]
		self.client_name = data["name"]
		uic.loadUi("ui/loans_window.ui", self)
		self.loan_table = QTableWidget()
		self.loan_table.setColumnCount(5)
		self.loan_table.setRowCount(len_rows_loans())
		self.loan_table.setHorizontalHeaderLabels(["amount", "issue date", "term months", "interest rate", "status"])

		self.verticalLayout.addWidget(self.loan_table)


		self.setWindowTitle(self.client_name)
		self.back_button.clicked.connect(self.open_main_window)

	def open_main_window(self):
		self.hide()
