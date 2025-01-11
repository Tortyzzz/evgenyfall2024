from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lab1 import Base, Member_type, Trip, Station

def create_session(engine):
    Session = sessionmaker(bind = engine)
    return Session()

# Функция для настройки базы данных
def setup_database(database_path="sqlite:///2023-2024tripdata.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine


def add_member(session, casual):
    member = Member_type(member_casual = casual)
    session.add(member)
    session.commit()
    print(f"Created new member with ID: {member.member_id} and casual: {member.member_casual}")
    return member

#Таблица Members
def read_member(session, member_id):
    member = session.query(Member_type).filter_by(member_id = member_id).first()
    if member:
        print(f"Read member with ID: {member.member_id}, casual: {member.member_casual}")
    else:
        print(f"Member with ID {member_id} not found")
    return member

def edit_member(session, member_id, casual):
    member = session.query(Member_type).filter_by(member_id = member_id).first()
    if member:
        old_casual = member.member_casual
        member.member_casual = casual
        session.commit()
        print(f"Updated member with ID: {member.member_id} from casual: {old_casual} to casual: {member.member_casual}")
    else:
        print(f"Member with ID {member_id} not found")
    return member

def delete_member(session, member_id):
    member = session.query(Member_type).filter_by(member_id = member_id).first()
    if member:
        session.delete(member)
        session.commit()
        print(f"Deleted member with ID: {member_id}")
    else:
        print(f"Member with ID {member_id} not found")
    return member

#Таблциа Trip
def add_trip(session, ride_id, rideable_type_id, start_date, end_date):
    new_trip = Trip(ride_id = ride_id, rideable_type_id = rideable_type_id, start_date = start_date, end_date = end_date)
    session.add(new_trip)
    session.commit()
    print(f"Created new trip with ride_key: {new_trip.ride_key}, ride_id: {new_trip.ride_id}, start_date: {new_trip.start_date}, end_date: {new_trip.end_date}")
    return new_trip

def read_trip(session, ride_key):
    trip = session.query(Trip).filter_by(ride_key = ride_key).first()
    if trip:
        print(f"Read trip with ride_key: {trip.ride_key}, ride_id: {trip.ride_id},Rideable_type_id: {trip.rideable_type_id}, start_date: {trip.start_date}, end_date: {trip.end_date}")
    else:
        print(f"Trip with ride_key {ride_key} not found")
    return trip

def edit_trip(session, ride_key, ride_id = None, rideable_type_id = None, start_date = None, end_date = None):
    trip = session.query(Trip).filter_by(ride_key = ride_key).first()
    if trip:
        if ride_id:
            print(f"Updating trip with ride_key: {trip.ride_key}, changing ride_id from {trip.ride_id} to {ride_id}")
            trip.ride_id = ride_id
        if rideable_type_id:
            print(f"Updating trip with ride_key: {trip.ride_key}, changing rideable_type_id from {trip.rideable_type_id} to {rideable_type_id}")
            trip.rideable_type_id = rideable_type_id
        if start_date:
            print(f"Updating trip with ride_key: {trip.ride_key}, changing start_date from {trip.start_date} to {start_date}")
            trip.start_date = start_date
        if end_date:
            print(f"Updating trip with ride_key: {trip.ride_key}, changing end_date from {trip.end_date} to {end_date}")
            trip.end_date = end_date
        session.commit()
    else:
        print(f"Trip with ride_key {ride_key} not found")
    return trip

def delete_trip(session, ride_key):
    trip = session.query(Trip).filter_by(ride_key = ride_key).first()
    if trip:
        session.delete(trip)
        session.commit()
        print(f"Deleted trip with ride_key: {ride_key}")
    else:
        print(f"Trip with ride_key {ride_key} not found")
    return trip

#Таблица Станции
def add_station(session, station_id, station_name, station_lat, station_lng):
    new_station = Station(station_id = station_id, station_name = station_name, station_lat = station_lat, station_lng = station_lng)
    session.add(new_station)
    session.commit()
    print(f"Created new station with station_key: {new_station.station_key}, station_id: {new_station.station_id}, station_name: {new_station.station_name}, station_lat: {new_station.station_lat}, station_lng: {new_station.station_lng}")
    return new_station

def read_station(session, station_key):
    station = session.query(Station).filter_by(station_key = station_key).first()
    if station:
        print(f"Read station with station_key: {station.station_key}, station_id: {station.station_id}, station_name: {station.station_name}, station_lat: {station.station_lat}, station_lng: {station.station_lng}")
    else:
        print(f"Station with station_key {station_key} not found")
    return station

def edit_station(session, station_key, station_id = None, station_name = None, station_lat = None, station_lng = None):
    station = session.query(Station).filter_by(station_key = station_key).first()
    if station:
        if station_id:
            print(f"Updating station with station_key: {station.station_key}, changing station_id from {station.station_id} to {station_id}")
            station.station_id = station_id
        if station_name:
            print(f"Updating station with station_key: {station.station_key}, changing station_name from {station.station_name} to {station_name}")
            station.station_name = station_name
        if station_lat:
            print(f"Updating station with station_key: {station.station_key}, changing station_lat from {station.station_lat} to {station_lat}")
            station.station_lat = station_lat
        if station_lng:
            print(f"Updating station with station_key: {station.station_key}, changing station_lng from {station.station_lng} to {station_lng}")
            station.station_lng = station_lng
        session.commit()
    else:
        print(f"Station with station_key {station_key} not found")
    return station

def delete_station(session, station_key):
    station = session.query(Station).filter_by(station_key = station_key).first()
    if station:
        session.delete(station)
        session.commit()
        print(f"Deleted station with station_key: {station_key}")
    else:
        print(f"Station with station_key {station_key} not found")
    return station

# Пример использования
if __name__ == "__main__":
    engine = setup_database()
    session = create_session(engine)


#Проверка кода
    creating_member = add_member(session, "Vlad")