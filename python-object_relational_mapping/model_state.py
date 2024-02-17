#!/usr/bin/python3
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

username = 'root'
password = ''
host = 'localhost'
port = '3306'
database = 'hbtn_0e_6_usa'

# Define the ORM model
Base = declarative_base()

class State(Base):
    # Specifies the name of the table in the database
    __tablename__ = 'states'
    # Define the columns of the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

# Example usage
if __name__ == "__main__":
 
    # Create the SQLAlchemy engine
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}', echo=True)

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

    