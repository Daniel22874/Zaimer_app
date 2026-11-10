import sqlite3 as sq


def init_db():
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS clients
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                passport TEXT NOT NULL,
                phone TEXT NOT NULL)
                """)
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
        cursor.execute("""CREATE TABLE IF NOT EXISTS payments
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                loan_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                payment_date TEXT NOT NULL,
                comment TEXT,
                FOREIGN KEY (loan_id) REFERENCES loans(id))
                """)


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


def len_rows_payments():
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM payments")
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
        cursor.execute("SELECT payment_date, amount, comment FROM payments WHERE loan_id IN ("
                       "SELECT id FROM loans WHERE client_id = ?)", (client_id, ))
        res = cursor.fetchall()
        return res


def update_status_loan(loan_id):
    with sq.connect("zaimer.db") as connect:
        cursor = connect.cursor()
        cursor.execute("UPDATE loans SET status = 'closed' WHERE id = ?", (loan_id, ))