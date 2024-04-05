import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel

class Matching:
    def __init__(self,new_entry):
        self.old_data = pd.read_csv('Crime Matching\datamatch.csv')
        self.new_entry=new_entry
        self.matching_rate,self.top_matches =self.calculate_matching_rate()

        self.new_entry_df = pd.DataFrame([self.new_entry])

        self.old_data = pd.concat([self.old_data,self.new_entry_df], ignore_index=True)
        dialog = PopupDialog(self.new_entry, self.matching_rate,self.top_matches,self.old_data)
        dialog.exec_()
        self.old_data.to_csv('Crime Matching\datamatch.csv', index=False)

    def calculate_matching_rate(self):
        vectorizer = TfidfVectorizer()
        old_text = self.old_data['Area'] + ' ' + self.old_data['Acts'] + ' ' + self.old_data['Crime'] + ' ' + self.old_data['Victim_ID'].astype(str)
        new_text = self.new_entry['Area'] + ' ' + self.new_entry['Acts'] + ' ' + self.new_entry['Crime'] + ' ' + str(self.new_entry['Victim_ID'])
        vectors = vectorizer.fit_transform(list(old_text) + [new_text])

        similarity = cosine_similarity(vectors[-1], vectors[:-1])

        top_matches = sorted(enumerate(similarity[0]), key=lambda x: x[1], reverse=True)[:5]

        matching_rate = sum(score for _, score in top_matches) / len(top_matches)

        return matching_rate * 100, top_matches

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel

class PopupDialog(QDialog):
    def __init__(self, new_entry, matching_rate, top_matches,old_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Matching Results')
        self.setFixedSize(1366,768) 
        layout = QVBoxLayout()
        matching_rate_label = QLabel(f"Matching Rate: {matching_rate:.2f}%")
        layout.addWidget(matching_rate_label)
        label1=QLabel("\n")
        layout.addWidget(label1)
        
        # Display top 5 matches
        top_matches_label = QLabel("Top 5 Matches:")
        layout.addWidget(top_matches_label)
        label2=QLabel("\n")
        layout.addWidget(label2)
        for index, score in top_matches:
            match_label = QLabel(f"Matching Rate: {score * 100:.2f}%")
            layout.addWidget(match_label)
            # Assuming old_data is a DataFrame with columns similar to new_entry
            match_data = old_data.iloc[index]
            for key, value in match_data.items():
                label = QLabel(f"{key}: {value}")
                layout.addWidget(label)
            label1=QLabel("\n")
            layout.addWidget(label1)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    
    

