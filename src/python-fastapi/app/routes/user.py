from typing import List
from fastapi import APIRouter, Depends, Path, Query, HTTPException, status
from sqlalchemy.orm import Session
from app.crud.user import (
    create_user, get_user,
    get_users, update_user, delete_user
)
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.db.session import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def api_create_user(
    user: UserCreate, db: Session = Depends(get_db)
) -> UserRead:
    """注册新用户"""
    return create_user(db=db, user=user)

@router.get("/{user_id}", response_model=UserRead)
def api_get_user(
    user_id: int = Path(..., title="用户ID", description="要查询的用户ID"),
    db: Session = Depends(get_db)
) -> UserRead:
    """根据 ID 查询单个用户"""
    return get_user(db=db, user_id=user_id)

@router.get("/", response_model=List[UserRead])
def api_list_users(
    skip: int = Query(0, ge=0, title="跳过的用户数量", description="用于分页"),
    limit: int = Query(100, le=100, title="返回的用户数量", description="最大返回100个用户"),
    db: Session = Depends(get_db)
) -> List[UserRead]:
    """查询用户列表"""
    return get_users(db=db, skip=skip, limit=limit)

@router.patch("/{user_id}", response_model=UserRead)
def api_update_user(
    user_upd: UserUpdate,
    user_id: int = Path(..., title="用户ID", description="要更新的用户ID"),
    db: Session = Depends(get_db)
) -> UserRead:
    """更新用户信息"""
    return update_user(db=db, user_id=user_id, user_upd=user_upd)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def api_delete_user(
    user_id: int = Path(..., title="用户ID", description="要删除的用户ID"),
    db: Session = Depends(get_db)
) -> None:
    """注销用户"""
    delete_user(db=db, user_id=user_id)
    return None