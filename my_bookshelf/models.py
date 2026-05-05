from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    # TODO: would be cute to have some stats for this
    nationality = Column(String)
    birth_date = Column(Date)

    # One author can have many books: books is a list of Book objects, and each 
    # Book object in this list has this Author as author field. 
    # TODO: implement many to many: some books are written by multiple authors 
    books = relationship("Book", back_populates="author")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Borrower(Base):
    __tablename__ = "borrowers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birthday = Column(Date)
    #TODO: add more relevant info about them as a person? or store their past borrowed books, 
    # or their opinion on the books? 

    # Relationship: One borrower can borrow many books
    borrowed_books = relationship("Book", back_populates="borrower")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

#TODO
# class Translator(Base):
#       # for translated books

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    publication_date = Column(Date)
    language = Column(String)

    # Foreign keys
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    borrower_id = Column(Integer, ForeignKey("borrowers.id"))

    # Relationships
    author = relationship("Author", back_populates="books")
    borrower = relationship("Borrower", back_populates="borrowed_books")

    # Lending info
    date_of_lending = Column(DateTime)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
