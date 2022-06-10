import pandas as pd
import matplotlib
import locale
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio
import geopandas as gpd

locale.setlocale(locale.LC_ALL, 'it_IT')
matplotlib.style.use('seaborn')


df = pd.read_excel(r"* - Sina.xlsx",sheet_name=None)

df1=df['1a.Prodotti_Venduti ']
df1.columns=df1.loc[7]
df1=df1[8:]
df1.index=range(0,len(df1))
df1.columns=['del1',
             'Tipologia di prodotto',
                   'Linea Prodotto',
           'Qualifica dell\'azienda',
             'Produzione propria %',
'Commercializzazione di prodotti di terzi %',
               'Settori di impiego',
                          'valore ',
                             'u.m.',
                           'Italia',
                               'UE',
                     'Resto Europa',
                     'Estero no UE',
                      'USA, Canada',
                           'Totale',
                         'Impianto',
                         'del2',
                      'Codice IPPC',
                         'Prodotto',
                    'Anno 2015 (t)',
                    'Anno 2016 (t)',
                    'Anno 2017 (t)',
                    'Anno 2018 (t)',
                    'Anno 2019 (t)',
                    'Anno 2020 (t)',
                    'del3',
                         'Prodotto R',
                     'Destinazione',
                    'Anno 2015 (t) R',
                    'Anno 2016 (t) R',
                    'Anno 2017 (t) R',
                    'Anno 2018 (t) R',
                    'Anno 2019 (t) R',
                    'Anno 2020 (t) R']

df11=df1[['Tipologia di prodotto',
           'Linea Prodotto',
           'Qualifica dell\'azienda',
           'Produzione propria %',
           'Commercializzazione di prodotti di terzi %',
           'Settori di impiego',
                  'valore ',
                     'u.m.',
                   'Italia',
                       'UE',
             'Resto Europa',
             'Estero no UE',
              'USA, Canada',
                   'Totale',
                 'Impianto']]

dn11=df11.copy()
for i in df11.columns:
    for j in df11[i].index:
        try:
            dn11[i][j]=locale.format_string('%10.2f', df11[i][j], grouping=True)
        except:
            dn11[i][j]=df11[i][j]

df12=df1[['Codice IPPC',
           'Prodotto',
        'Anno 2015 (t)',
        'Anno 2016 (t)',
        'Anno 2017 (t)',
        'Anno 2018 (t)',
        'Anno 2019 (t)',
        'Anno 2020 (t)']]

df12=df12[:5]

dn12=df12.copy()
for i in df12.columns:
    for j in df12[i].index:
        try:
            dn12[i][j]=locale.format_string('%10.2f', df12[i][j], grouping=True)
        except:
            dn12[i][j]=df12[i][j]

df13=df1[['Prodotto R',
            'Destinazione',
           'Anno 2015 (t) R',
           'Anno 2016 (t) R',
           'Anno 2017 (t) R',
           'Anno 2018 (t) R',
           'Anno 2019 (t) R',
           'Anno 2020 (t) R']]

df13=df13[:3]
df13.columns=[['Prodotto',
               'Destinazione',
               'Anno 2015 (t)',
               'Anno 2016 (t)',
               'Anno 2017 (t)',
               'Anno 2018 (t)',
               'Anno 2019 (t)',
               'Anno 2020 (t)']]

dn13=df13.copy()
for i in df13.columns:
    for j in df13[i].index:
        try:
            dn13[i][j]=locale.format_string('%10.2f', df13[i][j], grouping=True)
        except:
            dn13[i][j]=df13[i][j]

plt.close('all')
############################# PLOTS:
#### plt1 : df11 dn11
x=[1,2,3,4,5,6,7,8,9]
y=df11['valore ']
plt.figure(1)#,figsize=(10, 6))
mybars=plt.bar(x,y,width=0.4)
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
x_ax=plt.gca().xaxis
for item in x_ax.get_ticklabels():
    item.set_rotation(90)

