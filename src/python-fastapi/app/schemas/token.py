from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
class TokenData(BaseModel):
    """
    用于解码后载荷的字段校验
    """
    sub: str | None = None