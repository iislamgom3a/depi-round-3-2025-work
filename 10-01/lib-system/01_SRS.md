## **Library Management System**

### **1. Introduction**

#### **1.1 Purpose**

This document describes the requirements for a **Library Management System (LMS)**.
The system helps manage books in a library — including adding, searching, borrowing, and returning books.

#### **1.2 Scope**

The system will allow:

* **Admins** to add, edit, or remove books and copies.
* **Members** to search for, borrow, and return books.

It will keep track of all book copies and who borrowed each one.

---

### **2. Users and Roles**

| Role       | Description                                |
| ---------- | ------------------------------------------ |
| **Admin**  | Can add, remove, or edit books and copies. |
| **Member** | Can search, borrow, and return books.      |

---

### **3. Main Features**

1. **Add Books** – Admins can add new books with details like title, author, and ISBN.
2. **Remove Books** – Admins can delete books or book copies.
3. **Search Books** – Users can search for books by title, author.
4. **Borrow Books** – Members can borrow available book copies.
5. **Return Books** – Members can return borrowed books.
6. **List Books** – The system shows all books with their availability status.

---

### **4. Data Model**

#### **Entities**

| Entity       | Attributes                                                 | Description                                                |
| ------------ | ---------------------------------------------------------- | ---------------------------------------------------------- |
| **User**     | `UserID`, `FirstName`, `LastName`, `Email`, `Role`                          | Represents a library user (Admin or Member).               |
| **Book**     | `BookID`, `Title`, `Author`                                | Represents a book title.                                   |
| **BookCopy** | `CopyID`, `BookID`, `Status`                               | Represents a single physical book (Available or Borrowed). |
| **Borrow**   | `BorrowID`, `CopyID`, `UserID`, `BorrowDate`, `ReturnDate` | Tracks each borrowing action.                              |

#### **Relationships**

* One **Book** → Many **BookCopies**
* One **User** → Many **Borrows**
* One **Borrow** → One **BookCopy**

---

### **5. System Rules**

* Only Admins can add or remove books.
* A book can only be borrowed if a copy is **Available**.
* When a book is borrowed:

  * Its status changes to **Borrowed**.
  * A new **Borrow** record is created.
* When a book is returned:

  * Its status changes to **Available**.
  * The **ReturnDate** is updated in the borrow record.

---
