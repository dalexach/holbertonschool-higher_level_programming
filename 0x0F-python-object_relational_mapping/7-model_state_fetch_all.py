#!/usr/bin/python3
"""
Lists all State objects from the DB hbtn_0e_4_usa
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    for state in session().query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session().close()
