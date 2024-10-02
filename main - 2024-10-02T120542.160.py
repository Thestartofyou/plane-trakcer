import requests
import json
import time

# OpenSky Network API base URL
API_URL = "https://opensky-network.org/api/states/all"

def get_planes_data():
    # Fetch plane data from OpenSky Network
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data['states']
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None

def track_planes():
    while True:
        # Get current planes' data
        planes = get_planes_data()
        
        if planes:
            print(f"{len(planes)} planes in the air right now:")
            for plane in planes[:10]:  # Display the first 10 planes
                icao24 = plane[0]  # ICAO 24-bit address
                callsign = plane[1]  # Call sign
                country = plane[2]  # Country of origin
                altitude = plane[7]  # Altitude in meters
                velocity = plane[9]  # Velocity in m/s
                lat = plane[6]  # Latitude
                lon = plane[5]  # Longitude
                
                print(f"Plane {icao24} ({callsign}) from {country} is at {altitude}m, velocity: {velocity}m/s, location: ({lat}, {lon})")
                
        else:
            print("No data available")
        
        # Wait for a minute before getting the data again
        time.sleep(60)

if __name__ == "__main__":
    track_planes()
