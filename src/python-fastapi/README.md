# Python FastAPI 子项目

本目录是 `api-practice-hub` 项目的 Python 实现，使用 [FastAPI](https://fastapi.tiangolo.com/) 框架开发，复现常见 Web 接口以提升编码能力和系统设计水平。

## 📌 项目目标

- 使用 FastAPI 实现常见接口，如注册、登录、获取用户信息等
- 学习并实践 JWT 身份验证、ORM 数据建模、接口设计规范
- 提供结构清晰、模块化的 FastAPI 项目模板
- 为多语言接口对比打下基础（本项目为 Python 实现）

## 🧱 项目结构

```
python-fastapi/
├── app/
│   ├── main.py              # 应用启动入口
│   ├── models/              # 数据库模型
│   ├── schemas/             # 请求/响应数据结构
│   ├── crud/                # 数据库操作逻辑
│   ├── routes/              # 路由模块（接口定义）
│   ├── core/                # 核心工具（JWT、安全、依赖等）
│   └── db/                  # 数据库连接管理
├── requirements.txt         # Python 依赖
└── README.md
```

## 🚀 快速开始

## ✅ 实现进度（接口）

- [ ] 用户注册 `/api/register`
- [ ] 用户登录 `/api/login`
- [ ] 获取当前用户 `/api/me`
- [ ] 修改密码 `/api/reset-password`
- [ ] 文件上传
- [ ] 权限管理接口

## 📚 使用技术

- FastAPI
- SQLAlchemy
- Pydantic
- JWT（python-jose）
- SQLite（开发时使用）

## 📌 说明


## 📄 文档参考

- FastAPI 官方文档：[https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- Pydantic 官方文档：[https://docs.pydantic.dev](https://docs.pydantic.dev)
- SQLAlchemy 教程：[https://docs.sqlalchemy.org/en/20/tutorial](https://docs.sqlalchemy.org/en/20/tutorial)
- Uvicorn 文档（ASGI 服务器）：[https://www.uvicorn.org](https://www.uvicorn.org)
- python-jose（JWT 支持库）：[https://python-jose.readthedocs.io](https://python-jose.readthedocs.io)
