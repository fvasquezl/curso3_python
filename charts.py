import matplotlib.pyplot as plt
import csv
from functools import reduce


def generate_bar_chart(labels,values):
    fig, ax= plt.subplots()
    ax.bar(labels,values)
    ax.tick_params(axis='x', rotation=45)
    plt.show()

def generate_pie_chart(labels,values):
    fig, ax= plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.xticks(rotation=20)
    plt.show() 
    

def get_data_country_dict(country):
   with open('./data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    keys = headers[5:13]
    countries_dict = list(dict(zip(headers,row)) for row in reader)
    country_dict = [x for x in countries_dict if x['Country']==country].pop()
    filtered_country = {k:int(v) for (k,v) in country_dict.items() if k in keys} 
    return filtered_country

def get_data_countries_percent():
   with open('./data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    countries_dict={x[3]:float(x[-1]) for x in reader if x[4]=="North America"}
    return countries_dict
           

if __name__ == "__main__":
    # country = 'Mexico'
    # country_dict = get_data_country_dict(country)
    # generate_bar_chart(country_dict.keys(),country_dict.values()) 
    country_percent = get_data_countries_percent()
    generate_pie_chart(country_percent.keys(),country_percent.values())    

