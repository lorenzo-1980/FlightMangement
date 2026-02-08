import sqlite3
import os

DB_NAME = "FlightManagement.db"

print("Using DB:", os.path.abspath(DB_NAME))

conn = sqlite3.connect(DB_NAME)

# Update FL001 departure time

conn.execute("UPDATE flight " "SET FlightDepartureTime = '00:00' " "WHERE FlightID = 'FL001'"
)
conn.commit()

print("Updated Departure Time:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL001'"):
 print(row)

# Update FL002 departure time

 conn.execute("UPDATE flight " "SET FlightDepartureTime = '10:00' " "WHERE FlightID = 'FL002'"
)
conn.commit()

print("Departure Time")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL001'"):
 print(row)

# Update FL003 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '09:15' " "WHERE FlightID = 'FL003'")
conn.commit()

print("Departure Time:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL003'"):
    print(row)


# Update FL004 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '12:45' " "WHERE FlightID = 'FL004'")
conn.commit()

print("Departure Time:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL004'"):
    print(row)


# Update FL005 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '18:30' " "WHERE FlightID = 'FL005'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL005'"):
    print(row)


# Update FL006 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '14:10' " "WHERE FlightID = 'FL006'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL006'"):
    print(row)


# Update FL007 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '07:50' " "WHERE FlightID = 'FL007'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL007'"):
    print(row)


# Update FL008 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '16:20' " "WHERE FlightID = 'FL008'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL008'"):
    print(row)


# Update FL009 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '21:00' " "WHERE FlightID = 'FL009'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL009'"):
    print(row)


# Update FL010 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '06:40' " "WHERE FlightID = 'FL010'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL010'"):
    print(row)


# Update FL011 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '08:55' " "WHERE FlightID = 'FL011'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL011'"):
    print(row)


# Update FL012 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '19:35' " "WHERE FlightID = 'FL012'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL012'"):
    print(row)


# Update FL013 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '22:15' " "WHERE FlightID = 'FL013'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL013'"):
    print(row)


# Update FL014 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '11:25' " "WHERE FlightID = 'FL014'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL014'"):
    print(row)


# Update FL015 departure time
conn.execute("UPDATE flight " "SET FlightDepartureTime = '13:50' " "WHERE FlightID = 'FL015'")
conn.commit()

print("Updated row:")
for row in conn.execute("SELECT FlightID, FlightDepartureTime FROM flight WHERE FlightID = 'FL015'"):
    print(row)

conn.close()