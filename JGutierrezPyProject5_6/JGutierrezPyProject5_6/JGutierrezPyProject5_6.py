import geocoder

# Forward Geocoding
print("Forward Example")
g = geocoder.komoot('Phoenix, Arizona')
print(g.latlng)
print(g.country)
print("\n")

# Reverse Geocoding
print("Reverse Example")
g = geocoder.arcgis([51.5074, 0.1278], method='reverse')
print(g.city)
print(g.state)
print(g.country)
print("\n")

# IP address 1
print("IP Address Example 1")
g = geocoder.ip('8.8.8.8')
print(g.ip)
print(g.postal)
print(g.latlng)
print(g.city + " " + g.state)
print("\n")

# IP address 2
print("IP Address Example 2")
g = geocoder.ip('me')
print(g.ip)
print(g.postal)
print(g.latlng)
print(g.city + " " + g.state)
print("\n")

# House Address
print("House Address")
g = geocoder.komoot("1600 Pennsylvania Avenue NW, Washington DC")
print(g.housenumber)
print(g.postal)
print(g.street)
print(g.city)
print(g.state)
print(g.country)
print("\n")
