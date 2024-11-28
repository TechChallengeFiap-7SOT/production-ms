from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class DBConnectionHandler:
    ''' Class to handle application database connection '''
    
    def __init__(self):
        # Private
        self.__connection_string = os.environ['POSTGRES_STRING_CONN']
        
        # Public
        self.session = None
        
    def get_engine(self):
        ''' Get connection engine '''
        return create_engine(self.__connection_string)
        
    def __enter__(self):
        try:
            engine = create_engine(self.__connection_string)
            session_maker = sessionmaker()
            self.session = session_maker(bind=engine)
            return self
        except Exception as err:
            raise err
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
