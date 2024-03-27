### FINAL PROJECT: ONLINE BOOKSTORE AND COMMUNITY PLATFORM DATABASE

## PURPOSE
The goal of this comprehensive database is to establish a large online platform that not only functions as a bookshop but also promotes a community around books. It seeks to give users with a seamless experience for discovering, purchasing, discussing, and reviewing books.

## SCOPE
In addition to the functionality of an online shop, this database will include user reviews, suggestions, author interactions, and community forums. It seeks to meet the different demands of book lovers, from casual readers to devoted bibliophiles.

## ENTITTIES
* Books: which represent specific items offered in the shop.

* Authors: Contains information on book writers.

* Customers: Stores information on customers who engage with the site.

* Orders: Records individual orders placed by consumers.

* Inventory: Oversees the stock of books available for sale.

* Reviews: A collection of user-generated book reviews.

* Recommendations: Keeps individualized book suggestions for users.

* Genres: Groups books into categories for better browsing.

* Discussions: Hosts community conversations about different book-related subjects.

* Comments: Allows users to leave feedback on conversations and reviews.

## RELATIONSHIPS

* Books - Authors : Many-to-Many connection as a book may have several writers and one author can create multiple books.

* Books - Inventory: A one-to-one link exists since each book is associated with specific inventory information.

* Customers - Orders: A one-to-many connection exists because a customer can place several orders, but each order belongs to a single customer.

* Orders - Inventory: A many-to-many connection exists because each order can contain several books, and a book can be included in numerous orders.

* Books - Reviews: One-to-Many connection, as a book can have several reviews, but each review is exclusive to one book.

* Customers - Reviews: One-to-Many connection in which a customer can post several reviews, yet each review is authored by a single customer.

* Customers - Recommendations: A one-to-many connection in which a consumer may get several suggestions, but each recommendation is specific to one customer.

* Genres - Books: A many-to-many link exists because a book can belong to numerous genres, and a genre can contain multiple books.

* Books - Discussion: A one-to-many relationship occurs when a book is discussed in several venues, but each conversation is limited to one book.

* Discussions - Comments: A one-to-many relationship exists because a discussion might contain several comments, but each remark is specific to one discussion or review.

* Orders - Order Detial: A one-to-many relationship exists since each order information in the Order_Details table corresponds to a single order in the Orders table. This is because each entry in Order_Details corresponds to a single item ordered within an order. Each order in the Orders database can include several order details, which indicate that various products are included in the same order.

* Orders - Books : A one-to-many relationships since each order information in the Order_Details table corresponds to exactly one book in the Books table. This represents the precise book that was ordered as part of the order details.If a book has been ordered more than once, numerous order details can be used to refer to it.

* Book_Genres - Books : A one-to-many relationships since each row in the Book_Genres database corresponds to a single genre connected with a given book. Each book in the Books table can have several genres, and each genre can be linked to many books.

* Book_ Genres - Genres : A one- to- many relationship since each entry in the Book_Genres database relates to a certain genre in the Genres table, showing which genre is linked with the book.Each genre in the Genres table can be referred by several entries in the Book_Genres table since multiple novels might fall into the same genre.









