import sqlite3

conn = sqlite3.connect("FlightManagement.db")


print("Delayed flights:")
print ("Loading...")
for row in conn.execute(
    "SELECT d.Name, d.City, f.AirlineOperator, f.FlightDepartureTime, f.Status "
    "FROM flight f "
    "JOIN destination d ON f.DestinationID = d.DestinationID "
    "WHERE f.Status = 'Delayed'"
):
    print(row)


print("Inbound flights:")
print ("Loading...")
for row in conn.execute(
    "SELECT d.Name, d.City, f.AirlineOperator, f.FlightDepartureTime, f.Status "
    "FROM flight f "
    "JOIN destination d ON f.DestinationID = d.DestinationID "
    "WHERE f.Status = 'Scheduled'"
):
    print(row)


print("Boarding flights:")
print ("Loading...")
for row in conn.execute(
    "SELECT d.Name, d.City, f.AirlineOperator, f.FlightDepartureTime, f.Status "
    "FROM flight f "
    "JOIN destination d ON f.DestinationID = d.DestinationID "
    "WHERE f.Status = 'Boarding'"
):
    print(row)


print("Cancelled flights:")
print ("Loading...")
for row in conn.execute(
    "SELECT d.Name, d.City, f.AirlineOperator, f.FlightDepartureTime, f.Status "
    "FROM flight f "
    "JOIN destination d ON f.DestinationID = d.DestinationID "
    "WHERE f.Status = 'Cancelled'"
):
    print(row)


conn.close()