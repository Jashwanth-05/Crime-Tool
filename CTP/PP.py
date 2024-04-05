import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Pattern:
    def __init__(self, filename):
        self.filename = filename
        self.df=pd.read_csv(self.filename)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.gender_colors = {'Female': '#1f77b4', 'Male': '#ff7f0e'}


    def p1(self): 
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df, x='Date', hue='Date')
        plt.title('Temporal Patterns of Serial Killings')
        plt.xlabel('Date')
        plt.ylabel('Count of Killings')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def p2(self):
        plt.figure(figsize=(8, 6))
        sns.countplot(data=self.df, x='Location', hue='Location', palette='viridis')
        plt.title('Spatial Patterns of Serial Killings')
        plt.xlabel('Location')
        plt.ylabel('Count of Killings')
        plt.legend(title='Location', labels=self.df['Location'].unique())  # Set legend labels
        plt.tight_layout()
        plt.show()

    def p3(self):
        plt.figure(figsize=(8, 6))
        sns.histplot(data=self.df, x='Victim Age', bins=10, kde=True, hue='Victim Gender', palette=self.gender_colors)
        plt.title('Distribution of Victim Age by Gender')
        plt.xlabel('Victim Age')
        plt.ylabel('Count')
        plt.legend(title='Victim Gender', labels=['Female', 'Male'])
        plt.tight_layout()
        plt.show()

    def p4(self):
        plt.figure(figsize=(8, 6))
        sns.countplot(data=self.df, x='Method of Killing', hue='Method of Killing', palette='viridis')
        plt.title('Distribution of Methods of Killing')
        plt.xlabel('Method of Killing')
        plt.ylabel('Count of Killings')
        plt.xticks(rotation=45)
        plt.legend(title='Method of Killing', labels=self.df['Method of Killing'].unique())
        plt.tight_layout()
        plt.show()









