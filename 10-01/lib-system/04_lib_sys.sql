CREATE DATABASE IF NOT EXISTS libSys;

USE libSys; 

CREATE TABLE User(
    user_id INT PRIMARY KEY AUTO_INCREMENT, 
    first_name VARCHAR(20),
    last_name VARCHAR(20),  
    email VARCHAR(30),
    role ENUM('amdin', 'user') NOT NULL
);


CREATE TABLE Book(
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author VARCHAR(50)
);


CREATE TABLE BookCopy(
    copy_id INT PRIMARY KEY AUTO_INCREMENT, 
    book_id INT, 
    status ENUM('available', 'not_available') NOT NULL
);


CREATE TABLE Borrow(
    borrow_id INT PRIMARY KEY AUTO_INCREMENT,
    copy_id INT,
    user_id INT,
    borrow_date DATE,
    return_date DATE
); 

ALTER TABLE BookCopy
ADD CONSTRAINT book_id_fk FOREIGN KEY (book_id) REFERENCES Book(book_id);

ALTER TABLE Borrow
ADD CONSTRAINT copy_id_fk FOREIGN KEY (copy_id) REFERENCES BookCopy(copy_id),
ADD CONSTRAINT user_id_fk FOREIGN KEY (user_id) REFERENCES User(user_id);

------------------------------------

INSERT INTO User (first_name, last_name, email, role) VALUES
('Ali', 'Hassan', 'ali.hassan@example.com', 'user'),
('Sara', 'Mahmoud', 'sara.mahmoud@example.com', 'user'),
('Omar', 'Khaled', 'omar.khaled@example.com', 'user'),
('Mona', 'Youssef', 'mona.youssef@example.com', 'user'),
('Admin', 'User', 'admin@example.com', 'amdin');

INSERT INTO Book (title, author) VALUES
('Clean Code', 'Robert C. Martin'),
('The Pragmatic Programmer', 'Andrew Hunt'),
('Introduction to Algorithms', 'Thomas H. Cormen'),
('Artificial Intelligence: A Modern Approach', 'Stuart Russell'),
('Design Patterns', 'Erich Gamma');

INSERT INTO BookCopy (book_id, status) VALUES
(1, 'available'),
(1, 'not_available'),
(2, 'available'),
(3, 'not_available'),
(3, 'available'),
(4, 'available'),
(5, 'available'),
(5, 'not_available');

INSERT INTO Borrow (copy_id, user_id, borrow_date, return_date) VALUES
(2, 1, '2025-10-01', '2025-10-15'),
(4, 2, '2025-09-20', '2025-10-05'),
(8, 3, '2025-10-10', NULL),        -- not yet returned
(3, 4, '2025-10-05', '2025-10-20');


--------------------------------------

