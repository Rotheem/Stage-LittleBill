import uuid
from sqlalchemy import select
from app import models

from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_by_email(
    email: str,
    db: AsyncSession,
) -> models.User | None:
    """Retrieve a user by its email."""
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()


async def get_user_by_id(
    user_id: uuid.UUID,
    db: AsyncSession,
) -> models.User | None:
    """Retrieve a user by its id."""
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    return result.scalars().first()


async def create_user(
    db: AsyncSession,
    user: models.User,
) -> None:
    """Create a new user."""
    db.add(user)
    await db.commit()
