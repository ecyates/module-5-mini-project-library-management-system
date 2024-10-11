CREATE DATABASE library_management_db;

USE library_management_db;

CREATE TABLE Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
	author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(id)
);

CREATE TABLE Authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE BorrowedBooks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (book_id) REFERENCES Books(id)
);

CREATE TABLE Genres (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

ALTER TABLE Books 
ADD genre_id INT, 
ADD FOREIGN KEY (genre_id) REFERENCES Genres(id);

INSERT INTO Authors (name, biography)
VALUES 
("Harper Lee", "Harper Lee was an American novelist best known for her 1960 novel To Kill a Mockingbird, which won the Pulitzer Prize."),
("George Orwell", "George Orwell was an English novelist and essayist, journalist and critic, best known for his dystopian novel 1984 and the allegorical novella Animal Farm."),
("F. Scott Fitzgerald", "F. Scott Fitzgerald was an American novelist and short-story writer, widely regarded as one of the greatest American writers of the 20th century."),
("Jane Austen", "Jane Austen was an English novelist known for her six major novels which critique and comment upon the British landed gentry at the end of the 18th century."),
("Toni Morrison", "Toni Morrison was an American novelist, essayist, editor, and professor, known for her powerful novels exploring African-American culture and history."),
("J.K. Rowling", "J.K. Rowling is a British author, best known for the Harry Potter series, which has become one of the best-selling book series in history."),
("Ray Bradbury", "Ray Bradbury was an American author and screenwriter, known primarily for his works in the science fiction and fantasy genres."),
("Herman Melville", "Herman Melville was an American novelist, short-story writer, and poet of the American Renaissance period, best known for his novel Moby-Dick."), 
("Khaled Hosseini", "Khaled Hosseini is an Afghan-American novelist and physician, best known for his novels The Kite Runner and A Thousand Splendid Suns."),
("J.D. Salinger", "J.D. Salinger was an American writer best known for his novel The Catcher in the Rye, which became an icon for teenage rebellion."),
("Junot Díaz", "Junot Díaz is a Dominican-American writer, known for his short stories and his novel The Brief Wondrous Life of Oscar Wao, which won the 2008 Pulitzer Prize for Fiction."),
("Aldous Huxley", "Aldous Huxley was an English writer and philosopher, known for his novels including Brave New World and his essays exploring topics of interest."),
("Yann Martel", "Yann Martel is a Canadian author best known for his Man Booker Prize-winning novel Life of Pi."), 
("Donna Tartt", "Donna Tartt is an American author and essayist, known for her novels The Secret History, The Little Friend, and The Goldfinch, which won the Pulitzer Prize for Fiction."),
("John Steinbeck", "John Steinbeck was an American author and Nobel Prize winner, known for his novels about the working class and themes of social justice."), 
("Fyodor Dostoevsky", "Fyodor Dostoevsky was a Russian novelist and philosopher whose works explore human psychology in the troubled political, social, and spiritual atmosphere of 19th-century Russia."),
("Mary Shelley", "Mary Shelley was an English novelist best known for her Gothic novel Frankenstein, considered one of the earliest examples of science fiction."),
("Paulo Coelho", "Paulo Coelho is a Brazilian lyricist and novelist, best known for his novel The Alchemist, which is one of the best-selling books in history."),
("Yuval Noah Harari", "Yuval Noah Harari is an Israeli historian and professor, known for his books Sapiens, Homo Deus, and 21 Lessons for the 21st Century."),
("Colson Whitehead", "Colson Whitehead is an American novelist, known for his works of speculative fiction and literary fiction, including the Pulitzer Prize-winning The Underground Railroad."),
("Gillian Flynn", "Gillian Flynn is an American author, screenwriter, and critic, known for her novels Sharp Objects, Dark Places, and Gone Girl."),
("Jeffrey Eugenides", "Jeffrey Eugenides is an American novelist known for his books The Virgin Suicides, Middlesex, and The Marriage Plot."),
("Stieg Larsson", "Stieg Larsson was a Swedish journalist and writer, best known for his posthumously published Millennium trilogy, beginning with The Girl with the Dragon Tattoo."),
("Neil Gaiman", "Neil Gaiman is an English author of short fiction, novels, comic books, graphic novels, nonfiction, and films, known for his works of speculative fiction."),
("Margaret Atwood", "Margaret Atwood is a Canadian poet, novelist, literary critic, and essayist, known for her works of fiction, including The Handmaid's Tale.");

INSERT INTO Genres (name)
VALUES
("Fiction"),
("Non-fiction"), 
("Mystery"), 
("Fantasy"), 
("Sci-Fi"),
("Classic Fiction"),
("Dystopian Fiction"),
("Historical Fiction"), 
("Literary Fiction"),
("Philosophical Fiction"),
("Contemporary Fiction"),
("Adventure Fiction"), 
("Thriller"),
("Gothic Fiction");


INSERT INTO Books (isbn, title, author_id, publication_date, genre_id, availability)
VALUES
("9780061120084", "To Kill a Mockingbird", 1, "1960-07-11", 1, 1),
("9780451524935", "1984", 2, "1949-06-08", 7, 0),
("9780743273565", "The Great Gatsby", 3, "1925-04-10", 6, 1),
("9780679783268", "Pride and Prejudice", 4, "1813-01-28", 6, 1),
("9780307277671", "Beloved", 5, "1987-09-16", 8, 0),
("9780439139601", "Harry Potter and the Prisoner of Azkaban", 6, "1999-07-08", 4, 1),
("9781451673319", "Fahrenheit 451", 7, "1953-10-19", 7, 1),
("9780142437209", "Moby-Dick", 8, "1851-10-18", 6, 1),
("9781594480003", "The Kite Runner", 9, "2003-05-29", 8, 1),
("9780316769488", "The Catcher in the Rye", 10, "1951-07-16", 1, 0),
("9780374533557", "The Brief Wondrous Life of Oscar Wao", 11, "2007-09-04", 11, 1),
("9780060850524", "Brave New World", 12, "1932-01-01", 7, 1),
("9780452284235", "Life of Pi", 13, "2001-09-11", 12, 1),
("9780812981605", "The Goldfinch", 14, "2013-09-23", 9, 1),
("9780140177394", "Of Mice and Men", 15, "1937-02-06", 6, 1),
("9780140449266", "The Brothers Karamazov", 16, "1880-11-01", 10, 1),
("9780142437339", "Frankenstein", 17, "1818-01-01", 14, 1),
("9780060853969", "The Alchemist", 18, "1988-05-01", 10, 1),
("9780812974027", "Sapiens: A Brief History of Humankind", 19, "2011-09-04", 2, 1),
("9780802123701", "The Underground Railroad", 20, "2016-08-02", 8, 1),
("9780385534246", "Gone Girl", 21, "2012-06-05", 13, 1),
("9780375706677", "Middlesex", 22, "2002-09-04", 9, 1),
("9780307473479", "The Girl with the Dragon Tattoo", 23, "2005-09-16", 3, 1),
("9780060838676", "American Gods", 24, "2001-06-19", 4, 1),
("9780062315007", "The Handmaid's Tale", 25, "1985-09-01", 7, 1);

SELECT b.title as Title, a.name as Author, g.name as Genre
FROM Books b, Authors a, Genres g
WHERE b.author_id = a.id AND b.genre_id = g.id
ORDER BY b.title ASC;

INSERT INTO Users (name, library_id)
VALUES
("Emily Johnson", "LIB123456"),
("Abigail Taylor", "LIB789012"),
("Olivia Brown", "LIB345678"),
("James Williams", "LIB901234"),
("Sophia Martinez", "LIB567890"),
("Liam Anderson", "LIB123789"),
("Isabella Thompson", "LIB456123"),
("Noah Garcia", "LIB789345"),
("Mia Hernandez", "LIB012345"),
("Benjamin Wilson", "LIB678901"),
("Charlotte Davis", "LIB345012"),
("Alexander Rodriguez", "LIB901678"),
("Amelia Martinez", "LIB234567"),
("Lucas White", "LIB890123"),
("Harper Moore", "LIB123890"),
("Ethan Lee", "LIB456789"),
("Logan Thomas", "LIB012678"),
("Ava Jackson", "LIB901345"),
("William Martin", "LIB345901"),
("Mason Thompson", "LIB678345"),
("Elijah Martinez", "LIB234890"),
("Sophia White", "LIB567012"),
("Emily Garcia", "LIB890456"),
("Oliver Martinez", "LIB123234"),
("Avery Robinson", "LIB456345"),
("Sofia Lee", "LIB789567");

SELECT * FROM Authors;

INSERT INTO BorrowedBooks (user_id, book_id, borrow_date, return_date)
VALUES
(11, 5, "2024-10-09", "2024-10-23"),
(11, 10, "2024-10-08", "2024-10-22"),
(23, 2, "2024-10-07", "2024-10-21");

SELECT b.title as Title, u.name as UserName, bb.borrow_date as DateBorrowed, bb.return_date as DueDate
FROM Books b, Users u, BorrowedBooks bb
WHERE b.id = bb.book_id AND u.id = bb.user_id
ORDER BY bb.return_date ASC;

SELECT * FROM Books;
SELECT * FROM Users;
SELECT * FROM Authors;
SELECT * FROM Genres;
SELECT * FROM BorrowedBooks;