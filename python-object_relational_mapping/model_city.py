#!/usr/bin/python3
"""
This module defines the State class using SQLAlchemy ORM
to represent the 'states' table in a database.
"""
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from model_state import Base, State

username = 'root'
password = ''
host = 'localhost'
port = '3306'
database = 'hbtn_0e_14_usa'


class City(Base):
    """
    A State class that maps to the 'states' table in the database.
    """
    # Specifies the name of the table in the database
    __tablename__ = 'cities'
    # Define the columns of the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", backref="cities")

# Example usage
if __name__ == "__main__":
    # Construct the connection string
    cstring = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

    # Create the engine with echo set to True
    engine = create_engine(cstring, echo=True)

    # Create all tables that don't already exist in the database
    Base.metadata.create_all(engine)

    # Create a sessionmaker bound to the engine
    Session = sessionmaker(bind=engine)

    # Instantiate a session
    session = Session()

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
