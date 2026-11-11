from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
from db_manager import len_rows, get_clients, add_client, len_rows_loans, init_db
from loans_window import Loans_window


class Main_window(QMainWindow):                 # класс основного окна приложения
	def __init__(self):
		super(Main_window, self).__init__()
		uic.loadUi('ui/main_window.ui', self)
		self.setFixedSize(801, 591)             # фиксированные габариты окна
		self.setUI()

	def setUI(self):
		self.setWindowTitle("Zаймер")
		self.table = QTableWidget()
		self.table.setRowCount(len_rows())      # таблица имеет кол-во строк по кол-ву имеющихся клиентов из БД
		self.table.setColumnCount(4)            # 4 столбца
		self.table.setHorizontalHeaderLabels(["id", "ФИО", "Паспорт", "Телефон"])
		# добавление данных клиентов из БД в таблицу
		for row in range(len(get_clients())):
			for col in range(len(get_clients()[row])):
				self.table.setItem(row, col, QTableWidgetItem(str(get_clients()[row][col])))

		self.verticalLayout.addWidget(self.table)       # отображение таблицы в приложении

		self.label.setPixmap(QPixmap("background/dollar_main.jpg"))
		self.pushButton.clicked.connect(self.in_dialog)     # нажатие кнопки с добавлением клиента
		self.pushButton_2.clicked.connect(self.open_loans_window)   # нажатие кнопки просмотра займов

		self.status = QLabel(f"Кол-во клиентов: {len_rows()}, кол-во займов: {len_rows_loans()}")
		self.statusBar().addWidget(self.status)     # отображение статуса о кол-ве клиентов и займов

	def in_dialog(self):                        # запуск окна добавления клиента
		self.dialog = Dialog_window()
		self.dialog.show()

	def open_loans_window(self):                # запуск окна просмотра займов выделенного клиента в таблице
		if not self.table.selectedItems():
			QMessageBox.warning(self, "Ошибка", "Выбери клиента")
		else:
			row = self.table.currentRow()       # импорт нужных данных для использования в окне просмотра займов
			data = {
				"id": self.table.item(row, 0).text(),
				"name": self.table.item(row, 1).text()
			}
			self.win = Loans_window(data)
			self.win.show()


class Dialog_window(QDialog):
	def __init__(self):
		super(Dialog_window, self).__init__()
		uic.loadUi("ui/dialog_for_main.ui", self)
		self.setWindowTitle("Добавить клиента")
		self.setFixedSize(401, 300)
		self.label_4.setPixmap(QPixmap("background/dollar_dialog.jpg"))
		self.buttonBox.accepted.connect(self.agree)

	def agree(self):
		# проверка на заполненность всех полей при добавлении клиента
		if len(self.line_fio.text()) == 0 or len(self.line_passport.text()) == 0 or len(self.line_phone.text()) == 0:
			QMessageBox.warning(self, "Ошибка", "Не все поля заполнены!")
			return
		QMessageBox.warning(self, "Клиент был добавлен", "Пожалуйста, перезапустите приложение для внесения изменений!")
		add_client(self.line_fio.text(), self.line_passport.text(), self.line_phone.text())


if __name__ == '__main__':
	app = QApplication(sys.argv)
	init_db()
	win = Main_window()
	win.show()
	sys.exit(app.exec_())