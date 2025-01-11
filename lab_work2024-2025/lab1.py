from fontTools.merge.util import first
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Таблица Member_type
class Member_type(Base):
    __tablename__ = 'Member_type'

    member_id = Column(Integer, primary_key = True) # id участника
    member_casual = Column(VARCHAR) # участник


# Таблица Trip
class Trip(Base):
    __tablename__ = 'Trip'

    ride_key = Column(Integer, primary_key = True)
    ride_id = Column(VARCHAR) # id путешествия
    rideable_type_id = Column(Integer) # id типа путешествия
    start_date = Column(Integer) # начало путешествия
    end_date = Column(Integer) #окончание путешествия


class Station(Base):
    __tablename__ = 'Station'

    station_key = Column(Integer, primary_key = True) # ключ
    station_id = Column(VARCHAR) # id станции
    station_name = Column(VARCHAR) # имя станции
    station_lat = Column(Integer)
    station_lng = Column(Integer) #длина станции


def setup_database(database_path="2023-2024tripdata.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine


def create_session(engine):
    Session = sessionmaker(bind = engine)
    return Session()

engine = setup_database("sqlite:///2023-2024tripdata.sqlite")
session = create_session(engine)

session.commit()