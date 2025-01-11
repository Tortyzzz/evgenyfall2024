import tkinter as tk
from tkinter import messagebox, ttk
from sqlalchemy.orm import sessionmaker
from lab1 import Member_type, Trip, Station
from lab1_crud import setup_database, create_session, add_member, read_member, edit_member, delete_member, add_trip, \
    read_trip, edit_trip, delete_trip, add_station, read_station, edit_station, delete_station

# Инициализация базы данных и сессии
engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


# Функция для обновления данных в Treeview
def update_treeview(tree, table_class):
    # Очистка текущих данных в Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Получение данных из таблицы
    records = session.query(table_class).limit(1000)

    # Добавление данных в Treeview
    for record in records:
        tree.insert("", "end", values=tuple(record.__dict__.values())[1:])  # Игнорируем первый атрибут(id)

# Функция для переключения темы
def toggle_theme():
    global current_theme
    if current_theme == "light":
        set_dark_theme()
        current_theme = "dark"
    else:
        set_light_theme()
        current_theme = "light"

# Установка светлой темы
def set_light_theme():
    root.configure(bg="white")
    style.configure("TFrame", background="white")
    style.configure("TLabel", background="white", foreground="black")
    style.configure("TButton", background="#f0f0f0", foreground="black")
    style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
    style.map("TButton", background=[("active", "#d9d9d9")])

# Установка темной темы
def set_dark_theme():
    root.configure(bg="black")
    style.configure("TFrame", background="#black")
    style.configure("TLabel", background="#black", foreground="white")
    style.configure("TButton", background="#black", foreground="white")
    style.configure("Treeview", background="#black", foreground="white", fieldbackground="white")
    style.map("TButton", background=[("active", "white")])

# Member_type
def add_member_gui():
    casual = entry_member_casual.get()
    if casual:
        add_member(session, casual)
        update_treeview(tree_member, Member_type)  # Обновляем Treeview
        messagebox.showinfo("OK", "Участник добавлен")
    else:
        messagebox.showwarning("Ошибка", "Поле 'casual' не может быть пустым")


def read_member_gui():
    member_id = entry_member_id.get()
    if member_id:
        member = read_member(session, int(member_id))
        if member:
            messagebox.showinfo("Результат", f"ID: {member.member_id}, Casual: {member.member_casual}")
        else:
            messagebox.showwarning("Ошибка", "Участник не найден")
    else:
        messagebox.showwarning("Ошибка", "Поле 'ID' не может быть пустым")


def edit_member_gui():
    member_id = entry_member_id.get()
    casual = entry_member_casual.get()
    if member_id and casual:
        edit_member(session, int(member_id), casual)
        update_treeview(tree_member, Member_type)  # Обновляем Treeview
        messagebox.showinfo("OK", "Участник обновлен")
    else:
        messagebox.showwarning("Ошибка", "Поля 'ID' и 'casual' не могут быть пустыми")


def delete_member_gui():
    member_id = entry_member_id.get()
    if member_id:
        delete_member(session, int(member_id))
        update_treeview(tree_member, Member_type)  # Обновляем Treeview
        messagebox.showinfo("OK", "Участник удален")
    else:
        messagebox.showwarning("Ошибка", "Поле 'ID' не может быть пустым")


# Trip
def add_trip_gui():
    ride_id = entry_ride_id.get()
    rideable_type_id = entry_rideable_type_id.get()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()
    if ride_id and rideable_type_id and start_date and end_date:
        add_trip(session, ride_id, int(rideable_type_id), int(start_date), int(end_date))
        update_treeview(tree_trip, Trip)  # Обновляем Treeview
        messagebox.showinfo("OK", "Поездка добавлена")
    else:
        messagebox.showwarning("Ошибка", "Все поля должны быть заполнены")


