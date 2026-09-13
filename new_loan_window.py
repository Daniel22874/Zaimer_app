from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
from datetime import datetime
from db_manager import add_loan


class New_loan_window(QMainWindow):
	def __init__(self):
		super(New_loan_window, self).__init__()
		uic.loadUi("ui/new_loan_window.ui", self)
		self.pushButton.clicked.connect(self.getLoan)

	def getLoan(self):
		add_loan(float(self.lineEdit.text()), datetime.now().strftime("%Y-%m-%d"), int(self.lineEdit_2.text()),
			float(self.lineEdit_3.text()))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = New_loan_window()
	win.show()
	sys.exit(app.exec_())