import sqlite3

conn = sqlite3.connect('rrs.db')
conn.execute("PRAGMA foreign_keys=ON")  # Enabling FOREIGN KEYS
cur = conn.cursor()


# QUESTION 1
def get_train_from_full_names(full_names):
    full_names = full_names.title()
    sql_query = f"""
        SELECT train.train_number, train.train_name 
        FROM ((passenger 
        INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
        INNER JOIN train ON book.train_number=train.train_number) 
        WHERE book.status="Booked" AND passenger.full_names='{full_names}';
    """
    return cur.execute(sql_query).fetchall()


def get_passengers_from_day(day):
    day = day.title()
    sql_query = f"""
        SELECT DISTINCT passenger.full_names 
        FROM ((passenger 
        INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
        INNER JOIN train ON book.train_number=train.train_number) 
        WHERE book.status="Booked" AND train.availability LIKE '%{day}%';
    """
    return cur.execute(sql_query).fetchall()


def get_train_info_and_passenger_info_from_age(input_age):
    if not 50 <= input_age <= 60:
        return []

    sql_query = f"""
        SELECT passenger.full_names, passenger.address, book.ticket_type, book.status, train.train_number, train.train_name, train.source_station, train.destination_station FROM ((passenger 
        INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
        INNER JOIN train ON book.train_number=train.train_number) 
        WHERE passenger.age>=50 AND passenger.age<=60;
    """
    return cur.execute(sql_query).fetchall()


def get_train_status():
    sql_query = f"""
        SELECT train_name, (premium_seats_occupied + general_seats_occupied) 
        AS count_of_passengers 
        FROM train_status;
    """
    return cur.execute(sql_query).fetchall()


def get_passengers_from_train_name(train_name):
    train_name = train_name.title()
    sql_query = f"""
        SELECT passenger.full_names FROM ((passenger 
        INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
        INNER JOIN train ON train.train_number=book.train_number) 
        WHERE book.status="Booked" AND train.train_number=(SELECT train_number FROM train WHERE train_name='{train_name}');
    """
    return cur.execute(sql_query).fetchall()


def get_passengers_with_confirmed_tickets():
    booked_passengers_query = f"""
        SELECT DISTINCT passenger.full_names FROM passenger INNER JOIN book ON passenger.serial_number=book.passenger_sn AND book.status="Booked";
    """
    return cur.execute(booked_passengers_query).fetchall()


def cancel_ticket(passenger_name):
    passenger_name = passenger_name.title()
    sql_query = f"""
        BEGIN;
        DELETE FROM passenger WHERE full_names=(SELECT passenger.full_names FROM passenger INNER JOIN book ON passenger.serial_number=book.passenger_sn WHERE book.status="Booked" AND passenger.full_names='{passenger_name}');
        UPDATE book SET status="Booked" WHERE passenger_sn=(SELECT passenger_sn FROM book WHERE status="WaitL" LIMIT 1);
        COMMIT;
    """
    cur.executescript(sql_query)


# print(get_train_from_full_names("Art Venere"))
# print(get_passengers_from_day("Saturday"))
# print(get_train_info_and_passenger_info_from_age(50))
# print(get_train_status())
# print(get_passengers_from_train_name("Golden Chariot"))
# print(cancel_ticket("James Butt"))
print(get_passengers_with_confirmed_tickets())

conn.commit()
# conn.close()
