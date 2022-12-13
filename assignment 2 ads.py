# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:46:54 2022

@author: akhil
"""
#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#giving the funtion to read the file
def read_file(filename):
    """


    Parameters
    ----------
    filename : csv file

    Returns
    -------
    df : dataframe with years as columns
    df_t : dataframe with countries as columns

    """
    df = pd.read_csv(f"{filename}.csv")
#dropping unwanted columns by using drop
    df_t = df.drop(["Series Name","Series Code","Country Code"], axis = 1, inplace=True)
    df_t = pd.DataFrame.transpose(df)
    return  df, df_t
#calling each dataset using read_file and printing
df_agris = read_file("Agricultural land")
df_co2 = read_file("CO2 emissions")
df_fores = read_file("Forest area")
df_pop = read_file("Population growth")
df_ren = read_file("Renewable energy consumption")
df_urba = read_file("Urban population")
print(df_agris,df_co2,df_fores,df_pop,df_ren,df_urba)

"""
ploting bar graphs

"""

#ploting bar graph of agriculturalland using pandas
df_agri = pd.read_csv("Agricultural land.csv")
plt.figure(figsize=(25,12))
width = 0.1
ag = np.arange(len(df_agri["Country Name"]))
plt.bar(ag,df_agri["1980"],width,label="1980",align="edge",)
plt.bar(ag+width*2,df_agri["1990"],width,label="1990",align="edge",)
plt.bar(ag+width*3,df_agri["2010"],width,label="2010",align="edge",)
plt.bar(ag+width*4,df_agri["2015"],width,label="2015",align="edge",)
plt.bar(ag+width*5,df_agri["2020"],width,label="2020",align="edge",)
plt.title("Agricultural land (sq. km)",fontsize=30)
plt.xticks(ag,df_agri["Country Name"],fontsize=25,rotation=90)
plt.xlabel("countries",size=25)
plt.legend(prop={"size":25})
plt.show()


#ploting bar graph of forest area using pandas
df_fore = pd.read_csv("Forest area.csv")
plt.figure(figsize=(25,12))
width = 0.1
fo = np.arange(len(df_fore["Country Name"]))
plt.bar(fo,df_fore["1980"],width,label="1980",align="edge",)
plt.bar(fo+width*2,df_fore["1990"],width,label="1990",align="edge",)
plt.bar(fo+width*3,df_fore["2010"],width,label="2010",align="edge",)
plt.bar(fo+width*4,df_fore["2015"],width,label="2015",align="edge",)
plt.bar(fo+width*5,df_fore["2020"],width,label="2020",align="edge",)
plt.title("Forest area (sq. km)",fontsize=30)
plt.xticks(fo,df_fore["Country Name"],fontsize=25,rotation=90)
plt.xlabel("countries",size=25)
plt.legend(prop={"size":25})
plt.show()


#read the data from csv file
df_urb = pd.read_csv("Urban population.csv")
#ploting bar graph using panda
plt.figure(figsize=(25,12))
width = 0.1
ub = np.arange(len(df_urb["Country Name"]))
plt.bar(ub,df_urb["1980"],width,label="1980",align="edge")
plt.bar(ub+width,df_urb["1990"],width,label="1990",align="edge")
plt.bar(ub+width*2,df_urb["2010"],width,label="2010",align="edge")
plt.bar(ub+width*3,df_urb["2015"],width,label="2015",align="edge")
plt.bar(ub+width*4,df_urb["2020"],width,label="2020",align="edge")
plt.title("Urban population (% of total population)",fontsize=30)
plt.xticks(ub,df_urb["Country Name"],fontsize=25,rotation=90)
plt.xlabel("countries",size=25)
plt.legend(prop={"size":25})
plt.show()

"""
ploting multiple line graph

"""

#read the data from csv file
df_co2 = pd.read_csv("CO2 emissions.csv")
#ploting multiple line graph using pandas
co2 = df_co2
co2 = co2.drop(columns={"Series Name","Series Code","Country Name","Country Code"})
co = np.transpose(co2)
data = co.loc["1980":"2019"]
data = co.rename(columns={0:"Australia",1:"Brazil",2:"Canada",3:"Germany",4:"India",5:"Ireland",6:"Spain",7:"United Kingdom",8:"United States"})
plt.figure(figsize=(25,15))
plt.title("CO2 emissions (kt)",size=30)
plt.plot(data.index,data["Australia"],label="Australia")
plt.plot(data.index,data["Brazil"],label="Brazil")
plt.plot(data.index,data["Canada"],label="Canada")
plt.plot(data.index,data["Germany"],label="Germany")
plt.plot(data.index,data["India"],label="India")
plt.plot(data.index,data["Ireland"],label="Ireland")
plt.plot(data.index,data["Spain"],label="Spain")
plt.plot(data.index,data["United Kingdom"],label="United Kingdom")
plt.plot(data.index,data["United States"],label="United States")
plt.legend(fontsize=15)
plt.xlim(1)
plt.show()
#read the data from csv file
df_ren = pd.read_csv("Renewable energy consumption.csv")
#ploting multiple line graph using pandas
ren = df_ren
#droping unwanted columns
ren = ren.drop(columns={"Series Name","Series Code","Country Name","Country Code"})
re = np.transpose(ren)
data = re.loc["1990":"2019"]
#renaming the columns to get location of each countries and values
data = re.rename(columns={0:"Australia",1:"Brazil",2:"Canada",3:"Germany",4:"India",5:"Ireland",6:"Spain",7:"United Kingdom",8:"United States"})
plt.figure(figsize=(25,15))
plt.title("Renewable energy consumption (% of total final energy consumption)",size=30)
plt.plot(data.index,data["Australia"],label="Australia")
plt.plot(data.index,data["Brazil"],label="Brazil")
plt.plot(data.index,data["Canada"],label="Canada")
plt.plot(data.index,data["Germany"],label="Germany")
plt.plot(data.index,data["India"],label="India")
plt.plot(data.index,data["Ireland"],label="Ireland")
plt.plot(data.index,data["Spain"],label="Spain")
plt.plot(data.index,data["United Kingdom"],label="United Kingdom")
plt.plot(data.index,data["United States"],label="United States")
plt.legend(fontsize=15)
plt.xlim(1)
plt.show()

"""
applying statistical tools

"""

#using mean for finding mean value of forest area in each year
mean_fore = np.mean(df_fore)
print("average forest area in each year= ",mean_fore)
#using mean for finding mean value of urban population in each year
mean_urb = np.mean(df_urb)
print("average urban population area in each year=",mean_urb)
#using std for finding standard deviation of forest area in each year
std_fore = np.std(df_fore)
print("standard deviation of forest area in each year=",std_fore)
#using std for finding standard deviation of urban population in each year
std_urb =np.std(df_urb)
print("standard deviation of urban population in each year=",std_urb)

