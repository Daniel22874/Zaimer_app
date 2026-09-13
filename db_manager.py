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


def add_loan(amount, issue_date, term_months, interest_rate):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO loans (client_id, amount, issue_date, term_months, interest_rate, status) "
                       "VALUES ('Романов Роман Александрович', ?, ?, ?, ?, 'active')",
                       (amount, issue_date, term_months, interest_rate))

