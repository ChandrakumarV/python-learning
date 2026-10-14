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
