from flask import Flask, render_template, request, redirect, url_for, flash
from lab1_crud import setup_database, create_session, add_member, read_member, edit_member, delete_member, add_trip, read_trip, edit_trip, delete_trip, add_station, read_station, edit_station, delete_station
from lab1 import Member_type, Trip, Station
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.secret_key = '123456789'

# Инициализация базы данных и сессии
engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    return render_template('index.html')

# Участники (Member_type)
@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'POST':
        casual = request.form['casual']
        if casual:
            add_member(session, casual)
            flash('Участник добавлен', 'success')
        else:
            flash('Поле "casual" не может быть пустым', 'error')
    members = session.query(Member_type).all()
    return render_template('members.html', members=members)

@app.route('/members/<int:member_id>/edit', methods=['GET', 'POST'])
def edit_member_route(member_id):
    member = read_member(session, member_id)
    if request.method == 'POST':
        casual = request.form['casual']
        if casual:
            edit_member(session, member_id, casual)
            flash('Участник обновлен', 'success')
            return redirect(url_for('members'))
        else:
            flash('Поле "casual" не может быть пустым', 'error')
    return render_template('edit_member.html', member=member)

@app.route('/members/<int:member_id>/delete', methods=['POST'])
def delete_member_route(member_id):
    delete_member(session, member_id)
    flash('Участник удален', 'success')
    return redirect(url_for('members'))

# Поездки (Trip)
@app.route('/trips', methods=['GET', 'POST'])
def trips():
    if request.method == 'POST':
        ride_id = request.form['ride_id']
        rideable_type_id = request.form['rideable_type_id']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        if ride_id and rideable_type_id and start_date and end_date:
            add_trip(session, ride_id, int(rideable_type_id), int(start_date), int(end_date))
            flash('Поездка добавлена', 'success')
        else:
            flash('Все поля должны быть заполнены', 'error')
    trips = session.query(Trip).limit(2000)
    return render_template('trips.html', trips=trips)

@app.route('/trips/<int:ride_key>/edit', methods=['GET', 'POST'])
def edit_trip_route(ride_key):
    trip = read_trip(session, ride_key)
    if request.method == 'POST':
        ride_id = request.form['ride_id']
        rideable_type_id = request.form['rideable_type_id']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        edit_trip(session, ride_key, ride_id, int(rideable_type_id), int(start_date), int(end_date))
        flash('Поездка обновлена', 'success')
        return redirect(url_for('trips'))
    return render_template('edit_trip.html', trip=trip)

@app.route('/trips/<int:ride_key>/delete', methods=['POST'])
def delete_trip_route(ride_key):
    delete_trip(session, ride_key)
    flash('Поездка удалена', 'success')
    return redirect(url_for('trips'))

# Станции (Station)
@app.route('/stations', methods=['GET', 'POST'])
def stations():
    if request.method == 'POST':
        station_id = request.form['station_id']
        station_name = request.form['station_name']
        station_lat = request.form['station_lat']
        station_lng = request.form['station_lng']
        if station_id and station_name and station_lat and station_lng:
            add_station(session, station_id, station_name, int(station_lat), int(station_lng))
            flash('Станция добавлена', 'success')
        else:
            flash('Все поля должны быть заполнены', 'error')
    stations = session.query(Station).all()
    return render_template('stations.html', stations=stations)

@app.route('/stations/<int:station_key>/edit', methods=['GET', 'POST'])
def edit_station_route(station_key):
    station = read_station(session, station_key)
    if request.method == 'POST':
        station_id = request.form['station_id']
        station_name = request.form['station_name']
        station_lat = request.form['station_lat']
        station_lng = request.form['station_lng']
        edit_station(session, station_key, station_id, station_name, int(station_lat), int(station_lng))
        flash('Станция обновлена', 'success')
        return redirect(url_for('stations'))
    return render_template('edit_station.html', station=station)

@app.route('/stations/<int:station_key>/delete', methods=['POST'])
def delete_station_route(station_key):
    delete_station(session, station_key)
    flash('Станция удалена', 'success')
    return redirect(url_for('stations'))

if __name__ == '__main__':
    app.run(debug=True)