import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def p1(c):
    file_path = 'Crime Rate\Chennai.csv'
    data = pd.read_csv(file_path)
    city_name =c
    city_data = data[data['Area'] == city_name]
    crime_counts = city_data['Crime'].value_counts()
    plt.figure(figsize=(10, 6))
    crime_counts.plot(kind='bar', color='skyblue')
    plt.title('Crime Rate in ' + city_name)
    plt.xlabel('Crime Type')
    plt.ylabel('Number of Crimes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def p2(c):
    file_path = 'Crime Rate\Chennai.csv'
    data = pd.read_csv(file_path)
    crime_type = c
    crime_counts_by_area = data.groupby(['Area', 'Crime']).size().unstack(fill_value=0)
    total_crimes_by_area = crime_counts_by_area.sum(axis=1)
    top_10_areas = total_crimes_by_area.nlargest(10).index
    top_10_data = data[(data['Area'].isin(top_10_areas)) & (data['Crime'] == crime_type)]
    colors = plt.cm.tab10(np.arange(len(top_10_areas)))
    plt.figure(figsize=(10, 6))
    top_10_data['Area'].value_counts().sort_values().plot(kind='barh', color=colors)
    plt.title(f'{crime_type} in Top 10 Areas')
    plt.xlabel('Number of Occurrences')
    plt.ylabel('Area')
    plt.tight_layout()
    plt.show()