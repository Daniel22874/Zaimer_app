from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
from db_manager import add_payment
from datetime import datetime


class New_payment_window(QMainWindow):
	def __init__(self):
		super(QMainWindow, self).__init__()
		uic.loadUi("ui/new_payment_window.ui", self)
		self.pushButton.clicked.connect(self.add_pay)

	def add_pay(self):
		print(self.lineEdit.text())
		print(self.lineEdit_2.text())
		date = datetime.now().strftime("%Y-%m-%d")
		add_payment(float(self.lineEdit.text()), date, self.lineEdit_2.text())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = New_payment_window()
	win.show()
	sys.exit(app.exec_())