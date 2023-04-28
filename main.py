import sqlite3
from read_datasets import load_data

conn = sqlite3.connect('rrs.db')
conn.execute("PRAGMA foreign_keys=ON")  # Enabling FOREIGN KEYS
cur = conn.cursor()

# print(conn.execute("pragma foreign_keys;").fetchall())


def create_passenger_table():
    cur.execute("DROP TABLE IF EXISTS passenger")
    # cur.execute("DELETE FROM passenger")
    cur.execute("""
    CREATE TABLE passenger (
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        full_names TEXT NOT NULL,
        address TEXT,
        city TEXT,
        county TEXT,
        phone_number TEXT,
        serial_number INTEGER NOT NULL UNIQUE PRIMARY KEY,
        birth_date TEXT NOT NULL,
        age INTEGER
    )
    """)

    # Loading the Passenger data from Passenger-1.csv
    for _, row in load_data("passenger").iterrows():
        cur.execute("""
            INSERT INTO passenger VAlUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, row)
        # print(row)
        # break


def create_train_table():
    cur.execute("DROP TABLE IF EXISTS train")
    cur.execute("""
    CREATE TABLE train (
        train_number INTEGER NOT NULL,
        train_name TEXT NOT NULL,
        premium_fair INTEGER NOT NULL,
        general_fair INTEGER NOT NULL,
        source_station TEXT,
        destination_station TEXT,
        availability TEXT
    )
    """)

    # Loading the Train data from Train.csv
    for _, row in load_data("train").iterrows():
        cur.execute("""
            INSERT INTO train VAlUES(?, ?, ?, ?, ?, ?, ?)
        """, row)
        # print(row)
        # break


def create_book_table():
    cur.execute("DROP TABLE IF EXISTS book")
    cur.execute("""
    CREATE TABLE book (
        passenger_sn INTEGER NOT NULL,
        train_number INTEGER NOT NULL,
        ticket_type TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (passenger_sn)
        REFERENCES passenger (serial_number) 
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )
    """)

    # Loading the Book data from booked-1.csv
    for _, row in load_data("book").iterrows():
        cur.execute("""
            INSERT INTO book VAlUES(?, ?, ?, ?)
        """, row)
        # print(row)
        # break


def create_train_status_table():
    cur.execute("DROP TABLE IF EXISTS train_status")
    cur.execute("""
    CREATE TABLE train_status (
        train_date TEXT NOT NULL,
        train_name TEXT NOT NULL,
        premium_seats_available INTEGER NOT NULL,
        general_seats_available INTEGER NOT NULL,
        premium_seats_occupied INTEGER NOT NULL,
        general_seats_occupied INTEGER NOT NULL
    )
    """)

    # Loading the TrainStatus data from Train_status.csv
    for _, row in load_data("train_status").iterrows():
        cur.execute("""
            INSERT INTO train_status VAlUES(?, ?, ?, ?, ?, ?)
        """, row)
        # print(row)
        # break


create_passenger_table()
create_train_table()
create_book_table()
create_train_status_table()

conn.commit()
conn.close()
