from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError
from app.core.security import decode_access_token
from app.db.session import get_db
from app.models.user import User
from app.schemas.token import TokenData

# ① 声明 Token 从哪个接口获取
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login", scheme_name="Bearer")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """
    1. 从 Authorization: Bearer <token> 中拿到 token
    2. decode_access_token 解码 -> payload
    3. 从 payload.sub 拿到用户名，查询数据库
    4. 返回 User ORM 对象
    """
    try:
        payload = decode_access_token(token)
        token_data = TokenData(**{ "sub": payload.get("sub") })
        username = token_data.sub
        if username is None:
            raise JWTError()
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无法验证凭证",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户不存在",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
