# database.py

from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:************@ep-cool-bread-a5vllzk3.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)