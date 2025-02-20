import folium
from folium.plugins import HeatMap

# Define the thresholds for classification (still relevant if you need classification later)
RED_THRESHOLD = 10
YELLOW_THRESHOLD = 5
BLUE_THRESHOLD = 1

# Extended sample data with more states and locations
crime_data = {
    # Maharashtra
    "Pune (Bibwewadi)": {"count": 12, "coords": [18.4691, 73.8567]},  # Pune
    "Mumbai (Bandra)": {"count": 7, "coords": [19.0595, 72.8305]},   # Mumbai
    "Nagpur (Sadar)": {"count": 3, "coords": [21.1549, 79.0897]},   # Nagpur
    "Nashik (Panchavati)": {"count": 0, "coords": [19.9884, 73.8008]},   # Nashik
    "Aurangabad (CIDCO)": {"count": 15, "coords": [19.9044, 75.3206]},   # Aurangabad
    
    # Gujarat
    "Ahmedabad (Vastrapur)": {"count": 8, "coords": [23.0258, 72.5850]},  # Ahmedabad
    "Surat (City Light)": {"count": 5, "coords": [21.1702, 72.8311]},   # Surat
    "Vadodara (Alkapuri)": {"count": 2, "coords": [22.3039, 73.1822]},   # Vadodara

    # Rajasthan
    "Jaipur (C-Scheme)": {"count": 6, "coords": [26.9124, 75.7873]},  # Jaipur
    "Udaipur (City Palace)": {"count": 4, "coords": [24.5797, 73.7125]},   # Udaipur

    # Delhi
    "New Delhi (Connaught Place)": {"count": 10, "coords": [28.6139, 77.2090]},  # New Delhi
    "Delhi (Hauz Khas)": {"count": 3, "coords": [28.5535, 77.2070]},   # Hauz Khas

    # Uttar Pradesh
    "Lucknow (Hazratganj)": {"count": 7, "coords": [26.8467, 80.9462]},  # Lucknow
    "Noida (Sector 18)": {"count": 5, "coords": [28.5355, 77.3910]},   # Noida
}

# Prepare data for heatmap
heatmap_data = []
for location, data in crime_data.items():
    count = data["count"]
    coords = data["coords"]
    if count > 0:
        heatmap_data.extend([coords] * count)  # Add each location's coordinates multiple times based on the alert count

# Create a folium map centered at India (adjust as needed)
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered at India

# Add heatmap to the map
HeatMap(heatmap_data).add_to(m)

# Save the map as an HTML file
m.save("india_heatmap.html")

# Display the map (if running in a Jupyter Notebook or compatible environment)
m
