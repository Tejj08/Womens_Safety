import folium
from folium.plugins import HeatMap
import pandas as pd

# Load data from Excel file using pandas
# Make sure the Excel file has columns: 'Location', 'Count', 'Latitude', 'Longitude'
excel_data = pd.read_excel('crime.xlsx')

# Prepare data for heatmap from the Excel file
heatmap_data = []
for index, row in excel_data.iterrows():
    count = row['Count']
    coords = [row['Latitude'], row['Longitude']]
    if count > 0:
        heatmap_data.extend([coords] * count)  # Add each location's coordinates multiple times based on the alert count

# Create a folium map centered at India (adjust as needed)
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered at India

# Add heatmap to the map
HeatMap(heatmap_data).add_to(m)

# Save the map as an HTML file
m.save("Inidaa'sMap.html")

# Display the map (if running in a Jupyter Notebook or compatible environment)
m
