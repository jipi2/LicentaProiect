from sqlalchemy import create_engine, Column, Integer, String, Sequence, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

engine = create_engine('mysql+mysqlconnector://root:root@localhost:2703/testdb')
Session = sessionmaker(bind=engine)
session = Session()


class Base(DeclarativeBase):
    pass

class SuperUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    files = Column(LargeBinary(length=(2**32)-1))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)

Base.metadata.create_all(engine)