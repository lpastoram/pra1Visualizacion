import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from copy import deepcopy

original_data = pd.read_csv("covid_19_clean_complete.csv")
country = list(original_data["Country/Region"].drop_duplicates())
dates = list(original_data["Date"].drop_duplicates())
originalRegions = list(original_data["WHO Region"].drop_duplicates())
realRegions = ["Asia","Europe","Africa","Americas","Oceania"]

"""def changeRegion(originalRegion):
    if originalRegion == "Eastern Mediterranean":
        region = "Asia"
    elif originalRegion == 'South-East Asia':
        region = "Asia"
    elif originalRegion == 'Western Pacific':
        region = "Oceania"
    else:
        region = originalRegion
    return region

dictRegions = {"Eastern Mediterranean": "Asia", 
                       'South-East Asia':"Asia",
                       'Western Pacific':"Oceania"}
data = original_data.replace({"WHO Region":dictRegions})"""
data = deepcopy(original_data)
data["Region"] = data["WHO Region"]
data["Country"] = data["Country/Region"]
data = data.drop(["WHO Region","Province/State","Country/Region"],axis=1)


###############################################################################
# 1 - FIRST DATA SET

"""
datesCol = [[item] for item in dates]
data1 = deepcopy(data)
data1 = data1.drop(["Lat","Long"],axis=1)
data1 = data1.groupby(["Date",'Region',"Country"]).aggregate({'Confirmed':'sum'})
data1.reset_index(inplace=True)

newColumns = deepcopy(dates)
newColumns.append("Region")
newColumns.append("Country")
newColumns.append("URL")

finalData1 = []
dataaux =  pd.read_csv("flourish.csv")
dataaux["Country"]=dataaux["Country Name"]

for i in range(len(country)):
    auxData = data1[data1.Country == country[i]]
    pais = country[i]
    regione = data1[data1.Country == country[i]]["Region"].iloc[0]
    values = []
    for j in range(len(dates)):
        a = auxData[auxData.Date==dates[j]].iloc[0]["Confirmed"]
        values.append(a)
    values.append(regione)
    values.append(pais)
    if pais not in  ["Holy See","Saint Lucia","Saint Vincent and the Grenadines",
                     "San Marino","Taiwan*","US","Saint Kitts and Nevis","Kosovo"]:
        if 'United' in pais:
            l = pais[:10]+'.*'
            r = dataaux[dataaux.Country.str.match(l)].iloc[0]["Image URL"]
            values.append(r)
            finalData1.append(values)
        else:
            l = pais[:3]+'.*'
            r = dataaux[dataaux.Country.str.match(l)].iloc[0]["Image URL"]
            values.append(r)
            finalData1.append(values)
    


data1 = pd.DataFrame(finalData1, columns=newColumns)

data1.to_csv("data1.csv")
"""

###############################################################################
# 2 - SECOND DATA SET

data2 = deepcopy(data)
data2 = data2.drop(["Lat","Long"],axis=1)
data2 = data2.groupby(["Country","Date"]).aggregate({'Active':'sum'})
data2.reset_index(inplace=True)
paises2 = ["China","Philippines","Iran","Pakistan","Italy","Spain","Russia",
           "South Africa","Algeria","Canada","Brazil","India","Thailand"]
data2 = deepcopy(data2[data2["Country"].isin(paises2)])


dataArrays=[]
for i in range(len(dates)):
    aux = deepcopy(data2[data2.Date ==dates[i]])
    row = []
    for j in range(len(paises2)):
        aux2 = deepcopy(aux[aux.Country==paises2[j]])
        row.append(aux2.iloc[0].Active)
    row.append(dates[i])
    dataArrays.append(row)

paises2.append("Fechas")

data2 = pd.DataFrame(dataArrays, columns=paises2)

data2.to_csv("data2.csv")
        