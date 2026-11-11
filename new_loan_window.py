from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from datetime import datetime
from db_manager import add_loan


class New_loan_window(QMainWindow):         # класс окна приложения для добавления нового займа
	def __init__(self, data):
		super(New_loan_window, self).__init__()
		uic.loadUi("ui/new_loan_window.ui", self)
		self.client_id = data["id"]         # импорт данных с класса окна для просмотра займов
		self.client_name = data["name"]
		self.setWindowTitle("Новый займ")
		self.setFixedSize(331, 236)

		self.label_4.setPixmap(QPixmap("background/dollar_new_loan.jpg"))
		self.pushButton.clicked.connect(self.getLoan)       # кнопка добавления нового займа

	def getLoan(self):
		# добавление в БД id клиента, суммы займа, времени добавления займа, срока в мес. и процентной ставки
		try:
			add_loan(self.client_id, float(self.lineEdit.text()), datetime.now().strftime("%Y-%m-%d"),
				int(self.lineEdit_2.text()), float(self.lineEdit_3.text()))
			QMessageBox.warning(self, "Займ был создан", "Пожалуйста, перезапустите приложение для внесения изменений!")
			self.hide()
		except ValueError as e:     # обработка ошибки с неверным типом добавленных данных
			QMessageBox.warning(self, "Ошибка", "Данные введены в неправильном формате!")