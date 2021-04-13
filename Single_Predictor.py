import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split as tss
import joblib

# music_data = pd.read_csv("music.csv")
# X = music_data.drop(columns = ["genre"])
# y = music_data["genre"]

# model = DecisionTreeClassifier()
# model.fit(X, y)

model = joblib.load("music-reccomendation.joblib")

model.predict([[21, 1]])