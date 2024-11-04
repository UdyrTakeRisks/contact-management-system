from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    owner_user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))


engine = create_engine('sqlite:///db.sqlite3')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
