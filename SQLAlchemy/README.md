## SQLAlchemy ORM — recommended

Best starting point

Define database tables as Python classes and relationships with relationship(). It makes working with related records more convenient.

## SQLAlchemy Core

Define tables using MetaData, Table, and Column, then execute SQL expressions through connections. It's useful for direct SQL-oriented work, bulk operations, and queries where you want explicit control.

Recommended production stack
Component Purpose
PostgreSQL Database
SQLAlchemy 2.0 ORM Models, relationships, queries
Psycopg 3 PostgreSQL driver
Alembic Version-controlled database migrations
Session Database operations and transaction management

## Three ways to define tables in SQLAlchemy

| Feature            | Core `Table`                     | Traditional ORM       | SQLAlchemy 2.0 ORM           |
| ------------------ | -------------------------------- | --------------------- | ---------------------------- |
| Definition         | `Table()`                        | `Column()` in a class | `mapped_column()` in a class |
| Requires a class   | No                               | Yes                   | Yes                          |
| ORM object support | Not directly                     | Yes                   | Yes                          |
| Relationships      | Manual joins                     | `relationship()`      | `relationship()`             |
| Best suited for    | SQL queries and table operations | Existing ORM projects |

Think of SQLAlchemy as a way to communicate with your database. Three important concepts are:

- session — manages ORM objects and their database changes.
- execute() — sends a SQL statement or SQL expression to the database.
- commit() — permanently saves the current transaction's changes.
