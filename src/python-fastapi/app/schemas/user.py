from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class BaseSchema(BaseModel):
    """
    基础 Schema, 启用 Pydantic v2 ORM 属性读取
    """
    model_config = {"from_attributes": True}

class UserBase(BaseModel):
    """
    通用用户基础模型
    """
    username: str = Field(..., max_length=10, description="用户名, 最大长度10字符")
    email: EmailStr = Field(..., description="用户邮箱, 必须是有效的邮箱格式")

class UserCreate(UserBase):
    """
    创建用户时使用的模型
    """
    password: str = Field(..., min_length=8, description="密码, 最小长度8字符")

class UserRead(UserBase, BaseSchema):
    """
    读取用户, 返回用户信息时使用的模型
    """
    id: int = Field(..., description="用户ID")
    created_at: datetime = Field(..., description="用户创建时间, ISO 8601 格式")
    updated_at: datetime = Field(..., description="用户更新时间, ISO 8601 格式")
    
class UserUpdate(BaseModel):
    """
    更新用户时使用的模型
    """
    username: Optional[str] = Field(None, max_length=10, description="新用户名, 最大长度10字符")
    email: Optional[EmailStr] = Field(None, description="新用户邮箱, 必须是有效的邮箱格式")
    password: Optional[str] = Field(None, min_length=8, description="新密码, 最小长度8字符")