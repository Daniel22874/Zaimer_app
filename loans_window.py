from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys


class Loans_window(QMainWindow):
	def __init__(self):
		super(Loans_window, self).__init__()
		uic.loadUi("ui/loans_window.ui", self)
		self.setWindowTitle("ФИО клиента")
		self.back_button.clicked.connect(self.open_main_window)

	def open_main_window(self):
		self.hide()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Loans_window()
	win.show()
	sys.exit(app.exec_())
