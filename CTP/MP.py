import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Matching:
    def __init__(self,new_entry):
        self.old_data = pd.read_csv('Crime Matching\datamatch.csv')
        self.new_entry=new_entry
        matching_rate, top_matches =self.calculate_matching_rate()

        self.new_entry_df = pd.DataFrame([self.new_entry])

        self.old_data = pd.concat([self.old_data,self.new_entry_df], ignore_index=True)

        print("New Entry:")
        print(self.new_entry)
        print("Matching Rate: {:.2f}%".format(matching_rate))
        print("Top 5 Matches:")
        for index, score in top_matches:
            print("Matching Rate: {:.2f}%".format(score * 100))
            print(self.old_data.iloc[index])
            print()
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
    
