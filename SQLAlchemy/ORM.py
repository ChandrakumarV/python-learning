from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

engine = create_engine(
    # "postgresql+psycopg://postgres:password@localhost:5432/mydb",
    "sqlite:///database.db",
    echo=True,
)


# Table Definitions --------------------
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="posts")


# Create tables ------------------------
Base.metadata.create_all(engine)


session = Session(engine)

# Users - Insert Query -----------------
user = User(name="Chandra")
session.add(user)
session.flush()  # Generates user.id without committing

user_id = user.id

# Post - Insert Query ------------------
post = Post(
    title="Learning Python",
    user_id=user_id,
)
session.add(post)

session.commit()

# Select with JOIN ---------------------
select_query = select(User.name, Post.title).join(Post, User.id == Post.user_id)

rows = session.execute(select_query).all()

for row in rows:
    print(row)

session.close()
