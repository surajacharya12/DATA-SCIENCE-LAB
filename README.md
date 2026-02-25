# DATA-SCIENCE-LAB

---

## 📘Lab Report – Lab 1
**Title:** Python Essentials and Data Structures

**Objective:**
The objective of this lab is to understand basic Python syntax, data types (lists, dictionaries), functions, and control flow to build a solid foundation for data science.

**Data Analysis Key Findings:**
1. **Data Structures:**
   - Demonstrated list concatenation and dictionary operations.
   - Used `for` loops to iterate through dictionary items and strings.
2. **Functional Programming:**
   - Implemented functions with type hinting (`List`, `Dict`, `Optional`) for better code documentation.
   - Utilized `lambda` functions and `map()` for concise data processing.
3. **Looping and Sequences:**
   - Explored `range()`, `while` loops, and `for` loops for generating numerical sequences.
   - Performed mathematical operations like calculating the area of a circle using the `math` module.

---

## 📘Lab Report – Lab 2
**Title:** Iterators, Generators, and Decorators in Python

**Objective:**
The objective of this lab is to master advanced Python features that enable writing efficient, clean, and reusable code, specifically focusing on memory management and high-order functions.

**Data Analysis Key Findings:**
1. **Iterators and Protocol:**
   - Understanding the `__iter__()` and `__next__()` methods.
   - Analyzing how `for` loops internally leverage iterators.
2. **Generators:**
   - Creating memory-efficient iterators using the `yield` keyword.
   - Generating values on-the-fly to reduce memory footprint.
3. **Decorators:**
   - Implementing function wrappers to extend behavior without modifying original logic.
   - Practical application in logging and status tracking.

---

## 📘Lab Report – Lab 3
**Title:** OOP Concepts and File Handling in Python

**Objective:**
The objective of this lab is to understand and demonstrate key Object-Oriented Programming (OOP) concepts such as encapsulation and inheritance, and to learn how to handle different file formats using Python.

**Data Analysis Key Findings:**
1. **Object-Oriented Programming (OOP) Concepts:**
   - **Encapsulation:** Demonstrated using private attributes and public getter/setter methods.
   - **Inheritance:** Extended the Employee class to a Professor class, adding specialized subject attributes.
2. **File Handling Techniques:**
   - **CSV/Excel:** Reading and writing data using built-in modules and Pandas.
   - **JSON:** Handling document-style data with proper indentation for readability.
   - **Plain Text:** Managing raw text data with newline structures.

---

## 📘Lab Report – Lab 4
**Title:** Database Management (SQL vs NoSQL)

**Objective:**
The objective of this lab is to explore and implement CRUD (Create, Read, Update, Delete) operations using both relational (SQLite) and non-relational (MongoDB) databases.

**Data Analysis Key Findings:**
1. **Relational Database (SQLite):**
   - Established connections and created tables with diverse data types.
   - Performed standard SQL queries for record management.
2. **Object Relational Mapping (SQLAlchemy):**
   - Defined ORM models to interact with SQL databases using Python objects.
   - Managed sessions and executed queries without writing raw SQL.
3. **Non-Relational Database (MongoDB):**
   - Connected to cloud-based MongoDB clusters using `pymongo`.
   - Handled flexible document storage and complex queries (e.g., upserts).
4. **Comparison:** 
   - Highlighted the transition from rigid table schemas in SQL to flexible document schemas in NoSQL.
   - Explored the advantages of serverless SQLite for local dev versus scalable NoSQL for web apps.

---
---

## 📘Lab Report – Lab 5
**Title:** Web Scraping, REST and SOAP API Interaction

**Objective:**
The objective of this lab is to extract data from web pages using BeautifulSoup and to interact with external web services via REST (GET/POST) and SOAP APIs.

**Data Analysis Key Findings:**
1. **Web Scraping (BeautifulSoup):**
   - Extracted structured data from Wikipedia, including infobox metadata and quote lists.
   - Utilized both tag-based searching (`find_all`) and CSS selectors (`.select`) for targeted extraction.
2. **REST API Interaction:**
   - Performed GET requests to fetch and parse JSON data from remote endpoints.
   - Demonstrated POST requests to send structured data to a server and verify responses.
3. **SOAP API Interaction:**
   - Utilized the `zeep` library to connect to WSDL-based web services.
   - Executed remote procedure calls (RPC) to perform operations on an external service.

---

## 📘Lab Report – Lab 6
**Title:** Advanced Data Preprocessing and Pre-ML Workflows

**Objective:**
The objective of this chapter is to master complex data reshaping, cleaning, and memory optimization techniques to prepare high-quality datasets for machine learning.

**Data Analysis Key Findings:**
1. **Data Reshaping (Pivot & Melt):**
   - Transformed raw transactional data into multi-dimensional summaries using pivot tables.
   - Restructured wide-format reports back into long-format for analytical flexibility.
2. **Data Cleaning & Imputation:**
   - Identified missing data metrics (counts/percentages) across features.
   - Implemented Median, Mean, and Forward-Fill imputation strategies for numerical and time-series data.
3. **Feature Engineering & Encoding:**
   - Applied One-Hot and Ordinal encoding to transform categorical data for ML consumption.
   - Implemented Feature Scaling (Normalization and Standardization) to balance numerical ranges.
4. **Database Normalization & Reconstruction:**
   - Simulated relational normalization by splitting flat files into distinct entity tables (Customers, Products, Orders).
   - Reconstructed datasets using complex multi-table joins.
5. **Optimization:**
   - Developed memory optimization scripts to downcast datatypes and utilize categorical storage, significantly reducing RAM usage for large datasets.

---
