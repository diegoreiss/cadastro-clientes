from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from .base import Base
from ..Configs.config import config_database


class DBConnectionHandler:
    __CONNECTION_STRING = config_database()

    def __init__(self):
        self.__engine = self.__create_engine()
        self.session = None
        self.__create_database()

    def __create_database(self):
        engine = self.__create_engine()
        if not database_exists(engine.url):
            create_database(engine.url)

    def __create_table(self):
        Base.metadata.create_all(bind=self.__engine)

    def __create_engine(self):
        engine = create_engine(self.__CONNECTION_STRING, echo=True)

        return engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
