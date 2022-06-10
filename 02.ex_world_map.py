import pandas as pd
import matplotlib
import locale
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio
import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
starbucks_locations = pd.read_csv(r"C:*directory.csv")


citywise_geo_data = starbucks_locations.groupby("City").mean()[["Longitude","Latitude"]]
citywise_store_cnts = starbucks_locations.groupby("City").count()[["Store Number"]].rename(columns={"Store Number":"Count"})
citywise_store_cnts = citywise_geo_data.join(citywise_store_cnts).sort_values(by=["Count"], ascending=False)
citywise_store_cnts = citywise_store_cnts[citywise_store_cnts["Count"]>10]


with plt.style.context(("seaborn", "ggplot")):
    world.plot(figsize=(18,10),
               color="white",
               edgecolor = "grey");

plt.scatter(citywise_store_cnts.Longitude, citywise_store_cnts.Latitude, s=citywise_store_cnts.Count, color="green", alpha=0.5)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Strabucks Store Locations On Earth");



#############

with plt.style.context(("seaborn", "ggplot")):
    world.plot(figsize=(18,10),
               color="white",
               edgecolor = "grey");

plt.scatter(starbucks_locations.Longitude, starbucks_locations.Latitude, s=15, color="red", alpha=0.3)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Strabucks Store Locations On Earth");

plt.show()





with plt.style.context(("seaborn", "ggplot")):
    world.plot(figsize=(18,10),
               color="white",
               edgecolor = "grey");

plt.scatter(citywise_store_cnts.Longitude, citywise_store_cnts.Latitude, s=citywise_store_cnts.Count, color="green", alpha=0.5)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Strabucks Store Locations On Earth");
plt.show()
