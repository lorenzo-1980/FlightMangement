import sqlite3
conn = sqlite3.connect("FlightManagement.db")


# Counts number of flights per destination

print("Number of flights per destination:")

for row in conn.execute("""
SELECT 
    d.DestinationID,
    d.Name,
    COUNT(f.FlightID) AS NumberOfFlights
FROM destination d
LEFT JOIN flight f ON d.DestinationID = f.DestinationID
GROUP BY d.DestinationID, d.Name
ORDER BY d.DestinationID
"""):
    print(row)



# Counts number of pilots assigned for each flight

print("\nNumber of pilots assigned to each flight:")

for row in conn.execute("""
SELECT 
    f.FlightID,
    COUNT(fp.PilotID) AS NumberOfPilots
FROM flight f
LEFT JOIN flight_pilot fp ON f.FlightID = fp.FlightID
GROUP BY f.FlightID
ORDER BY f.FlightID
"""):
    print(row)

conn.close()