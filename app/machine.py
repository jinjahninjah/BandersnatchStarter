import datetime

import joblib
from sklearn.ensemble import RandomForestClassifier


class Machine:

    def __init__(self, df):
        self.name = "Random Forest Classifier"
        target = df.Rarity
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)
        self.timestamp = datetime.datetime.now()

    def __call__(self, feature_basis):
        prediction, *_ = self.model.predict(feature_basis)
        confidence, *_ = self.model.predict_proba(feature_basis)
        return prediction, max(confidence)

    def save(self, filepath):
        return joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        return joblib.load(filepath)

    def info(self):
        return f"Model Used: {self.name}<br>Time Model Trained: {self.timestamp}"
