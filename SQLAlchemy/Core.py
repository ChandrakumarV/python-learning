from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    select,
)

engine = create_engine(
    # "postgresql+psycopg://postgres:password@localhost:5432/mydb",
    "sqlite:///ddd.db",
    echo=True,
)

meta = MetaData()

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
)

posts = Table(
    "posts",
    meta,
    Column("id", Integer, primary_key=True),
    Column("title", String(200), nullable=False),
    Column("user_id", Integer, ForeignKey("users.id")),
)

# Create tables
meta.create_all(engine)


conn = engine.connect()

# Users - Insert Query -----------------
insert_query = users.insert().values(name="Chandra")
result = conn.execute(insert_query)

user_id = result.inserted_primary_key[0]

# Post - Insert Query ------------------
post_insert_query = posts.insert().values(
    title="Learning Python",
    user_id=user_id,
)
conn.execute(post_insert_query)

conn.commit()

# Select with JOIN's --------------------
select_query = select(users.c.name, posts.c.title).join(
    posts, users.c.id == posts.c.user_id
)

rows = conn.execute(select_query).all()


for row in rows:
    print(row)