def read_trip_gui():
    ride_key = entry_ride_key.get()
    if ride_key:
        trip = read_trip(session, int(ride_key))
        if trip:
            messagebox.showinfo("Результат",
                                f"Ride Key: {trip.ride_key}, Ride ID: {trip.ride_id}, Start Date: {trip.start_date}, End Date: {trip.end_date}")
        else:
            messagebox.showwarning("Ошибка", "Поездка не найдена")
    else:
        messagebox.showwarning("Ошибка", "Поле 'Ride Key' не может быть пустым")


def edit_trip_gui():
    ride_key = entry_ride_key.get()
    ride_id = entry_ride_id.get()
    rideable_type_id = entry_rideable_type_id.get()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()
    if ride_key:
        edit_trip(session, int(ride_key), ride_id, int(rideable_type_id) if rideable_type_id else None,
                  int(start_date) if start_date else None, int(end_date) if end_date else None)
        update_treeview(tree_trip, Trip)  # Обновляем Treeview
        messagebox.showinfo("OK", "Поездка обновлена")
    else:
        messagebox.showwarning("Ошибка", "Поле 'Ride Key' не может быть пустым")

def delete_trip_gui():
    ride_key = entry_ride_key.get()
    if ride_key:
        delete_trip(session, int(ride_key))
        update_treeview(tree_trip, Trip)  # Обновляем Treeview
        messagebox.showinfo("OK", "Поездка удалена")
    else:
        messagebox.showwarning("Ошибка", "Поле 'Ride Key' не может быть пустым")

#Station
def add_station_gui():
    station_id = entry_station_id.get()
    station_name = entry_station_name.get()
    station_lat = entry_station_lat.get()
    station_lng = entry_station_lng.get()
    if station_id and station_name and station_lat and station_lng:
        add_station(session, station_id, station_name, int(station_lat), int(station_lng))
        update_treeview(tree_station, Station)  # Обновляем Treeview после добавления станции
        messagebox.showinfo("OK", "Станция добавлена")
    else:
        messagebox.showwarning("Ошибка", "Все поля должны быть заполнены")


def read_station_gui():
    station_key = entry_station_key.get()
    if station_key:
        station = read_station(session, int(station_key))
        if station:
            messagebox.showinfo("Результат",
            f"Station Key: {station.station_key}, Station ID: {station.station_id}, Station Name: {station.station_name}, Lat: {station.station_lat}, Lng: {station.station_lng}")
        else:
            messagebox.showwarning("Ошибка", "Станция не найдена")
    else:
        messagebox.showwarning("Ошибка", "Поле 'Station Key' не может быть пустым")


def edit_station_gui():
    station_key = entry_station_key.get()
    station_id = entry_station_id.get()
    station_name = entry_station_name.get()
    station_lat = entry_station_lat.get()
    station_lng = entry_station_lng.get()
    if station_key:
        edit_station(session, int(station_key), station_id, station_name, int(station_lat) if station_lat else None,
                     int(station_lng) if station_lng else None)
        update_treeview(tree_station, Station)  # Обновляем Treeview после изменения станции
        messagebox.showinfo("OK", "Станция обновлена")
    else:
        messagebox.showwarning("Ошибка", "Поле 'Station Key' не может быть пустым")


def delete_station_gui():
    station_key = entry_station_key.get()
    if station_key:
        delete_station(session, int(station_key))
        update_treeview(tree_station, Station)  # Обновляем Treeview
        messagebox.showinfo("OK", "Станция удалена")
    else:
        messagebox.showwarning("Ошибка", "Поле 'Station Key' не может быть пустым")


# Окно
root = tk.Tk()
root.title("Приложение для БД")
root.resizable(False, False)  # Запрет изменения размера

style = ttk.Style(root)
current_theme = "light"  # Начальная тема
set_light_theme()  # Устанавливаем светлую тему по умолчанию

# Кнопка для переключения темы
if current_theme == "light":
    tema = tk.Button(root, text = 'Темная тема', bg = "black", fg = "white", command=toggle_theme)
