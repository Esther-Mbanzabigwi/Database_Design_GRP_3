
# 📚 Database Assignment 📚

## 📝 Overview
This project involves creating and managing a database using both SQL and NoSQL approaches, developing CRUD API endpoints, and fetching data for predictions using an e-commerce shipping data model.

## 🏆 Tasks and Contributions

### Task 1: Database Schema Design (✅ Completed by Esther)
- Designed a normalized database schema using tools like Lucidchart/Draw.io.
- Defined tables and relationships for the database.

### Task 2: SQL and NoSQL Implementation (✅ Completed by Caroline)
- Created a relational database schema with at least 3 tables using a chosen RDBMS (e.g., MySQL/PostgreSQL/SQLite).
- Implemented the same schema using MongoDB collections.
- Ensured the inclusion of primary and foreign keys for relational integrity.

### Task 3: CRUD API Creation (✅ Completed by Emmanuel)
- Used FastAPI to create API endpoints for performing:
  - Create (POST)
  - Read (GET)
  - Update (PUT)
  - Delete (DELETE)

### Task 4: Data Fetching and Prediction Script (✅ Completed by Charite)
- Developed a script to fetch the latest entry from the API.
- Prepared the input data for prediction using a pre-trained e-commerce shipping model.
- Integrated data scaling and prediction logic.

## 🔧 Technology Stack
- **Database**: MySQL/PostgreSQL, MongoDB
- **Framework**: FastAPI
- **Programming Language**: Python
- **Model**: Pre-trained e-commerce shipping data model

## 🚀 How to Run the Project
1. **Set up the database schema**: Import the provided SQL and MongoDB schema files.
2. **Run the FastAPI server**: Use `uvicorn main:app --reload` to start the API server.
3. **Run the fetch and predict script**: Execute the Python script for fetching and processing the data.

## 📊 Prediction Model
- **Model**: Pre-trained e-commerce shipping data model.
- **Data Preprocessing**: Includes data scaling using a MinMaxScaler.
