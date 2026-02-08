import sqlite3

# This program connects to an SQLite database called FlightManagement.db.
# It allows the user to create tables and perform basic CRUD operations
# for flights, pilots, destinations, and pilot–flight assignments.


class DBOperations:
    # DBOperations handles all database-related actions.
    # This includes creating tables, inserting records,
    # updating data, deleting records, and running queries.

    def __init__(self, db_name="FlightManagement.db"):
        self.db_name = db_name
        self.conn = None
        self.cur = None

        # SQL statements used to create the database tables.
        # IF NOT EXISTS is used so tables are not recreated every time the program runs.
        self.sql_create_pilot_table = """
        CREATE TABLE IF NOT EXISTS Pilot (
          PilotID INTEGER NOT NULL,
          Rank VARCHAR(30),
          Nationality VARCHAR(40),
          Name VARCHAR(40),
          Dob DATE,
          HoursFlown INTEGER,
          LicenseID VARCHAR(20),
          PRIMARY KEY (PilotID)
        );
        """

        # The Destination table stores airport and location details.
        self.sql_create_destination_table = """
        CREATE TABLE IF NOT EXISTS Destination (
          DestinationID VARCHAR(20) NOT NULL,
          Name VARCHAR(40),
          Country VARCHAR(40),
          DestinationDate DATE,
          City VARCHAR(40) NOT NULL,
          PRIMARY KEY (DestinationID)
        );
        """

        # The Flight table stores information about individual flights.
        # Each flight is linked to a destination using DestinationID.
        self.sql_create_flight_table = """
        CREATE TABLE IF NOT EXISTS Flight (
          FlightID VARCHAR(20) NOT NULL,
          AircraftID VARCHAR(20),
          Status VARCHAR(20) NOT NULL,
          AirlineOperator VARCHAR(40) NOT NULL,
          FlightArrivalTime TIME,
          FlightDepartureTime TIME,
          DestinationID VARCHAR(20) NOT NULL,
          PRIMARY KEY (FlightID),
          FOREIGN KEY (DestinationID) REFERENCES Destination(DestinationID)
        );
        """

        # The Assigned table is a junction table.
        # It is used to represent the many-to-many relationship
        # between pilots and flights.
        self.sql_create_assigned_table = """
        CREATE TABLE IF NOT EXISTS Assigned (
          PilotID INTEGER NOT NULL,
          FlightID VARCHAR(20) NOT NULL,
          PRIMARY KEY (PilotID, FlightID),
          FOREIGN KEY (PilotID) REFERENCES Pilot(PilotID),
          FOREIGN KEY (FlightID) REFERENCES Flight(FlightID)
        );
        """

        # SQL statement to insert a new flight record.
        self.sql_insert_flight = """
        INSERT INTO Flight (FlightID, AircraftID, Status, AirlineOperator, FlightArrivalTime, FlightDepartureTime, DestinationID)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """

        # SQL statements for viewing and searching flight records.
        self.sql_select_all_flights = "SELECT * FROM Flight;"
        self.sql_search_flight = "SELECT * FROM Flight WHERE FlightID = ?;"

        # SQL statements for updating and deleting flights.
        self.sql_update_flight_status = "UPDATE Flight SET Status = ? WHERE FlightID = ?;"
        self.sql_delete_flight = "DELETE FROM Flight WHERE FlightID = ?;"

        # SQL statement to insert a new destination record.
        self.sql_insert_destination = """
        INSERT INTO Destination (DestinationID, Name, Country, DestinationDate, City)
        VALUES (?, ?, ?, ?, ?);
        """

        # SQL statements for viewing and updating destinations.
        self.sql_select_all_destinations = "SELECT * FROM Destination;"
        self.sql_update_destination = """
        UPDATE Destination
        SET Name = ?, Country = ?, DestinationDate = ?, City = ?
        WHERE DestinationID = ?;
        """

        # SQL statements for assigning pilots to flights and viewing pilot schedules.
        self.sql_assign_pilot = "INSERT INTO Assigned (PilotID, FlightID) VALUES (?, ?);"
        self.sql_view_pilot_schedule = """
        SELECT A.PilotID, A.FlightID, F.DestinationID, F.FlightDepartureTime, F.FlightArrivalTime, F.Status
        FROM Assigned A
        JOIN Flight F ON F.FlightID = A.FlightID
        WHERE A.PilotID = ?
        ORDER BY F.FlightDepartureTime;
        """

    def get_connection(self):
        # Opens a connection to the database and creates a cursor
        # so SQL commands can be executed.
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cur = self.conn.cursor()

    def close(self):
        # Closes the database connection safely after each operation.
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cur = None

    def create_tables(self):
        # Creates all required tables in the correct order
        # so foreign key constraints work properly.
        try:
            self.get_connection()
            self.cur.execute(self.sql_create_pilot_table)
            self.cur.execute(self.sql_create_destination_table)
            self.cur.execute(self.sql_create_flight_table)
            self.cur.execute(self.sql_create_assigned_table)
            self.conn.commit()
            print("Tables created (or already exist).")
        except Exception as e:
            print("Error creating tables:", e)
        finally:
            self.close()

    # ---------- FLIGHT ----------
    def add_new_flight(self):
        # Adds a new flight to the database using user input.
        try:
            self.get_connection()
            flight = FlightInfo()

            flight.set_flight_id(input("Enter FlightID (e.g. FL001): ").strip())
            flight.set_aircraft_id(input("Enter AircraftID (e.g. AC01): ").strip())
            flight.set_status(input("Enter Status (e.g. Scheduled): ").strip())
            flight.set_airline_operator(input("Enter AirlineOperator (e.g. BA): ").strip())
            flight.set_arrival_time(input("Enter ArrivalTime (HH:MM) or leave blank: ").strip() or None)
            flight.set_departure_time(input("Enter DepartureTime (HH:MM) or leave blank: ").strip() or None)
            flight.set_destination_id(input("Enter DestinationID (e.g. DST01): ").strip())

            self.cur.execute(self.sql_insert_flight, flight.as_tuple())
            self.conn.commit()
            print("Flight added.")
        except Exception as e:
            print("Error adding flight:", e)
        finally:
            self.close()

    def view_all_flights(self):
        # Displays all flights currently stored in the database.
        try:
            self.get_connection()
            self.cur.execute(self.sql_select_all_flights)
            rows = self.cur.fetchall()
            if not rows:
                print("No flights found.")
                return
            for r in rows:
                print(r)
        except Exception as e:
            print("Error viewing flights:", e)
        finally:
            self.close()

    def search_flight(self):
        # Searches for a specific flight using the FlightID.
        try:
            self.get_connection()
            flight_id = input("Enter FlightID to search: ").strip()
            self.cur.execute(self.sql_search_flight, (flight_id,))
            row = self.cur.fetchone()
            if row:
                print(row)
            else:
                print("No Record")
        except Exception as e:
            print("Error searching flight:", e)
        finally:
            self.close()

    def update_flight_status(self):
        # Updates the status of a flight (for example: Scheduled, Delayed, Cancelled).
        try:
            self.get_connection()
            flight_id = input("Enter FlightID to update: ").strip()
            new_status = input("Enter new Status: ").strip()
            self.cur.execute(self.sql_update_flight_status, (new_status, flight_id))
            self.conn.commit()
            if self.cur.rowcount:
                print("Updated successfully.")
            else:
                print("Cannot find this record in the database")
        except Exception as e:
            print("Error updating flight:", e)
        finally:
            self.close()

    def delete_flight(self):
        # Deletes a flight from the database using its FlightID.
        try:
            self.get_connection()
            flight_id = input("Enter FlightID to delete: ").strip()
            self.cur.execute(self.sql_delete_flight, (flight_id,))
            self.conn.commit()
            if self.cur.rowcount:
                print("Deleted successfully.")
            else:
                print("Cannot find this record in the database")
        except Exception as e:
            print("Error deleting flight:", e)
        finally:
            self.close()

    # ---------- DESTINATION ----------
    def add_destination(self):
        # Adds a new destination to the database.
        try:
            self.get_connection()
            dest_id = input("Enter DestinationID (e.g. DST01): ").strip()
            name = input("Enter Destination Name (e.g. London Heathrow): ").strip()
            country = input("Enter Country: ").strip()
            dest_date = input("Enter DestinationDate (YYYY-MM-DD) or leave blank: ").strip() or None
            city = input("Enter City: ").strip()

            self.cur.execute(self.sql_insert_destination, (dest_id, name, country, dest_date, city))
            self.conn.commit()
            print("Destination added.")
        except Exception as e:
            print("Error adding destination:", e)
        finally:
            self.close()

    def view_destinations(self):
        # Displays all destinations stored in the database.
        try:
            self.get_connection()
            self.cur.execute(self.sql_select_all_destinations)
            rows = self.cur.fetchall()
            if not rows:
                print("No destinations found.")
                return
            for r in rows:
                print(r)
        except Exception as e:
            print("Error viewing destinations:", e)
        finally:
            self.close()

    def update_destination(self):
        # Updates destination information such as name, country, or date.
        try:
            self.get_connection()
            dest_id = input("Enter DestinationID to update: ").strip()
            name = input("New Name: ").strip()
            country = input("New Country: ").strip()
            dest_date = input("New DestinationDate (YYYY-MM-DD) or leave blank: ").strip() or None
            city = input("New City: ").strip()

            self.cur.execute(self.sql_update_destination, (name, country, dest_date, city, dest_id))
            self.conn.commit()
            if self.cur.rowcount:
                print("Destination updated.")
            else:
                print("Destination not found.")
        except Exception as e:
            print("Error updating destination:", e)
        finally:
            self.close()

    # ---------- PILOT–FLIGHT ASSIGNMENT ----------
    def assign_pilot_to_flight(self):
        # Assigns a pilot to a flight by inserting a record
        # into the Assigned table.
        try:
            self.get_connection()
            pilot_id = int(input("Enter PilotID: ").strip())
            flight_id = input("Enter FlightID: ").strip()

            self.cur.execute(self.sql_assign_pilot, (pilot_id, flight_id))
            self.conn.commit()
            print("Pilot assigned to flight.")
        except Exception as e:
            print("Error assigning pilot:", e)
        finally:
            self.close()

    def view_pilot_schedule(self):
        # Displays all flights assigned to a specific pilot.
        try:
            self.get_connection()
            pilot_id = int(input("Enter PilotID: ").strip())
            self.cur.execute(self.sql_view_pilot_schedule, (pilot_id,))
            rows = self.cur.fetchall()
            if not rows:
                print("No schedule found for this pilot.")
                return
            for r in rows:
                print(r)
        except Exception as e:
            print("Error viewing schedule:", e)
        finally:
            self.close()