else:
    tema = tk.Button(root, text = "Светлая тема", bg = "white", fg = "black", command=toggle_theme)
theme_button = tk.Button(root, text = "Светлая тема", bg = "white", fg = "black", command=toggle_theme)
theme_button.pack(pady=10)

# Вкладки для каждой таблицы
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=False)

### Вкладка Member_type
frame_member = ttk.Frame(notebook)
notebook.add(frame_member, text="Участники")

# Поля ввода Member_type
tk.Label(frame_member, text="ID участника:").grid(row=0, column=4, padx=10, pady=7)
entry_member_id = tk.Entry(frame_member)
entry_member_id.grid(row=0, column=5, padx=15, pady=5)

tk.Label(frame_member, text="Casual:").grid(row=1, column=4, padx=10, pady=7)
entry_member_casual = tk.Entry(frame_member)
entry_member_casual.grid(row=1, column=5, padx=15, pady=5)

# Кнопки Member_type
tk.Button(frame_member, bg = "green", fg = "white", text="Добавить участника", command=add_member_gui).grid(row=0, column=6, padx=15, pady=8)
tk.Button(frame_member, bg = "blue", fg = "white", text="Найти участника", command=read_member_gui).grid(row=0, column=7, padx=15, pady=8)
tk.Button(frame_member, bg = "green", fg = "white", text="Обновить участника", command=edit_member_gui).grid(row=1, column=6, padx=15, pady=8)
tk.Button(frame_member, bg = "red", fg = "white", text="Удалить участника", command=delete_member_gui).grid(row=1, column=7, padx=15, pady=8)

# Treeview Member_type
columns_member = ("Casual", "ID")
tree_member = ttk.Treeview(frame_member, columns=columns_member, show="headings")
tree_member.heading("ID", text="ID")
tree_member.heading("Casual", text="Casual")
tree_member.grid(row=4, column=4, columnspan=6, padx=10, pady=10)

# Обновление данных в Treeview
tk.Button(frame_member, bg = "green", fg = "white",  text="Обновить данные", command=lambda: update_treeview(tree_member, Member_type)).grid(row=5,
                                                                                                                column=4,
                                                                                                                columnspan=6,
                                                                                                                pady=10)

### Вкладка Trip
frame_trip = ttk.Frame(notebook)
notebook.add(frame_trip, text="Поездки")

# Поля ввода Trip
tk.Label(frame_trip, text="Ride Key:").grid(row=0, column=0, padx=10, pady=5)
entry_ride_key = tk.Entry(frame_trip)
entry_ride_key.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_trip, text="Ride ID:").grid(row=1, column=0, padx=10, pady=5)
entry_ride_id = tk.Entry(frame_trip)
entry_ride_id.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_trip, text="Rideable Type ID:").grid(row=2, column=0, padx=10, pady=5)
entry_rideable_type_id = tk.Entry(frame_trip)
entry_rideable_type_id.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_trip, text="Start Date:").grid(row=3, column=0, padx=10, pady=5)
entry_start_date = tk.Entry(frame_trip)
entry_start_date.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame_trip, text="End Date:").grid(row=4, column=0, padx=10, pady=5)
entry_end_date = tk.Entry(frame_trip)
entry_end_date.grid(row=4, column=1, padx=10, pady=5)

# Кнопки Trip
tk.Button(frame_trip, bg = "green", fg = "white", text="Добавить поездку", command=add_trip_gui).grid(row=2, column=3, padx=10, pady=5)
tk.Button(frame_trip, bg = "blue", fg = "white",text="Найти поездку", command=read_trip_gui).grid(row=2, column=4, padx=10, pady=5)
tk.Button(frame_trip, bg = "green", fg = "white",text="Обновить поездку", command=edit_trip_gui).grid(row=3, column=3, padx=10, pady=5)
tk.Button(frame_trip, bg = "red", fg = "white", text="Удалить поездку", command=delete_trip_gui).grid(row=3, column=4, padx=10, pady=5)

