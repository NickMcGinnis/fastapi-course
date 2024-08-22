from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import auth, post, user, vote
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware

# Disable this line to avoid creating tables on every run
# Since Alembic is used for migrations

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