for bari in mybars:
    height = bari.get_height()
    if height>5000:
        plt.gca().text(bari.get_x() + bari.get_width()/2,  bari.get_height()-5700, locale.format_string('%10.2f', (int(height)), grouping=True),
                     ha='center', color='w', fontsize=10, rotation=90, weight='bold')
    else:
        plt.gca().text(bari.get_x() + bari.get_width()/2,  bari.get_height(), locale.format_string('%10.2f', (int(height)), grouping=True),
                     ha='center', color='k', fontsize=10, rotation=90, weight='bold')

fig = plt.gcf()
fig.tight_layout()
plt.tight_layout()
ax=plt.gca()
ax.set_xlabel('Tipologia di prodotto', weight='bold')
ax.set_ylabel('Valori [t]')
ax.set_title('Quantità vendute [t] di ogni tipologia di prodotto 2020')
#axes = plt.axes()
#axes.set_xticklabels(['fabbricato','contenuti', 'Ricorso Terzi', 'Cristalli','Furto', 'Merci Refrigerazione'])
plt.xticks(x,('Biostimolanti\nper agricoltura','Gesso di\ndefecazione', 'Grasso per\nbiocombustibili', 'Ritardante\nper gesso','Altri', 'Idrolizzato\nproteico da\ncarniccio', 'Idrolizzato\nproterico da\nrasatura tutto\nusato da Arzignano', 'un prodotto\ntecnico', 'solfato di\nammonio al 38%'))
#plt.legend(['Valori', 'Terremoto', 'Inondazione, Alluvione, Allagamento', 'Terrorismo', 'Eventi Socio Politici, Atti Dolosi' ],loc=1,frameon=False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.gca().axes.yaxis.set_visible(False)
plt.gca().tick_params(axis='both', which='both', length=0)

fname='plt01.png'
fig.savefig(bbox_inches='tight',fname=fname)

#### plt2 : df11 dn11
x_t=['Italia', 'UE',
       'Estero no UE', 'USA, Canada']
x=[1,2,3,4]
plt.figure(2)
for i in [0,2,3,4]:
    y=df11[x_t].loc[i]
    y=y.fillna(0)
    y=y*1000
    #print(x,'11111111111111111111111111111111')
    mybars=plt.bar(x,y,width=0.2)
    plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
    #x_ax=plt.gca().xaxis
    #for item in x_ax.get_ticklabels():
    #    item.set_rotation(90)
    for bari in mybars:
        height = bari.get_height()
        if height>4000000:
            plt.gca().text(bari.get_x() + bari.get_width()/2,  bari.get_height()-4000000, locale.format_string('%10.0f', (int(height)), grouping=True),
                         ha='center', color='w', fontsize=10, rotation=90, weight='bold')
        else:
            plt.gca().text(bari.get_x() + bari.get_width()/2,  bari.get_height(), locale.format_string('%10.0f', (int(height)), grouping=True),
                         ha='center', color='k', fontsize=10, rotation=90, weight='bold')
    for j in range(0,len(x)):
        x[j]+=0.2
        print(x,'11111111111111111111111111111111')



