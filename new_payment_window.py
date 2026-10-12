from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from db_manager import add_payment
from datetime import datetime


class New_payment_window(QMainWindow):
	def __init__(self, data):
		super(QMainWindow, self).__init__()
		uic.loadUi("ui/new_payment_window.ui", self)
		self.client_id = data["id"]
		self.client_name = data["name"]
		self.setWindowTitle("Внести платёж")
		self.setFixedSize(408, 208)

		self.label_3.setPixmap(QPixmap("background/dollar_new_payment.jpg"))
		self.pushButton.clicked.connect(self.add_pay)

	def add_pay(self):
		print(self.lineEdit.text())
		print(self.lineEdit_2.text())
		date = datetime.now().strftime("%Y-%m-%d")
		add_payment(float(self.lineEdit.text()), date, self.lineEdit_2.text())
