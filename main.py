from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLabel
from PyQt5 import uic
import sys
from test import len_rows, get_data, add_client
from loans_window import Loans_window


class Main_window(QMainWindow):
	def __init__(self):
		super(Main_window, self).__init__()
		uic.loadUi('ui/main_window.ui', self)
		self.setUI()

	def setUI(self):
		self.table = QTableWidget()
		self.table.setRowCount(len_rows())
		self.table.setColumnCount(4)
		self.table.setHorizontalHeaderLabels(["id", "ФИО", "Паспорт", "Телефон"])

		for row in range(len(get_data())):
			for col in range(len(get_data()[row])):
				self.table.setItem(row, col, QTableWidgetItem(get_data()[row][col]))

		self.verticalLayout.addWidget(self.table)
		self.pushButton.clicked.connect(self.in_dialog)
		self.pushButton_2.clicked.connect(self.open_loans_window)

		self.status = QLabel(f"Кол-во клиентов: {len_rows()}, кол-во займов: 5")
		self.statusBar().addWidget(self.status)

	def in_dialog(self):
		self.dialog = Dialog_window()
		self.dialog.show()

	def open_loans_window(self):
		self.win = Loans_window()
		self.win.show()


class Dialog_window(QDialog):
	def __init__(self):
		super(Dialog_window, self).__init__()
		uic.loadUi("ui/dialog_for_main.ui", self)
		self.buttonBox.accepted.connect(lambda: add_client(self.line_fio.text(),
				self.line_passport.text(), self.line_phone.text()))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Main_window()
	win.show()
	sys.exit(app.exec_())