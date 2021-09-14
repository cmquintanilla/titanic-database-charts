import functions as fnc
import pandas as pd
import os

os.system("cls")
fnc.welcome()

df = fnc.loadCSVFile('Listade_Pasajeros_del_Titanic.csv')
#fnc.inspectingData(df)
df = fnc.cleaningData(df)
#print(df.isnull().sum())

while True:
    fnc.menu()
    option = input(" Please type your option: ")
    if fnc.optionValidation(option) == -1:
        continue
    if option == "1":
        ticket = input("Type the Ticket number please: ")
        print('\n')
        fnc.printPassengerInfo(df, ticket)
    if option == "2":
        fnc.chartDeathSuvivor(df)
    if option == "3":
        fnc.chartSuvivorByClass(df)
    if option == "4":
        fnc.minMaxTicketPrice(df)
    if option == "5":
        break