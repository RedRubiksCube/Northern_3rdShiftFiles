import sqlite3
conn = sqlite3.connect("Routes.db")
c = conn.cursor()

c.execute("""CREATE TABLE Monday (
		Run_Num int,
		Route int,
		Destination text,
		Driver_Num int,
		Driver_Name text,
		Truck_Num int,
		Cell_Num text,
		Scheduled_Start text,
		Key_Drop text,
		Training text
	)""")

c.execute("""CREATE TABLE Tuesday (
		Run_Num int,
		Route int,
		Destination text,
		Driver_Num int,
		Driver_Name text,
		Truck_Num int,
		Cell_Num text,
		Scheduled_Start text,
		Key_Drop text,
		Training text
	)""")

c.execute("""CREATE TABLE Wednesday (
		Run_Num int,
		Route int,
		Destination text,
		Driver_Num int,
		Driver_Name text,
		Truck_Num int,
		Cell_Num text,
		Scheduled_Start text,
		Key_Drop text,
		Training text
	)""")

c.execute("""CREATE TABLE Thursday (
		Run_Num int,
		Route int,
		Destination text,
		Driver_Num int,
		Driver_Name text,
		Truck_Num int,
		Cell_Num text,
		Scheduled_Start text,
		Key_Drop text,
		Training text
	)""")

c.execute("""CREATE TABLE Friday (
		Run_Num int,
		Route int,
		Destination text,
		Driver_Num int,
		Driver_Name text,
		Truck_Num int,
		Cell_Num text,
		Scheduled_Start text,
		Key_Drop text,
		Training text
	)""")

conn.commit()
conn.close()