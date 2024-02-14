import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

stdata=pd.read_csv("CaseStudy-11.csv")
t=True
while(t==True):
    n=int(input(""" Welcome to Python internship project done by Swapnadeep Kapuri and Omkar Bhandari  
                Menu (select any one of it)
                1.Get the 1st six rows
                2.Check the columns contained in the data set
                3.Check the shape of the dataframe
                4.Check if the data frame has any null values
                5.List the last six rows
                6.Check the values for the columns /"Confirmed Indian National" and /"Confirmed Foreign National"
                7.Drop the columns /'Sno' and /'Time'
                8.Find the maximum cases until 11th August 2021 for each state
                9.Find out total confirmed cases till 11th August 2021
                10.Find the percentage of the active, fatal and cured cases
                11.Check out the data for the 10 most affected states with covid-19 in India
                12.Find out total deaths till August 2021
                13.EXIT
                DEFAULT:Error
                Enter your option:"""))
    if(n==1):
        print("The 1st six rows are:")
        print(stdata.head(6))
    if(n==2):
        print("The columns contained in the data set are:")
        print(stdata.columns)
    if(n==3):
        print("Shape of the dataframe is (i.e rows and columns):")
        print(stdata.shape)
    if(n==4):
        print("Does the Dataframe contains null values?")
        print(stdata.isnull().sum())
    if(n==5):
        print("The last six rows are:")
        print(stdata.tail(6))
    if(n==6):
        print("The values of the columns of Confirmed Indian and Foreign Nationals are:")
        print(stdata[["ConfirmedIndianNational","ConfirmedForeignNational"]])
    if(n==7):
        print("As dropping columns might disturb .csv files instead columns except of Sno and Time will be displayed")
        print(stdata[["Date","State/UnionTerritory","ConfirmedIndianNational","ConfirmedForeignNational","Cured","Deaths","Confirmed"]])
        print("Note: By using stdata.drop(['Sno','Time']) method we can drop the required columns if required")
    if(n==8):
        print("The maximum cases until 11th August 2021 for each state is:")
        result=stdata[["Date","State/UnionTerritory",'Confirmed']].loc['1/30/2020':'8/11/2021'].groupby(["State/UnionTerritory"]).max()["Confirmed"]
        print(result)
    if(n==9):
        print("Total Confirmed cases until 11th August 2021 is:")
        result2=stdata[["Date","State/UnionTerritory",'Confirmed']].loc['1/30/2020':'8/11/2021'].groupby(["State/UnionTerritory"]).sum()["Confirmed"]
        print(result2)   
    if(n==10):
        print("The percentage of active cases are:")
        result3=((stdata.sum()["Confirmed"]-stdata.sum()["Cured"])/stdata.sum()["Confirmed"])*100
        print(result3)
        print("The percentage of fatal cases i.e deaths are:")
        result9=(stdata.sum()["Deaths"]/stdata.sum()["Confirmed"])*100
        print(result9)
        print("The percentage of cured cases are:")
        result10=(stdata.sum()["Cured"]/stdata.sum()["Confirmed"])*100
        print(result10)
        print("The percentage in the pie chart is as following:")
        x=np.array([result3,result9,result10])
        labels = ['Active', 'Fatal', 'Cured']
        colors = ['red', 'blue', 'green']
        plt.pie(x,labels=labels, colors=colors)
        plt.title("The percentage of covid cases")
        plt.show()
    if(n==11):
        print("The data of 10 most affected states in India are:")
        result4=stdata[["Date","State/UnionTerritory",'Confirmed']].loc['1/30/2020':'8/11/2021'].groupby(["State/UnionTerritory"]).sum()["Confirmed"].sort_values().tail(10)
        print(result4)
    if(n==12):
        print("Total Deaths till 11th August 2021 is:")
        result5=stdata.loc['1/30/2020':'8/11/2021'].sum()["Deaths"]
        print(result5)
    if(n==13):
        t=False
    if(type(n)!=int or n>13 or n<1):
        print("Wrong Option typed!! Please type a correct option!!")
        

