import plotly.express as px
import csv
import numpy as nm

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

def getDataSource(data_path):
    marks = []
    days = []
    with open(data_path) as x:
        data = csv.DictReader(x)
        for row in data:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return{"x":marks,"y":days}

def findCorrelation(data_source):
    correlation = nm.corrcoef(data_source["x"],data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = "./Marks-Days.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()