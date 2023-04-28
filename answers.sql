-- QUESTION ONE: 
/* SELECT train_name, train_number FROM train 
	WHERE train_number IN (
		SELECT train_number FROM book WHERE (
			status='Booked' AND passenger_sn=(
				SELECT serial_number FROM passenger WHERE full_names='Art Venere'
				)
			)
		); */
		
SELECT train.train_number, train.train_name 
FROM ((passenger 
INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
INNER JOIN train ON book.train_number=train.train_number) 
WHERE book.status="Booked" AND passenger.full_names="Art Venere";



-- QUESTION TWO
/* SELECT full_names FROM passenger 
	WHERE serial_number IN (
		SELECT passenger_sn FROM book WHERE train_number IN (
			SELECT train_number FROM train WHERE availability LIKE '%Saturday%' AND status='Booked'
			)
		); */
		
SELECT DISTINCT passenger.full_names 
FROM ((passenger 
INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
INNER JOIN train ON book.train_number=train.train_number) 
WHERE book.status="Booked" AND train.availability LIKE '%Saturday%';

		

-- QUESTION THREE
SELECT passenger.full_names, passenger.address, book.ticket_type, book.status, train.train_number, train.train_name, train.source_station, train.destination_station FROM ((passenger 
INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
INNER JOIN train ON book.train_number=train.train_number) 
WHERE passenger.age>=50 AND passenger.age<=60;


-- QUESTION FOUR
SELECT train_name, (premium_seats_occupied + general_seats_occupied) 
AS count_of_passengers 
FROM train_status;


-- QUESTION FIVE
/* SELECT passenger.full_names, book.train_number, book.status, train.train_name FROM ((passenger 
INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
INNER JOIN train ON train.train_number=book.train_number) 
WHERE book.status="Booked" AND train.train_number=(SELECT train_number FROM train WHERE train_name="Golden Chariot"); */

SELECT passenger.full_names FROM ((passenger 
INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
INNER JOIN train ON train.train_number=book.train_number) 
WHERE book.status="Booked" AND train.train_number=(SELECT train_number FROM train WHERE train_name="Golden Chariot");


-- QUESTION SIX
/* BEGIN;
DELETE FROM passenger WHERE full_names=(SELECT passenger.full_names FROM passenger INNER JOIN book ON passenger.serial_number=book.passenger_sn WHERE book.status="Booked" LIMIT 1);
UPDATE book SET status="Booked" WHERE passenger_sn=(SELECT passenger_sn FROM book WHERE status="WaitL" LIMIT 1);
COMMIT; */

BEGIN;
DELETE FROM passenger WHERE full_names=(SELECT passenger.full_names FROM passenger INNER JOIN book ON passenger.serial_number=book.passenger_sn WHERE book.status="Booked" AND passenger.full_names="James Butt");
UPDATE book SET status="Booked" WHERE passenger_sn=(SELECT passenger_sn FROM book WHERE status="WaitL" LIMIT 1);
SELECT DISTINCT passenger.full_names FROM passenger INNER JOIN book ON passenger.serial_number=book.passenger_sn AND book.status="Booked";
COMMIT;

