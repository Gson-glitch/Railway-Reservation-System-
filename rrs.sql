-- QUESTION ONE
BEGIN;
	SET @full_names = 'Art Venere';
	SELECT train.train_number, train.train_name 
	FROM ((passenger 
	INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
	INNER JOIN train ON book.train_number=train.train_number) 
	WHERE book.status="Booked" AND passenger.full_names=@full_names;
COMMIT;


-- QUESTION TWO
BEGIN;
	SET @day='Saturday';
	SELECT DISTINCT passenger.full_names 
	FROM ((passenger 
	INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
	INNER JOIN train ON book.train_number=train.train_number) 
	WHERE book.status="Booked" AND train.availability LIKE (SELECT CONCAT('%',@day,'%'));
COMMIT;


-- QUESTION THREE
-- SELECT TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) AS age FROM passenger;
BEGIN;
	SELECT passenger.full_names, passenger.address, book.ticket_type, book.status, train.train_number, train.train_name, train.source_station, train.destination_station FROM ((passenger 
	INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
	INNER JOIN train ON book.train_number=train.train_number) 
	WHERE passenger.age>=50 AND passenger.age<=60;
END;


-- QUESTION FOUR
SELECT train_name, (premium_seats_occupied + general_seats_occupied) 
AS count_of_passengers 
FROM train_status;


--- QUESTION FIVE
BEGIN;
	SET @train_name='Golden Chariot';
	SELECT passenger.full_names FROM ((passenger 
	INNER JOIN book ON passenger.serial_number=book.passenger_sn) 
	INNER JOIN train ON train.train_number=book.train_number) 
	WHERE book.status="Booked" AND train.train_number=(SELECT train_number FROM train WHERE train_name=@train_name);
END;


-- QUESTION SIX
BEGIN;
	SET @full_names = 'James Butt';
	DELETE FROM passenger WHERE full_names=(SELECT passenger.full_names FROM passenger INNER JOIN book ON passenger.serial_number=book.passenger_sn WHERE book.status="Booked" AND passenger.full_names=@full_names);
	UPDATE book SET status="Booked" WHERE passenger_sn=(SELECT passenger_sn FROM book WHERE status="WaitL" LIMIT 1);
	SELECT DISTINCT passenger.full_names FROM passenger INNER JOIN book ON passenger.serial_number=book.passenger_sn AND book.status="Booked";
COMMIT;
