from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from datetime import datetime
from db_manager import add_loan


class New_loan_window(QMainWindow):
	def __init__(self, data):
		super(New_loan_window, self).__init__()
		uic.loadUi("ui/new_loan_window.ui", self)
		self.client_id = data["id"]
		self.client_name = data["name"]
		self.setWindowTitle("Новый займ")
		self.setFixedSize(331, 236)

		self.label_4.setPixmap(QPixmap("background/dollar_new_loan.jpg"))
		self.pushButton.clicked.connect(self.getLoan)

	def getLoan(self):
		add_loan(self.client_id, float(self.lineEdit.text()), datetime.now().strftime("%Y-%m-%d"), int(self.lineEdit_2.text()),
			float(self.lineEdit_3.text()))