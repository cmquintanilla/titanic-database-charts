#import mongoDB as MongoDB
from numpy.core.defchararray import title
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def welcome():
    print(134 * '*')
    print("* Welcome to Evaluacion03, this program was created for learning purposes and it's a tiny program to consult the Titanic passengers *")
    print("* For this scenario we are using Pandas and Matplotlib to consult the passengers and see a couple of charts", 35 * ' ', '*')
    print(120 * '*')
    print("\n")


def menu():
    print("Choose an option please:")
    print("MENU")
    print("1- Search a passenger by Ticket number")
    print("2- Pie chart - Deaths & Survivors")
    print("3- Bar chart - Survivors by Travel Class")
    print("4- Most expensive ticket & Cheapest ticket")
    print("5- Exit")


def optionValidation(op):
    try:
        option = int(op)
        return option
    except ValueError:
        print("This is not a correct option!!!!")
        return -1

def loadCSVFile(path):
    df = pd.read_csv(path)
    return df

def inspectingData(df: pd.DataFrame):
    #Printing the Dataframe shape 
    print("#########Printing the Dataframe shape")
    print(df.shape)
    #Printing the Dataframe info
    print("#########Printing the Dataframe info")
    print(df.info())
    #Printing the Dataframe quantity of nulls
    print("#########Printing the Dataframe quantity of nulls")
    print(df.isnull().sum())
    #Printing the Dataframe head 25
    print("#########Printing the Dataframe head 25")
    print(df.head(25))
    #Printing the Dataframe tail 25
    print("#########Printing the Dataframe tail 25")
    print(df.tail(25))
    return df

def cleaningData(df: pd.DataFrame):
    #Replacing nulls with zero in Cuerpo columns
    df['Cuerpo'] = df['Cuerpo'].fillna(0)
    #Replacing nulls with zero in Edad columns
    df['Edad'] = df['Edad'].fillna(0)
    #Replacing nulls with zero in Tarifa columns
    df['Tarifa'] = df['Tarifa'].fillna(0)
    #Replacing nulls with "" in Cabina columns
    df['Cabina'] = df['Cabina'].fillna("")
    #Replacing nulls with "" in Bote de Rescate columns
    df['Bote de Rescate'] = df['Bote de Rescate'].fillna("")
    #Replacing nulls with "" in Destino columns
    df['Destino'] = df['Destino'].fillna("")
    return df

def printPassengerInfo(df: pd.DataFrame, ticketNumber):
    try:
        df = df.loc[df['Ticket'] == ticketNumber]
        if(df.empty):
            print("###Sorry, this ticket number doesn't exists in this data set###")
        else:
            print('Class:', df['Clase'][0])
            print('Survive:', "Yes" if df['Sobrevivio'][0] == 1 else "No")
            print('Name:', df['Nombre'][0])
            print('Gender:', df['Sexo'][0])
            print('Age:', df['Edad'][0])
            print('Ticket #:', df['Ticket'][0])
            print('Fare:', df['Tarifa'][0])
            print('Cabin:', df['Cabina'][0])
            print('Rescue boat:', df['Bote de Rescate'][0])
            print('Body:', df['Cuerpo'][0])
            print('Destination:', df['Destino'][0])

        print('\n')
    except ValueError:
        print("###Sorry, this ticket number doesn't exists in this data set###")

def chartDeathSuvivor(df: pd.DataFrame):
    deathSurviveCount = df.groupby("Sobrevivio")['Clase'].count()
    #print(deathSurviveCount)
    y = np.array([deathSurviveCount[0], deathSurviveCount[1]])
    thisLabels = ["Death", "Survivor"]
    plt.pie(y, labels=thisLabels, shadow= True)
    plt.legend(title= "Count Deaths & Survivors")
    plt.show()

def chartSuvivorByClass(df: pd.DataFrame):
    df = df.loc[df['Sobrevivio'] == 1]
    survivorByClassCount = df.groupby("Clase")['Sobrevivio'].count()
    #print(survivorByClassCount)
    labels = ['Clase 1', 'Clase 2', 'Clase 3']    
    y = np.array([survivorByClassCount[1], survivorByClassCount[2], survivorByClassCount[3]])
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots()
    x1 = ax.bar(x - width/2, y, width, label='Survivor')

    ax.set_ylabel('Survivor')
    ax.set_title('Survivors by Travel Class')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    ax.bar_label(x1, padding=3)

    fig.tight_layout()
    plt.show()

def minMaxTicketPrice(df: pd.DataFrame):
    df = df.loc[df['Tarifa'] != 0]
    print('\n')
    print('The most expensive fare: ', df['Tarifa'].max())
    print('The cheapest fare: ', df['Tarifa'].min())
    print('\n')
    #print(df)