from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
from db_manager import len_rows, get_data, add_client


class Main_window(QMainWindow):
	def __init__(self):
		super(Main_window, self).__init__()
		uic.loadUi('main_window.ui', self)
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

	def in_dialog(self):
		self.dialog = Dialog_window()
		self.dialog.show()


class Dialog_window(QDialog):
	def __init__(self):
		super(Dialog_window, self).__init__()
		uic.loadUi("dialog_for_main.ui", self)
		self.buttonBox.accepted.connect(lambda: add_client(self.line_fio.text(),
				self.line_passport.text(), self.line_phone.text()))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Main_window()
	win.show()
	sys.exit(app.exec_())