from my_bookshelf.database import engine
from my_bookshelf.models import Base

# Create all tables
Base.metadata.create_all(bind=engine)
print("Database tables created!")
