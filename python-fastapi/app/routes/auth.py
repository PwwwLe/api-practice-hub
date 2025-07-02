from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.crud.auth import authenticate_user
from app.core.security import create_access_token
from app.schemas.token import Token
from app.schemas.user import UserRead
from app.api.deps import get_current_user
from app.db.session import get_db

router = APIRouter(tags=["Auth"])

@router.post("/login", response_model=Token, summary="用户登录并获取 Token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    使用表单字段 username (即 email 或用户名) 和 password 进行认证，
    成功则生成并返回 Bearer Token。
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({ "sub": user.username })
    return { "access_token": access_token, "token_type": "bearer" }

@router.get("/users/me", response_model=UserRead, summary="获取当前登录用户信息")
def read_current_user(
    current_user = Depends(get_current_user),
):
    """
    依赖 get_current_user，自动验证 Token 并注入当前用户。
    """
    return current_user
