import my_charts
import pandas as pd

def run():
   df = pd.read_csv('./data.csv')
   df = df[df['Continent']=='North America']
   country =df['Country'].values
   percentages = df['World Population Percentage'].values
   my_charts.generate_pie_chart(country,percentages) 

   
if __name__ == "__main__":
    run()