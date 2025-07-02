from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import verify_password

def authenticate_user(
    db: Session,
    username_or_email: str,
    password: str
) -> Optional[User]:
    """
    根据用户名或邮箱 + 密码验证用户身份。
    成功返回 User ORM 实例，否则返回 None。
    """
    # 支持用 username 或 email 登录
    user = (
        db.query(User)
            .filter((User.username == username_or_email) | (User.email == username_or_email))
            .first()
    )
    if not user:
        return None
    if not verify_password(password, str(user.hashed_password)):
        return None
    return user
