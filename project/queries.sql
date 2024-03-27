SELECT * FROM Books WHERE author_id =1;

SELECT * FROM Orders WHERE customer_id =1;

INSERT INTO Inventory (book_id , quantity) VALUES (1,100);

UPDATE Inventory SET quantity = 80 WHERE book_id = 1;

DELETE FROM Orders WHERE order_id = 1;
