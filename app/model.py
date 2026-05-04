
import numpy as np
from sklearn.linear_model import LogisticRegression

# simple dummy model (trained on fake data)
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

model = LogisticRegression()
model.fit(X, y)

def predict(value):
    result = model.predict([[value]])
    return int(result[0])
