from fastapi import FastAPI
from app.core.logging import setup_logging
from app.db.base import Base
from app.db.session import engine
from app.routes import user, auth

setup_logging()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Practice Hub")


app.include_router(user.router, tags=["User"])
app.include_router(auth.router)
