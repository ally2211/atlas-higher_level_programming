#!/usr/bin/python3
"""
This module defines the State class using SQLAlchemy ORM
to represent the 'states' table in a database.
"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
#from model_city import City

username = 'root'
password = ''
host = 'localhost'
port = '3306'
database = 'hbtn_0e_6_usa'

# Define the ORM model
Base = declarative_base()


class State(Base):
    """
    A State class that maps to the 'states' table in the database.
    """
    # Specifies the name of the table in the database
    __tablename__ = 'states'
    # Define the columns of the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    #cities = relationship("City", back_populates="state")

# Example usage
if __name__ == "__main__":
    # Construct the connection string
    cstring = f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}'

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
