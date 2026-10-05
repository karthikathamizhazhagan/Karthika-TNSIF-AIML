import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([
    [20, 15000],
    [22, 18000],
    [25, 25000],
    [28, 30000],
    [30, 35000],
    [35, 40000],
    [40, 50000],
    [45, 60000]
])

y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)
age = 27
income = 28000

prediction = model.predict([[age, income]])

if prediction[0] == 1:
    print("Purchased: Yes")
else:
    print("Purchased: No")
