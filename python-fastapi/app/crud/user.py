from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.core.security import get_password_hash

def create_user(db: Session, user: UserCreate) -> UserRead:
    """创建新用户"""
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名或邮箱已被使用"
        )
    return UserRead.model_validate(db_user)

def get_user(db: Session, user_id: int) -> UserRead:
    """根据 ID 查询单个用户"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户未找到")
    return UserRead.model_validate(db_user)

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[UserRead]:
    """查询用户列表"""
    users = db.query(User).offset(skip).limit(limit).all()
    return [UserRead.model_validate(user) for user in users]

def update_user(db: Session, user_id: int, user_upd: UserUpdate) -> UserRead:
    """更新用户信息"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户未找到")
    # 过滤掉未设置的字段，逐个更新
    update_data = user_upd.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if field == "password":
            setattr(db_user, "hashed_password", get_password_hash(value))
        else:
            setattr(db_user, field, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserRead.model_validate(db_user)

def delete_user(db: Session, user_id: int) -> None:
    """注销用户"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户未找到")
    db.delete(db_user)
    db.commit()