# Treeview Trip
columns_trip = ("Ride Key", "Start Date", "End Date", "Rideable Type ID", "Ride ID")
tree_trip = ttk.Treeview(frame_trip, columns=columns_trip, show="headings")
tree_trip.heading("Ride Key", text="Ride Key")
tree_trip.heading("Ride ID", text="Ride ID")
tree_trip.heading("Rideable Type ID", text="Rideable Type ID")
tree_trip.heading("Start Date", text="Start Date")
tree_trip.heading("End Date", text="End Date")
tree_trip.grid(row=7, column=0, columnspan=7, padx=10, pady=10)

# Кнопка для обновления данных в Treeview
tk.Button(frame_trip, bg = "green", fg = "white", text="Обновить данные", command=lambda: update_treeview(tree_trip, Trip)).grid(row=8, column=1,
                                                                                                     columnspan=4,
                                                                                                     pady=10)
### Вкладка для Station
frame_station = ttk.Frame(notebook)
notebook.add(frame_station, text="Станции")

# Поля ввода для Station
tk.Label(frame_station, text="Station Key:").grid(row=0, column=1, padx=10, pady=8)
entry_station_key = tk.Entry(frame_station)
entry_station_key.grid(row=0, column=2, padx=10, pady=5)

tk.Label(frame_station, text="Station ID:").grid(row=1, column=1, padx=10, pady=8)
entry_station_id = tk.Entry(frame_station)
entry_station_id.grid(row=1, column=2, padx=10, pady=5)

tk.Label(frame_station, text="Station Name:").grid(row=2, column=1, padx=10, pady=8)
entry_station_name = tk.Entry(frame_station)
entry_station_name.grid(row=2, column=2, padx=10, pady=5)

tk.Label(frame_station, text="Station Lat:").grid(row=3, column=1, padx=10, pady=8)
entry_station_lat = tk.Entry(frame_station)
entry_station_lat.grid(row=3, column=2, padx=10, pady=5)

tk.Label(frame_station, text="Station Lng:").grid(row=4, column=1, padx=10, pady=8)
entry_station_lng = tk.Entry(frame_station)
entry_station_lng.grid(row=4, column=2, padx=10, pady=5)

# Кнопки для операций с Station
tk.Button(frame_station, bg = "green", fg = "white", text="Добавить станцию", command=add_station_gui).grid(row=2, column=3, padx=10, pady=5)
tk.Button(frame_station, bg = "blue", fg = "white", text="Найти станцию", command=read_station_gui).grid(row=2, column=4, padx=10, pady=5)
tk.Button(frame_station, bg = "green", fg = "white", text="Обновить станцию", command=edit_station_gui).grid(row=3, column=3, padx=10, pady=5)
tk.Button(frame_station, bg = "red", fg = "white", text="Удалить станцию", command=delete_station_gui).grid(row=3, column=4, padx=10, pady=5)

# Treeview для Station
columns_station = ("Station Name", "Lng", "Station ID", "Lat", "Station Key")
tree_station = ttk.Treeview(frame_station, columns=columns_station, show="headings")
tree_station.heading("Station Key", text="Station Key")
tree_station.heading("Station ID", text="Station ID")
tree_station.heading("Station Name", text="Station Name")
tree_station.heading("Lat", text="Lat")
tree_station.heading("Lng", text="Lng")
tree_station.grid(row=6, column=1, columnspan=5, padx=10, pady=10)

# Кнопка для обновления данных в Treeview
tk.Button(frame_station, bg = "green", fg = "white", text="Обновить данные", command=lambda: update_treeview(tree_station, Station)).grid(row=8,
                                                                                                              column=1,
                                                                                                              columnspan=5,
                                                                                                              pady=10)
# Запуск основного цикла
root.mainloop()