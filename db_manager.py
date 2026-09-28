import sqlite3 as sq


def len_rows():
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM clients")
        res = cursor.fetchall()
        return len(res)


def get_data():
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM clients")
        res = cursor.fetchall()
        return res


def add_client(fio, passport, phone):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO clients (full_name, passport, phone) VALUES (?, ?, ?)", (fio, passport, phone))


def len_rows_loans():
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM loans")
        res = cursor.fetchall()
        return len(res)


def add_loan(amount, issue_date, term_months, interest_rate):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO loans (client_id, amount, issue_date, term_months, interest_rate, status) "
                       "VALUES ('Романов Роман Александрович', ?, ?, ?, ?, 'active')",
                       (amount, issue_date, term_months, interest_rate))


def add_payment(amount, payment_date, comment):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO payments (loan_id, amount, payment_date, comment) VALUES (3, ?, ?, ?)",
                       (amount, payment_date, comment))