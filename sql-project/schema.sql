CREATE TABLE Authors(
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL
);

CREATE TABLE Books(
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE Customers(
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(15),
    address TEXT
);

CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGEN KEY (customer_id) REFERENCES Customers(customers_id)

);

CREATE TABLE Order_Details(
    order_detail_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

CREATE TABLE Inventory(
    inventory_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES Books(book_id)

);

CREATE TABLE Reviews(
    review_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    customer_id INT NOT NULL,
    rating INT NOT NULL,
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Recommendations(
    recommendation_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    recommended_book_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY(recommended_book_id) REFERENCES Books(book_id)

);

CREATE TABLE Genres(
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(100) NOT NULL
);

CREATE TABLE Book_Genres(
    book_genre_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    genre_id INT NOT NULL,
    FOREIGN KEY (book_id) REEFERENCES Books(book_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);

CREATE TABLE Discussions(
    discussion_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    discussion_text TEXT,
    discussion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

CREATE TABLE Comments(
    comment_id SERIAL PRIMARY KEY,
    discussion_id INT,
    review_id INT,
    customer_id INT NOT NULL,
    comment_text TEXT,
    comment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (discussion_id) REFERENCES Discussions(discussion_id),
    FOREIGN KEY (review_id) REFERENCES Reviews(review_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)

);


