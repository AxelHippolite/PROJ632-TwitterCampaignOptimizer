import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def getDatesCSV(path):
    """
    input: str
    output: list
    returns the creation dates of all the tweets of the file passed in argument
    """
    df = pd.read_excel(path)
    data = pd.DataFrame(df, columns=[1]).values.tolist()
    return [dates[0] for dates in data]

def formatter(dates):
    """
    input: list
    output: list
    returns all dates in datetime format
    """
    format_string = "%Y-%m-%d %H:%M:%S"
    return [datetime.strptime(i[:-6], format_string) for i in dates]

def datasetCreator(data):
    """
    input: list
    output: lists
    returns the temporal distribution of tweets by months, weekdays and hours
    """
    months, days, hours = [0 for i in range(12)], [0 for i in range(7)], [0 for i in range(24)]
    for i in data:
        months[i.month - 1] += 1
        days[int(i.strftime("%w"))] += 1
        hours[i.hour] += 1
    return months, days, hours

def displayHist(months, days, hours):
    """
    input: lists
    output: None
    display the temporal distribution in a Bar Diagram
    """
    fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)
    fig.suptitle("Temporal Distribution of the Tweets")

    axs[0].bar([datetime(1, i, 1).strftime('%b') for i in range(1, 13)], months, color='orangered', align='center')
    axs[0].set_xlabel('Months'), axs[0].set_ylabel('# of Tweets')

    axs[1].bar([datetime(2022, 5, i).strftime('%a') for i in range(9, 16)], days, color='coral', align='center')
    axs[1].set_xlabel('Days'), axs[1].set_ylabel('# of Tweets')

    axs[2].bar([str(i) + 'h' for i in range(24)], hours, color='lightsalmon', align='center')
    axs[2].set_xlabel('Hours'), axs[2].set_ylabel('# of Tweets')

    print("Close the Diagrams to Continue...")

    plt.show()

def main():
    """
    input: None
    output: None
    main function allowing to display the temporal distribution of a list of tweets
    """
    path = input("Enter the Path to your Tweets List : ")
    dates = formatter(getDatesCSV(path))
    print("Total Tweets :", len(dates))
    months, days, hours = datasetCreator(dates)
    displayHist(months, days, hours)
