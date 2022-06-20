#finding the address and giving the coordinates
import pandas as pd
import math
from functools import partial
from geopy.geocoders import Nominatim
def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False

geolocator=Nominatim(user_agent="googleearth")
geocode=partial(geolocator.geocode,language="en")
dff = pd.read_excel(r"C:\Users\sina.kian\Desktop\Antonio\Input.xlsx")

df=dff.iloc[:160]
Ad=[]
for i in range(0,len(df)):
    if not isnan(df['Country_ISOCode'][i]):
        A=str(df['Country_ISOCode'][i])

    if not isnan(df['City'][i]):
        A=A+', '+str(df['City'][i])

    if not isnan(df['Street'][i]):
        A=A+', '+str(df['Street'][i])

    Ad.append(A)

Longi=[]
Lati=[]
le=[]
tr=[]
C=1
for i in Ad:
    print(C)
    C+=1
    location=geolocator.geocode(i)  #location=geolocator.geocode(i,timeout=10)
    le.append(len(i))
    t=0
    while location is None:
        if len(i)>5:
            i=i[0:len(i)-1]
            t+=1
            location=geolocator.geocode(i)
        else:
            Longi.append(0)
            Lati.append(0)
    else:
        tr.append(t)
        Longi.append(location.longitude)
        Lati.append(location.latitude)

dg=pd.DataFrame()
dg['Adress']=Ad
dg["Longi"]=Longi
dg["Lati"]=Lati
dg["precision"]=[(x1 - x2)/x1 for (x1, x2) in zip(le, tr)]
dg["Length"]=le
dg["number of tries"]=tr

file_name='victoryha.xlsx'
dg.to_excel(file_name)
