import sqlite3
conn = sqlite3.connect("FlightManagment")


conn.execute("DROP TABLE IF EXISTS flight")
conn.execute("DROP TABLE IF EXISTS destination")
conn.execute("DROP TABLE IF EXISTS pilot")

conn.execute("CREATE TABLE pilot (PilotID INTEGER NOT NULL, Rank VARCHAR(30), Nationality VARCHAR(40), Name VARCHAR(40), Dob DATE, HoursFlown INTEGER, LicenseID VARCHAR(20), PRIMARY KEY (PilotID))")
conn.execute("CREATE TABLE destination (DestinationID VARCHAR(20) NOT NULL, Name VARCHAR(40), Country VARCHAR(40), PRIMARY KEY (DestinationID))")
conn.execute("CREATE TABLE flight (FlightID VARCHAR(20) NOT NULL, AircraftID VARCHAR(20), Status VARCHAR(20) NOT NULL, AirlineOperator VARCHAR(40) NOT NULL, FlightArrivalTime TIME, FlightDepartureTime TIME, DestinationID VARCHAR(20) NOT NULL, PRIMARY KEY (FlightID), FOREIGN KEY (DestinationID) REFERENCES destination (DestinationID))")

conn.commit()
conn.close()