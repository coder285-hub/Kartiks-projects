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
d


