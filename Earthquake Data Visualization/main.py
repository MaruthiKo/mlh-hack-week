# Earthquake Data Visualization


# Data Source -> https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv 

# Importing Libraries
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def extract_subarea(place):
    return place[0]

def extract_area(place):
    return place[-1]

# Fetch Data and clean it
def fetch_eq_data(period= 'daily', region="Worldwide", min_mag=1):
    # data source
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{}.csv"

    if period == "weekly":
        new_url = url.format('all_week')
    elif period == "monthly":
        new_url = url.format('all_month')
    else:
        new_url = url.format('all_day')

    # fetch data
    df_earthquake = pd.read_csv(new_url)
    df_earthquake = df_earthquake[["time", "latitude","longitude", "mag", "place"]]

    # Extract sub-area in place data
    place_list = df_earthquake['place'].str.split(", ")
    df_earthquake["sub_area"] = place_list.apply(extract_subarea)
    df_earthquake["area"] = place_list.apply(extract_area)
    df_earthquake = df_earthquake.drop(columns=["place"], axis=1)

    # Filter data based on min_threshold
    if isinstance(min_mag, int) and min_mag > 0:
        df_earthquake = df_earthquake[df_earthquake["mag"] >= min_mag]
    else:
        df_earthquake = df_earthquake[df_earthquake["mag"] > 0]

    # Convert 'time' to pd datetime 
    df_earthquake["time"] = pd.to_datetime(df_earthquake['time'])
# Create Visualizer