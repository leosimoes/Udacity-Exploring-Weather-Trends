import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

YEARS_PERIOD = 10 

def plotTemperaturesPerYears(years_global_temp, global_temp, years_rj_temp, rj_temp): 
        fig = plt.figure() 
        plt.title("Years X Temperatures (10-year Moving Averages)")
        plt.plot(years_global_temp, global_temp, "blue", label="Global") 
        plt.plot(years_rj_temp, rj_temp, "red", label="Rio de Janeiro") 
        plt.ylabel("Temperatures (°C)")
        plt.xlabel("Years")
        plt.legend(loc="center right") 
        fig.savefig('temperaturesPerYears.png') 
        plt.show() 

def calculeMovingAverage10(temp): 
        mov_avg = []
        for i in range(0, len(temp) - YEARS_PERIOD + 1): 
                sum_avg = sum(temp[i:i + YEARS_PERIOD]) / YEARS_PERIOD
                mov_avg.append(sum_avg) 
        return mov_avg 

def main(): 
        # Opening csv files as pandas data frames 
        df_global_temp = pd.read_csv("Temperature_Global.csv", sep=",", encoding="UTF8") 
        df_rj_temp = pd.read_csv("Temperature_Rio_de_Janeiro.csv", sep=",", encoding="UTF8")

        # Filling in possible null or NaN values 
        df_global_temp = df_global_temp.fillna(0) 
        df_rj_temp = df_rj_temp.fillna(0) 

        # Separating data from years and temperatures, and sorting in an increasing way 
        years_global_temp = df_global_temp['year'].values[::-1] 
        years_rj_temp = df_rj_temp['year'].values[::-1] 
        global_temp = df_global_temp['avg_temp'].values[::-1] 
        rj_temp = df_rj_temp['avg_temp'].values[::-1]

        plotTemperaturesPerYears(years_global_temp[0:101], calculeMovingAverage10(global_temp), years_rj_temp[0:101], calculeMovingAverage10(rj_temp)) 

if __name__ == '__main__': main()
