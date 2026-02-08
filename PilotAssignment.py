import sqlite3
conn = sqlite3.connect("FlightManagement.db")
conn.execute("PRAGMA foreign_keys = ON")

# Safe assign (won’t duplicate if you run again)
conn.execute(
    "INSERT OR IGNORE INTO flight_pilot (FlightID, PilotID, Role) "
    "VALUES ('FL001', 1, 'Captain')"
)
conn.commit()

print("Assigned:")
for row in conn.execute(
    "SELECT FlightID, PilotID, Role FROM flight_pilot WHERE FlightID = 'FL001' AND PilotID = 1"
):
    print(row)


conn.execute(
    "INSERT OR IGNORE INTO flight_pilot (FlightID, PilotID, Role) "
    "VALUES ('FL001', 2, 'First Officer')"
)
conn.commit()

print("Assigned:")
for row in conn.execute(
    "SELECT FlightID, PilotID, Role FROM flight_pilot WHERE FlightID = 'FL001' AND PilotID = 2"
):
    print(row)


conn.execute(
    "INSERT OR IGNORE INTO flight_pilot (FlightID, PilotID, Role) "
    "VALUES ('FL002', 3, 'Captain')"
)
conn.commit()

print("Assigned:")
for row in conn.execute(
    "SELECT FlightID, PilotID, Role FROM flight_pilot WHERE FlightID = 'FL002' AND PilotID = 3"
):
    print(row)


conn.execute(
    "INSERT OR IGNORE INTO flight_pilot (FlightID, PilotID, Role) "
    "VALUES ('FL002', 4, 'First Officer')"
)
conn.commit()

print("Assigned:")
for row in conn.execute(
    "SELECT FlightID, PilotID, Role FROM flight_pilot WHERE FlightID = 'FL002' AND PilotID = 4"
):
    print(row)

print("\nPilot schedule (PilotID = 1):")
for row in conn.execute("""
SELECT 
    p.PilotID,
    p.Name,
    fp.FlightID,
    f.Status,
    f.FlightDepartureTime,
    f.FlightArrivalTime,
    d.City,
    fp.Role
FROM pilot p
JOIN flight_pilot fp ON p.PilotID = fp.PilotID
JOIN flight f ON fp.FlightID = f.FlightID
JOIN destination d ON f.DestinationID = d.DestinationID
WHERE p.PilotID = 1
ORDER BY f.FlightDepartureTime
"""):
    print(row)


print("\nPilot schedule (PilotID = 2):")
for row in conn.execute("""
SELECT 
    p.PilotID,
    p.Name,
    fp.FlightID,
    f.Status,
    f.FlightDepartureTime,
    f.FlightArrivalTime,
    d.City,
    fp.Role
FROM pilot p
JOIN flight_pilot fp ON p.PilotID = fp.PilotID
JOIN flight f ON fp.FlightID = f.FlightID
JOIN destination d ON f.DestinationID = d.DestinationID
WHERE p.PilotID = 2
ORDER BY f.FlightDepartureTime
"""):
    print(row)

print("\nPilot schedule (PilotID = 3):")
for row in conn.execute("""
SELECT 
    p.PilotID,
    p.Name,
    fp.FlightID,
    f.Status,
    f.FlightDepartureTime,
    f.FlightArrivalTime,
    d.City,
    fp.Role
FROM pilot p
JOIN flight_pilot fp ON p.PilotID = fp.PilotID
JOIN flight f ON fp.FlightID = f.FlightID
JOIN destination d ON f.DestinationID = d.DestinationID
WHERE p.PilotID = 3
ORDER BY f.FlightDepartureTime
"""):
    print(row)
print("\nPilot schedule (PilotID = 4):")
for row in conn.execute("""
SELECT 
    p.PilotID,
    p.Name,
    fp.FlightID,
    f.Status,
    f.FlightDepartureTime,
    f.FlightArrivalTime,
    d.City,
    fp.Role
FROM pilot p
JOIN flight_pilot fp ON p.PilotID = fp.PilotID
JOIN flight f ON fp.FlightID = f.FlightID
JOIN destination d ON f.DestinationID = d.DestinationID
WHERE p.PilotID = 4
ORDER BY f.FlightDepartureTime
"""):
    print(row)

conn.close()