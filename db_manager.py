import sqlite3 as sq


def len_rows():
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM clients")
        res = cursor.fetchall()
        return len(res)


def get_clients():
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM clients")
        res = cursor.fetchall()
        return res


def get_loans(client_id):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT id, amount, issue_date, term_months, interest_rate, status FROM loans "
                       "WHERE client_id = ?", (client_id, ))
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


def add_loan(client_id, amount, issue_date, term_months, interest_rate):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO loans (client_id, amount, issue_date, term_months, interest_rate, status) "
                       "VALUES (?, ?, ?, ?, ?, 'active')",
                       (client_id, amount, issue_date, term_months, interest_rate))


def add_payment(loan_id, amount, payment_date, comment):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO payments (loan_id, amount, payment_date, comment) VALUES (?, ?, ?, ?)",
                       (loan_id, amount, payment_date, comment))


def get_payments(client_id):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT payment_date, amount, comment FROM payments WHERE loan_id = ("
                       "SELECT id FROM loans WHERE client_id = ?)", (client_id, ))
        res = cursor.fetchall()
        return res


def update_status_loan(loan_id):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("UPDATE loans SET status = 'closed' WHERE id = ?", (loan_id, ))