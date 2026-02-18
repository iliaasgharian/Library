# book_database


---

## 📁 Files

| Files | |
|------|-------------|
| model.py : All classes are in this file. |
| LibraryDataAdapter.py : All the work we do in SQL is in this file. |
| main.py : All requests are stated in this file. |
| Library.sql : SQL script to create the database. |
| NewLibrary.db : SQLite database file that saves data.|



---

### ➕ Add / ➖ Delete Objects

- **Add Author**  
  ``` 
  insert author [name] [birthdate] [nationality]
  ```  
- **Delete Author**  
  ```
  delete author [author_id]
  ```  

- **Add Publisher**  
  ```
  insert publisher [name] [address] [website]
  ```  
- **Delete Publisher**  
  ```
  delete publisher [publisher_id]
  ```  

- **Add Language**  
  ```
  insert language [name]
  ```  
- **Delete Language**  
  ```
  delete language [language_id]
  ```  

- **Add Cover Designer**  
  ```
  insert designer [name] [birthdate] [nationality]
  ```  
- **Delete Cover Designer**  
  ```
  delete designer [designer_id]
  ```  

- **Add Translator**  
  ```
  insert translator [name] [language]
  ```  
- **Delete Translator**  
  ```
  delete translator [translator_id]
  ```  

- **Add Resource**  
  ```
  insert resource [name]
  ```  
- **Delete Resource**  
  ```
  delete resource [resource_id]
  ```  

- **Add Category**  
  ```
  insert category [name]
  ```  
- **Delete Category**  
  ```
  delete category [category_id]
  ```  
- **Add Book**  
  ``` 
  insert book [title] [product_code] [categories] [age_group] [release_date] [authors] [price] [langugaes] [publisher_id] [designers] [translators] [resources]
  ```  
---


##  How to work

1. Run the main script:  
   ```bash
   python main.py
   ```  
2. Enter a command, e.g.:  
   ```
   insert author Jim 2000-01-01 German
   ```   
   ```
   insert book nlbook 1050 [1] Adlut 2000-10-25 [1] 75 [1,2] 3 [1] [2] [4]
   ```  
   ```
   delete book 5
   ```
   ```
   delete author 2
   ```  

---

## ⚙️ Underlying Technology

- Uses Python and the built-in `sqlite3` module to manage a lightweight SQL database. :contentReference[oaicite:0]{index=0}  
- The adapter handles database connection, query execution, insertion, deletion and commit — ensuring persistent storage.  
- `Library.sql` can be used to (re)create database schema from scratch if needed.  

---

## 👍 Why This Project

This project serves as a simple but extensible example of a relational data-based library system. The system can store rich metadata: multiple authors per book, multiple languages, categories, cover designers, translators, sources, publishers, and more - allowing for complex modeling of a book library beyond simple title/author pairs.  

---
  
thanks for reading