class FlightInfo:
    # FlightInfo is used to temporarily store flight data
    # entered by the user before it is inserted into the database.

    def __init__(self):
        self.flightID = ""
        self.aircraftID = ""
        self.status = ""
        self.airlineOperator = ""
        self.flightArrivalTime = None
        self.flightDepartureTime = None
        self.destinationID = ""

    def set_flight_id(self, flightID):
        self.flightID = flightID

    def set_aircraft_id(self, aircraftID):
        self.aircraftID = aircraftID

    def set_status(self, status):
        self.status = status

    def set_airline_operator(self, airlineOperator):
        self.airlineOperator = airlineOperator

    def set_arrival_time(self, arrival_time):
        self.flightArrivalTime = arrival_time

    def set_departure_time(self, departure_time):
        self.flightDepartureTime = departure_time

    def set_destination_id(self, destinationID):
        self.destinationID = destinationID

    def as_tuple(self):
        # Converts the flight object into a tuple
        # so it can be used safely in SQL parameterised queries.
        return (
            self.flightID,
            self.aircraftID,
            self.status,
            self.airlineOperator,
            self.flightArrivalTime,
            self.flightDepartureTime,
            self.destinationID,
        )


def main():
    # Displays a menu that allows the user to interact with the system.
    # The program continues running until the user chooses to exit.
    db_ops = DBOperations()

    while True:
        print("\n Menu:")
        print("**********")
        print(" 1. Create tables (Pilot, Destination, Flight, Assigned)")
        print(" 2. Add a New Flight")
        print(" 3. View all Flights")
        print(" 4. Search a Flight (by FlightID)")
        print(" 5. Update Flight Status")
        print(" 6. Delete a Flight")
        print(" 7. Add Destination")
        print(" 8. View Destinations")
        print(" 9. Update Destination")
        print("10. Assign Pilot to Flight")
        print("11. View Pilot Schedule")
        print("12. Exit\n")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            db_ops.create_tables()
        elif choice == 2:
            db_ops.add_new_flight()
        elif choice == 3:
            db_ops.view_all_flights()
        elif choice == 4:
            db_ops.search_flight()
        elif choice == 5:
            db_ops.update_flight_status()
        elif choice == 6:
            db_ops.delete_flight()
        elif choice == 7:
            db_ops.add_destination()
        elif choice == 8:
            db_ops.view_destinations()
        elif choice == 9:
            db_ops.update_destination()
        elif choice == 10:
            db_ops.assign_pilot_to_flight()
        elif choice == 11:
            db_ops.view_pilot_schedule()
        elif choice == 12:
            print("Bye!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()