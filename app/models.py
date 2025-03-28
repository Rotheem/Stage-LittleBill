from app.utils.sqlalchemy import Base, PrimaryKey
from sqlalchemy.orm import Mapped


class User(Base):
    """User model."""

    __tablename__ = "users"

    id: Mapped[PrimaryKey]
    username: Mapped[str]
    email: Mapped[str]
    password_hash: Mapped[str]
    is_active: Mapped[bool]

    def __repr__(self) -> str:
        return f"<User {self.username}>"
