from mysql.connector import connect


class DB:
    mysqldb = connect(
        host="127.1.1.0",
        user="root",
        password="P@ssw0rd",
        buffered=True,
        database="libSys",
    )

    def create_connection(self):
        cursor = self.mysqldb.cursor()
        return cursor

    def excute_featch_all(self, qre: str, params: tuple = tuple()) -> list:
        cursor = self.create_connection()
        if params:
            cursor.execute(qre, params)
        else:
            cursor.execute(qre)
        return cursor.fetchall()


class App:
    def __init__(self):
        self.db = DB()

    def list_books(self):
        rows = self.db.excute_featch_all("SELECT id, title, author, year FROM books")
        print("------" * 10)
        for r in rows:
            print(r)
        print("------" * 10)

    def add_book(self, title, author, year):
        cursor = self.db.create_connection()
        cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)",
            (title, author, year),
        )
        self.db.mysqldb.commit()
        print("------" * 10)
        print(
            self.db.excute_featch_all(
                "SELECT id, title FROM books WHERE title = %s", (title,)
            )
        )
        print("------" * 10)

    def update_book_year(self, title, new_year):
        cursor = self.db.create_connection()
        cursor.execute("UPDATE books SET year = %s WHERE title = %s", (new_year, title))
        self.db.mysqldb.commit()
        print("------" * 10)
        print(
            self.db.excute_featch_all(
                "SELECT id, title, year FROM books WHERE title = %s", (title,)
            )
        )
        print("------" * 10)

    def delete_book(self, title):
        cursor = self.db.create_connection()
        cursor.execute("DELETE FROM books WHERE title = %s", (title,))
        self.db.mysqldb.commit()
        print("------" * 10)
        print(("deleted", title))
        print("------" * 10)


if __name__ == "__main__":
    app = App()
    db = app.db
    cursor = db.create_connection()
    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), year INT)"
        )
        db.mysqldb.commit()
        cursor.execute("DELETE FROM books")
        db.mysqldb.commit()
        app.add_book("1984", "George Orwell", 1949)
        app.add_book("Brave New World", "Aldous Huxley", 1932)
        app.list_books()
        app.update_book_year("1984", 1950)
        app.list_books()
        app.delete_book("Brave New World")
        app.list_books()
        cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)",
            ("Temp Book", "Temp Author", 2025),
        )
        db.mysqldb.rollback()
        print("------" * 10)
        print(
            db.excute_featch_all(
                "SELECT title FROM books WHERE title = %s", ("Temp Book",)
            )
        )
        print("------" * 10)
    except Exception as e:
        db.mysqldb.rollback()
        print("Error:", e)
    finally:
        try:
            cursor.close()
        except Exception:
            pass
        try:
            db.mysqldb.close()
        except Exception:
            pass
