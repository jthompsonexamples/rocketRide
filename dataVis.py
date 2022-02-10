# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 09:56:42 2022

@author: bexar
"""

# andas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")

# If you were unable to complete the previous lab correctly you can uncomment and load this csv

df2 = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_2.csv')

df.head(5)
df2.head(5)

sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()


sns.catplot(y="LaunchSite", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()

sns.catplot(y="LaunchSite", x="PayloadMass", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()


df.loc[:,["Orbit","Class"]].groupby("Orbit").mean("Class").reset_index()
df.loc[df["Orbit"] == "SO", ["Orbit","Class"]]

sns.barplot(x="Orbit", y="Class", data=df.loc[:,["Orbit","Class"]].groupby("Orbit").mean("Class").reset_index())
plt.ylabel("Prob",fontsize=20)
plt.xlabel("Orbit",fontsize=20)
plt.show()

sns.catplot(y="Orbit", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.show()

df["year"]=pd.to_datetime(df["Date"]).dt.year

df.loc[:,["year","Class"]].groupby("year").mean("Class")


features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights',
               'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()

features_one_hot = pd.concat([features[['FlightNumber', 'PayloadMass','Flights','GridFins', 'Reused', 'Legs', 'Block', 'ReusedCount']],
                              pd.get_dummies(df[['Orbit','LaunchSite', 'LandingPad','Serial']])], axis=1)

features_one_hot.astype("float64").dtypes
