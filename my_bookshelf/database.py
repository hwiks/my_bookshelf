from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# TODO: look into what this whole thing does exactly

# SQLite database URL (stored in .env for flexibility)
DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
