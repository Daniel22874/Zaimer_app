from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidget
from PyQt5 import uic
import sys


class History_payment_window(QMainWindow):
	def __init__(self):
		super(QMainWindow, self).__init__()
		uic.loadUi("ui/history_payment_window.ui", self)
		self.table = QTableWidget()
		self.table.setColumnCount(3)
		self.table.setRowCount(12)
		self.table.setHorizontalHeaderLabels(["Дата", "Сумма", "Комментарий"])
		self.verticalLayout.addWidget(self.table)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = History_payment_window()
	win.show()
	sys.exit(app.exec_())