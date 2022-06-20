import sys
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
italy = gpd.read_file(r"C:\Users\sina.kian\Desktop\Antonio\shp\reg2011_g.shp")
df =pd.read_excel(r"C:\Users\sina.kian\Desktop\Ricardo\updates\DataBase_5_final.xlsx")
dp=pd.read_excel(r"C:\Users\sina.kian\Desktop\Antonio\it.xlsx")


world.crs
italy.crs

italy=italy.to_crs(epsg=4326)
##@@
df=df[df.columns[1:]]
df['map_color']=['white']*len(df)
for i in df.index:
    if df['Earthquake Zone'][i]==0:
        df['map_color'][i]='Green'
    elif df['Earthquake Zone'][i]==1:
        df['map_color'][i]='yellow'
    elif df['Earthquake Zone'][i]==2:
        df['map_color'][i]='orange'
    elif df['Earthquake Zone'][i]==3:
        df['map_color'][i]='red'

##@@
for i in italy.index:
    italy['NOME_REG'][i]=italy['NOME_REG'][i].capitalize()

italy['NOME_REG'][1]='Aosta'
italy['NOME_REG'][7]='Emilia-Romagna'
italy['NOME_REG'][3]='Trentino'
italy['NOME_REG'][5]='Friuli-Venezia Giulia'
##@@
cmap = matplotlib.cm.Blues(np.linspace(0,1,40))
CCC= cmap[4]
with plt.style.context(("seaborn", "ggplot")):
    ax=italy.plot(figsize=(18,10),
               color=CCC,
               edgecolor = "grey");


ax.scatter(df['Longitude'], df['Latitude'], marker="o", color=df['map_color'], alpha=0.7, zorder=5, s=10)
#green_patch = mpatches.Patch(color='green', label='0')
green_patch = Line2D([0], [0], marker='o', color='w', label='0',
                        markerfacecolor='g', markersize=7)
yellow_patch = Line2D([0], [0], marker='o', color='w', label='1',
                        markerfacecolor='yellow', markersize=7)
orange_patch = Line2D([0], [0], marker='o', color='w', label='2',
                        markerfacecolor='orange', markersize=7)
red_patch = Line2D([0], [0], marker='o', color='w', label='3',
                        markerfacecolor='red', markersize=7)
plt.legend(handles=[green_patch,yellow_patch, orange_patch, red_patch])


plt.title("Ubicazione di Hotel - zona terremoto");
leg = ax.get_legend()
leg.set_title('Zona terremoto')
ax.set_axis_off()
fig = plt.gcf()
fig.tight_layout()
plt.tight_layout()
fname='plt01.png'
fig.savefig(bbox_inches='tight',fname=fname)
plt.close('all')
