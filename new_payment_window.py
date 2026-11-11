from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from db_manager import add_payment
from datetime import datetime
from db_manager import update_status_loan


class New_payment_window(QMainWindow):         # класс окна приложения для внесения платежа
	def __init__(self, data):
		super(New_payment_window, self).__init__()
		uic.loadUi("ui/new_payment_window.ui", self)
		self.loan_id = data["id"]               # импорт данных с класса окна для просмотра займов
		self.amount = data["amount"]
		self.setWindowTitle("Внести платёж")
		self.setFixedSize(408, 208)

		self.label_3.setPixmap(QPixmap("background/dollar_new_payment.jpg"))
		self.pushButton.clicked.connect(self.add_pay)       # кнопка добавления платежа

	def add_pay(self):
		date = datetime.now().strftime("%Y-%m-%d")
		if float(self.lineEdit.text()) > float(self.amount):    # если вернули больше чем должны
			# добавление в БД id закрываемого займа, суммы платежа, даты погашения займа, комментария
			add_payment(self.loan_id, float(self.lineEdit.text()), date, self.lineEdit_2.text())
			update_status_loan(self.loan_id)        # обновления статуса займа с aсtive на closed
			QMessageBox.warning(self, "Оплата займа прошла",
			f"Ваша сдача: {float(self.lineEdit.text()) - float(self.amount)}. Перезапустите для внесения изменений!")
			self.hide()
		if float(self.lineEdit.text()) == float(self.amount):   # если вернули столько, сколько и должны
			# добавление в БД id закрываемого займа, суммы платежа, даты погашения займа, комментария
			add_payment(self.loan_id, float(self.lineEdit.text()), date, self.lineEdit_2.text())
			update_status_loan(self.loan_id)        # обновления статуса займа с aсtive на closed
			QMessageBox.warning(self, "Оплата займа прошла",
			f"Ваша сдача: {float(self.lineEdit.text()) - float(self.amount)}. Перезапустите для внесения изменений!")
			self.hide()
		if float(self.lineEdit.text()) < float(self.amount):    # еcли вернули не всю сумму
			QMessageBox.warning(self, "Оплата займа не прошла",
			"Вносимая сумма меньше суммы для погашения долга!")




