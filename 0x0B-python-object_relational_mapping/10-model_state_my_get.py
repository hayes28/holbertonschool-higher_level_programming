#!/usr/bin/python3
"""
Script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    if item := session.query(State).filter_by(name=sys.argv[4]).first():
        print(f"{item.id}")
    else:
        print("Not found")

    session.close()
