"""
Test data handlers
"""

from datetime import datetime, timezone

from app.core.util.password import hash_password
from app.models.user import User


async def add_empty_user() -> None:
    """Adds test users to user collection"""
    empty_user = User(
        email="empty@test.io",
        password=hash_password("empty@test.io"),
        email_confirmed_at=datetime.now(tz=timezone.utc),
    )
    await empty_user.create()