fig = plt.gcf()
fig.tight_layout()
plt.tight_layout()
ax=plt.gca()
ax.set_xlabel('Regione Del Mondo', weight='bold')
ax.set_ylabel('Valori [€]')
ax.set_title('Fatturato [€] di ogni regione del mondo 2020')
#axes = plt.axes()
#axes.set_xticklabels(['fabbricato','contenuti', 'Ricorso Terzi', 'Cristalli','Furto', 'Merci Refrigerazione'])
plt.legend(['Biostimolanti\nper agricoltura','Grasso per\nbiocombustibili', 'Ritardante\nper gesso','Altri'],loc=1,frameon=False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.gca().axes.yaxis.set_visible(False)
plt.gca().tick_params(axis='both', which='both', length=0)
ax.set_xticks([1.3,2.3,3.3,4.3])
ax.set_xticklabels(['Italia', 'UE','Estero no UE', 'USA, Canada'])
fname='plt02.png'
fig.savefig(bbox_inches='tight',fname=fname)

#### plt3 : df12 dn12
x=df12.columns[2:]
xx=['2015','2016','2017','2018','2019','2020']
plt.figure(3)
for i in [0,1,2,3,4]:
    yy=dn12[x].loc[i]
    y=df12[x].loc[i]
    plt.plot(xx,y,'o-',linewidth=3)
    for xp,yp,yyp in zip(xx,y,yy):
        label = yyp
        plt.annotate(label, # this is the text
                     (xp,yp), # these are the coordinates to position the label
                     textcoords="offset points", # how to position the text
                     xytext=(0,-10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center

ax=plt.gca()
ax.set_xlabel('anno')
ax.set_title('Produzione annua stabilimento di Arzignano [t]')
plt.gca().axes.yaxis.set_visible(False)
plt.legend(['Grasso','Correttivo\ncalcico', 'Idrolizzato\nproteico da\ncamiccio','Fertilizzanti\nsemplici\no composti' ,'Settore\nindustriale'],bbox_to_anchor=(1.04,1), loc="upper left",frameon=False)
#'Fertilizzanti\na base di\nfosforo, azoto,\npotassio, semplici\no composti'
fig = plt.gcf()
fig.tight_layout()
plt.tight_layout()
fname='plt03.png'
fig.savefig(bbox_inches='tight',fname=fname)
#### plt32 : df12 dn12
x=df12.columns[2:]
xx=['2015','2016','2017','2018','2019','2020']
plt.figure(4)
for i in [0,1,2,3,4]:
    yy=dn12[x].loc[i]
    y=df12[x].loc[i]
    plt.plot(xx,y,'o-',linewidth=3)

ax=plt.gca()
ax.set_xlabel('anno')
ax.set_ylabel('tonnelate')
ax.set_title('Produzione annua stabilimento di Arzignano [t]')
plt.legend(['Grasso','Correttivo\ncalcico', 'Idrolizzato\nproteico da\ncamiccio','Fertilizzanti\nsemplici\no composti' ,'Settore\nindustriale'],bbox_to_anchor=(1.04,1), loc="upper left",frameon=False)
#'Fertilizzanti\na base di\nfosforo, azoto,\npotassio, semplici\no composti'
fig = plt.gcf()
fig.tight_layout()
plt.tight_layout()
fname='plt03_2.png'
fig.savefig(bbox_inches='tight',fname=fname)
#### plt4 : df13 dn13
x=df13.columns[2:]
xx=['2015','2016','2017','2018','2019','2020']
plt.figure(5)
for i in [0,1,2]:
    yy=dn13[x].loc[i]
    y=df13[x].loc[i]
    plt.plot(xx,y,'o-',linewidth=3)
    for xp,yp,yyp in zip(xx,y,yy):
        label = yyp
        plt.annotate(label, # this is the text
                     (xp,yp), # these are the coordinates to position the label
                     textcoords="offset points", # how to position the text
                     xytext=(0,-10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center

ax=plt.gca()
ax.set_xlabel('anno')
ax.set_title('Produzione annua stabilimento di Chiampo [t]')
plt.gca().axes.yaxis.set_visible(False)
plt.legend(['Idrolizzato\nproteico da\nrasatura','prodotto tecnico\ncommercializzato' ,'solfato di\nammonio\n al 38%'],bbox_to_anchor=(1.04,1), loc="upper left",frameon=False)
#'Fertilizzanti\na base di\nfosforo, azoto,\npotassio, semplici\no composti'
fig = plt.gcf()
fig.tight_layout()
plt.tight_layout()
fname='plt04.png'
fig.savefig(bbox_inches='tight',fname=fname)
#### plt42 : df13 dn13
x=df13.columns[2:]
xx=['2015','2016','2017','2018','2019','2020']
plt.figure(6)
for i in [0,1,2]:
    yy=dn13[x].loc[i]
    y=df13[x].loc[i]
    plt.plot(xx,y,'o-',linewidth=3)

ax=plt.gca()
ax.set_xlabel('anno')
ax.set_ylabel('tonnelate')
ax.set_title('Produzione annua stabilimento di Chiampo [t]')
plt.legend(['Idrolizzato\nproteico da\nrasatura','prodotto tecnico\ncommercializzato' ,'solfato di\nammonio\n al 38%'],bbox_to_anchor=(1.04,1), loc="upper left",frameon=False)
#'Fertilizzanti\na base di\nfosforo, azoto,\npotassio, semplici\no composti'
fig = plt.gcf()
fig.tight_layout()
plt.tight_layout()
fname='plt04_2.png'
fig.savefig(bbox_inches='tight',fname=fname)
#### plt5 : dgg
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
cities = gpd.read_file(geopandas.datasets.get_path('naturalearth_cities'))
dg=df11[df11.columns[8:-2]]
dg=dg[['Italia', 'UE','Estero no UE', 'USA, Canada']]
dg=dg.loc[[0,2,3,4]].fillna(0)
dg.loc['Total'] = pd.Series(dg[['Italia', 'UE','Estero no UE', 'USA, Canada']].sum(), index = ['Italia', 'UE','Estero no UE', 'USA, Canada'])
cc=['ITA','FRA', 'CHN' ,'USA']
dgg=dg.loc['Total']
dgg=dgg.to_frame().reset_index()
dgg['index']=cc
import plotly.express as px
fig = px.scatter_geo(dgg, locations='index', color=dg.columns,
                     hover_name='index', size="Total",)
                     #projection="natural earth")
#fig = px.scatter_mapbox(data, lat="latitude", lon="longitude",color="room_type", size="price",
                  #color_continuous_scale=px.colors.cyclical.IceFire, size_max=20,zoom=12)
#fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

pio.write_image(fig, 'plt5.png', format='png', width=1500, height=700)
#### plt51 : dgg
matplotlib.style.use('default')

cc=['Rome','Paris', 'Beijing' ,'Washington, D.C.']
ind=[]
for i in cc:
    ind.append(cities[cities['name']==i].index[0])

mycities=cities.loc[ind]


#ax=mycities.plot(marker='o',color='red',markersize=dgg['Total']*.005)
#world.plot(ax=ax,alpha=0.4, edgecolor='white', linewidth=2)
ax=world.plot(alpha=0.4, edgecolor='white', linewidth=1.5, figsize=(16,8))
ax.set_axis_off()
fname='plt05_1.png'
plt.savefig(fname=fname)
#### plt6 : df111
df111=df11[['Tipologia di prodotto' ,'valore ']]
df111=df111[df111['valore ']!=0]
df111=df111.loc[[0,1,2,3,8]]
#x=df111['Tipologia di prodotto']
x=[ 'Biostimolanti\nper agricoltura', 'Gesso di\ndefecazione', ' Grasso per\nbiocombustibili', 'Ritardante\nper gesso', 'solfato di\nammonio al 38%' ]
y=df111['valore ']
#yy=y[y!=0]

#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:5]

#create pie chart
plt.pie(y, labels = x, colors = colors, autopct='%.0f%%')
fname='plt06.png'
plt.savefig(fname=fname)

colors = sns.color_palette('bright')[0:5]
_, _, autotexts=plt.pie(y, labels = x, colors = colors, autopct='%.0f%%')

for autotext in autotexts:
    autotext.set_color('white')

fname='plt06_1.png'
plt.savefig(fname=fname)
plt.close('all')
#### plt7 : df12
matplotlib.style.use('seaborn')
x_t=['Italia', 'UE',
       'Estero no UE', 'USA, Canada']
x=[1,2,3,4]
plt.figure(2)
SHT=pd.Series([0,0,0,0])
PBar=[]
yy=[0,0,0,0]
for i in [0,2,3,4]:
    y=df11[x_t].loc[i]
    y=y.fillna(0)
    y=y*1000
    #print(x,'11111111111111111111111111111111')
    print(yy)
    mybars=plt.bar(x,y,width=0.2,bottom=yy)
    if i==0:
        for bari in mybars:
            PBar.append(bari.get_x())
    yy+=y
    plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
    #x_ax=plt.gca().xaxis
    #for item in x_ax.get_ticklabels():
    #    item.set_rotation(90)
    HT=[]
    for bari in mybars:
        height = bari.get_height()
        HT.append(height)
    SHT+=HT

for i,j in zip(SHT.to_list(),PBar):
    plt.gca().text(j-.08, 589480.0 , 'Total = '+locale.format_string('%10.0f', (int(i)), grouping=True),
                    ha='center', color='k', fontsize=10, rotation=90, weight='bold')

plt.legend(['Biostimolanti\nper agricoltura','Grasso per\nbiocombustibili', 'Ritardante\nper gesso','Altri'],loc=1,frameon=False)
fig = plt.gcf()
fig.tight_layout()
plt.tight_layout()
ax=plt.gca()
ax.set_xlabel('Regione Del Mondo', weight='bold')
ax.set_ylabel('Valori [€]')
ax.set_title('Fatturato [€] di ogni regione del mondo 2020')
#axes = plt.axes()
#axes.set_xticklabels(['fabbricato','contenuti', 'Ricorso Terzi', 'Cristalli','Furto', 'Merci Refrigerazione'])
plt.legend(['Biostimolanti\nper agricoltura','Grasso per\nbiocombustibili', 'Ritardante\nper gesso','Altri'],loc=1,frameon=False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.gca().axes.yaxis.set_visible(False)
plt.gca().tick_params(axis='both', which='both', length=0)
ax.set_xticks([1,2,3,4])
ax.set_xticklabels(['Italia', 'UE','Estero no UE', 'USA, Canada'])
fname='plt07.png'
fig.savefig(bbox_inches='tight',fname=fname)









import geopandas as gpd
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cmap = mpl.cm.Greens(np.linspace(0,1,40))
cmap = mpl.colors.ListedColormap(cmap[4:,:-1])




world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
cities = gpd.read_file(gdp.datasets.get_path('naturalearth_cities'))


WW=world.copy()
WW=WW[['continent', 'name', 'iso_a3', 'gdp_md_est', 'geometry']]
ind=[]
df=pd.read_excel(r"C:\Users\sina.kian\Desktop\Sicit_graphics\P1py.xlsx")

WW['scope']=['No Value']*len(WW)
WW['value']=[0]*len(WW)


ll=[]
LL=[]
inc=[]
incl=[]
for i in df['country']:
    ll=(WW[WW['name']==i].index.to_list())
    if ll==[]:
        inc=df[df['country']==i].index.to_list()
        incl+=inc
    LL+=ll

df=df.drop(incl)
df=df.set_axis(LL)
WW.update(df)



with plt.style.context(("seaborn", "ggplot")):
    ax=WW.plot(column='value', cmap=cmap,figsize=(18,10),
               edgecolor = "grey", legend=True)

plt.gca().axes.yaxis.set_visible(False)
plt.gca().axes.xaxis.set_visible(False)
fname='plt08.png'
plt.savefig(bbox_inches='tight',fname=fname)

ax.set_axis_off()
ax.set_title('Fatturato Totale [€] di ogni regione del mondo 2020')
fname='plt08_1.png'
plt.savefig(bbox_inches='tight',fname=fname)


WW['alpha']=[0]*len(WW)
for i in WW[WW['continent']=='pole'].index:
    WW['alpha'][i]=1




ax2=WW.plot(ax=ax, edgecolor=u'gray', color='White',alpha=WW['alpha'], figsize=(16,8), legend=True)
ax.set_title('Fatturato Totale [€] di ogni regione del mondo 2020')
fname='plt08_2.png'
plt.savefig(bbox_inches='tight',fname=fname)






with plt.style.context(("seaborn", "ggplot")):
    ax=WW.plot(column='value', cmap=cmap,figsize=(18,10),
               edgecolor = "grey", legend=True)

plt.gca().axes.yaxis.set_visible(False)
plt.gca().axes.xaxis.set_visible(False)

WW['alpha']=[0]*len(WW)
for i in WW[WW['continent']=='pole'].index:
    WW['alpha'][i]=1

ax2=WW.plot(ax=ax, edgecolor=u'gray', color='White',alpha=WW['alpha'], figsize=(16,8), legend=True)
ax.set_title('Fatturato Totale [€] di ogni regione del mondo 2020')
fname='plt08_3.png'
plt.savefig(bbox_inches='tight',fname=fname)




cmap = mpl.cm.Blues(np.linspace(0,1,40))
cmap = mpl.colors.ListedColormap(cmap[4:,:-1])






plt.style.context(("seaborn", "ggplot"))
ax=WW.plot(column='value', cmap=cmap, figsize=(16,8),edgecolor = "grey",legend=True)
#ax2=WW.plot(ax=ax, edgecolor=u'gray', color=myworld['color'],alpha=myworld['alpha'], figsize=(16,8))


ax.set_axis_off()
ax.set_title('Fatturato Totale [€] di ogni regione del mondo 2020')
fname='plt08_4.png'
plt.savefig(bbox_inches='tight',fname=fname)




plt.style.context(("seaborn", "ggplot"))
ax=WW.plot(column='value', cmap='OrRd', figsize=(16,8), edgecolor = "grey")
#ax2=WW.plot(ax=ax, edgecolor=u'gray', color=WW['color'],alpha=WW['alpha'], figsize=(16,8), legend=True)
plt.gca().axes.yaxis.set_visible(False)
plt.gca().axes.xaxis.set_visible(False)
#ax2.axis('scaled')
ax.set_title('Fatturato Totale [€] di ogni regione del mondo 2020')
fname='plt08_5.png'
plt.savefig(bbox_inches='tight',fname=fname)







cmap = mpl.cm.Greens(np.linspace(0,1,40))
cmap = mpl.colors.ListedColormap(cmap[4:,:-1])




with plt.style.context(("seaborn", "ggplot")):
    ax=WW.plot(column='value', cmap=cmap,figsize=(18,10),
               edgecolor = "grey", legend=True)#, missing_kwds={"edgecolor": "red", "hatch": "///"})

plt.gca().axes.yaxis.set_visible(False)
plt.gca().axes.xaxis.set_visible(False)
fname='plt08.png'
plt.savefig(bbox_inches='tight',fname=fname)

ax.set_axis_off()
ax.set_title('Fatturato Totale [€] di ogni regione del mondo 2020')




WW['Value_nan']=[np.nan]*len(WW)
for i in WW.index:
    if WW['value'].loc[i]!=0:
        WW['Value_nan'].loc[i]=WW['value'].loc[i]



with plt.style.context(("seaborn", "ggplot")):
    ax=WW.plot(column='Value_nan',scheme="NaturalBreaks", cmap=cmap,figsize=(18,10),
               edgecolor = "grey", missing_kwds={'color':'lightgrey', "edgecolor": "#FA9986", "hatch": "///","label": "0"}, legend=True, legend_kwds={'loc': (0.05, 0.2), 'fontsize' : 10, 'facecolor' : 'white', 'edgecolor': 'white'})




plt.gca().axes.yaxis.set_visible(False)
plt.gca().axes.xaxis.set_visible(False)



ax.set_axis_off()
ax.set_title('Fatturato Totale [€] di ogni regione del mondo 2020')

fname='plt08_6.png'
plt.savefig(bbox_inches='tight',fname=fname)
