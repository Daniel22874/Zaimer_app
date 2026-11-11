import sqlite3 as sq


def init_db():          # создание БД при запуске приложения
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        # создание таблицы clients
        cursor.execute("""CREATE TABLE IF NOT EXISTS clients
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                passport TEXT NOT NULL,
                phone TEXT NOT NULL)
                """)
        # создание таблицы loans
        cursor.execute("""CREATE TABLE IF NOT EXISTS loans
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                issue_date TEXT NOT NULL,
                term_months INTEGER NOT NULL,
                interest_rate REAL NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (client_id) REFERENCES clients(id))
                """)
        # создание таблицы payments
        cursor.execute("""CREATE TABLE IF NOT EXISTS payments
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                loan_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                payment_date TEXT NOT NULL,
                comment TEXT,
                FOREIGN KEY (loan_id) REFERENCES loans(id))
                """)


def len_rows():        # возвращает кол-во клиентов добавленных в БД
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM clients")
        res = cursor.fetchall()
        return len(res)


def get_clients():     # возвращает клиентов добавленных в БД
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM clients")
        res = cursor.fetchall()
        return res


def get_loans(client_id):       # возвращает займы заданного клиента
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT id, amount, issue_date, term_months, interest_rate, status FROM loans "
                       "WHERE client_id = ?", (client_id, ))
        res = cursor.fetchall()
        return res


def add_client(fio, passport, phone):       # добавление данных клиента в БД
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO clients (full_name, passport, phone) VALUES (?, ?, ?)", (fio, passport, phone))


def len_rows_loans():                       # возвращает кол-во займов добавленных в БД
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM loans")
        res = cursor.fetchall()
        return len(res)


def len_rows_payments():                    # возвращает кол-во платежей из БД
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM payments")
        res = cursor.fetchall()
        return len(res)


def add_loan(client_id, amount, issue_date, term_months, interest_rate):    # добавление нового займа в БД
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO loans (client_id, amount, issue_date, term_months, interest_rate, status) "
                       "VALUES (?, ?, ?, ?, ?, 'active')",
                       (client_id, amount, issue_date, term_months, interest_rate))


def add_payment(loan_id, amount, payment_date, comment):            # добавление внесённого платежа в БД
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO payments (loan_id, amount, payment_date, comment) VALUES (?, ?, ?, ?)",
                       (loan_id, amount, payment_date, comment))


def get_payments(client_id):        # возвращает платежи заданного клиента
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT payment_date, amount, comment FROM payments WHERE loan_id IN ("
                       "SELECT id FROM loans WHERE client_id = ?)", (client_id, ))
        res = cursor.fetchall()
        return res


def update_status_loan(loan_id):    # обновление статуса клиента, который погасил займ
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("UPDATE loans SET status = 'closed' WHERE id = ?", (loan_id, ))