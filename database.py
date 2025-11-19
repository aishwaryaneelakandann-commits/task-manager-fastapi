#database - Backend setup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False, #not save data automatically
    autoflush=False, #changes will not push to db automattically 
    bind=engine #tells the sessionmaker to use db engine 
) 

Base = declarative_base()

def get_db():
    """Dependency for getting database session"""
    db = SessionLocal()
    try:
        yield db #Give the database connection to the API to use
    finally:
        db.close()