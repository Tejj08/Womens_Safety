import folium

# Define the thresholds for classification
RED_THRESHOLD = 10
YELLOW_THRESHOLD = 5
BLUE_THRESHOLD = 1

# Sample data: Dictionary with location names, number of alerts, and their coordinates (latitude, longitude)
crime_data = {
    "Pune (Bibwewadi)": {"count": 12, "coords": [18.4691, 73.8567]},  # Example coordinates for Bibwewadi, Pune
    "Mumbai (Bandra)": {"count": 7, "coords": [19.0595, 72.8305]},   # Example coordinates for Bandra, Mumbai
    "Nagpur (Sadar)": {"count": 3, "coords": [21.1549, 79.0897]},   # Example coordinates for Sadar, Nagpur
    "Nashik (Panchavati)": {"count": 0, "coords": [19.9884, 73.8008]},   # Example coordinates for Panchavati, Nashik
    "Aurangabad (CIDCO)": {"count": 15, "coords": [19.9044, 75.3206]},   # Example coordinates for CIDCO, Aurangabad
}

# Function to classify each location based on the number of alerts
def classify_hotspots(crime_data):
    classification = {}
    for location, data in crime_data.items():
        count = data["count"]
        if count >= RED_THRESHOLD:
            classification[location] = {"classification": "Red (High-Risk)", "color": "red"}
        elif count >= YELLOW_THRESHOLD:
            classification[location] = {"classification": "Yellow (Moderate-Risk)", "color": "orange"}  # Use "orange" for yellow
        elif count >= BLUE_THRESHOLD:
            classification[location] = {"classification": "Blue (Low-Risk)", "color": "blue"}
        else:
            classification[location] = {"classification": "Green (Safest)", "color": "green"}
    return classification

# Classify the locations
classified_locations = classify_hotspots(crime_data)

# Create a folium map centered at Maharashtra (adjust as needed)
m = folium.Map(location=[19.7515, 75.7139], zoom_start=6)  # Centered at Maharashtra

# Add markers to the map
for location, info in classified_locations.items():
    folium.Marker(
        location=crime_data[location]["coords"],
        popup=f"{location}: {info['classification']}",
        icon=folium.Icon(color=info["color"])
    ).add_to(m)

# Save the map as an HTML file
m.save("maharashtra_hotspot_map.html")

# Display the map (if running in a Jupyter Notebook or compatible environment)
m
