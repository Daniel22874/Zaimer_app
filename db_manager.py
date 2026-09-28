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