# Bookstore Management API with Python, Flask, Docker, and Postgres

This project aims to develop a RESTful API for managing a bookstore inventory using Python, Flask, Docker, and PostgreSQL. The API provides endpoints for CRUD operations on books, along with search functionality and API documentation using Swagger.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Flask
- **Database:** PostgreSQL
- **Containerization:** Docker

## Features

### Book Entity

- **Attributes:** 
  - id (integer, primary key)
  - title (string)
  - author (string)
  - ISBN (string, unique)
  - price (float)

### API Endpoints

- **GET /books:** Retrieves a list of all books.
- **GET /books/{id}:** Retrieves a specific book by its ID.
- **GET /books/search?title={title}:** Searches for books by title (case-insensitive).
- **POST /books:** Adds a new book to the inventory.
- **PUT /books/{id}:** Updates an existing book.
- **DELETE /books/{id}:** Deletes a book from the inventory.

### Documentation

- Integration of Swagger for API documentation with clear descriptions and examples for each endpoint.

## Project Structure

- **main.py:** Entry point for the application.
- **models.py:** Defines the Book model with its attributes.
- **database.py:** Handles database connection and management using SQLAlchemy.
- **repository.py:** Defines the BookRepository class with methods for CRUD operations on the Book entity.
- **service.py:** Encapsulates business logic and interacts with the repository.
- **api.py:** Defines the Flask application with endpoints for managing books.

## Development Steps

1. **Setup Environment:** Install Python, Flask, Docker, and PostgreSQL. Configure database connection details in database.py.
2. **Define Models:** Create the Book model in models.py.
3. **Database Access:** Utilize SQLAlchemy for database interaction in database.py.
4. **Repository Layer:** Develop the BookRepository class for CRUD operations in repository.py.
5. **Service Layer:** Create the BookService class in service.py to handle business logic.
6. **API Development:** Define Flask application in api.py. Implement API endpoints and link them with service logic.
7. **Documentation:** Integrate Swagger for API documentation with detailed descriptions and examples.
8. **Dockerization:** Create a Dockerfile for building and containerizing the application.
9. **Testing:** Implement unit and integration tests for API and service layers.

## Deliverables

- Functional Python code for the API with specified features and documentation.
- Dockerfile for containerizing the application.
- README.md with setup, running, and testing instructions.
