import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

data = {
    "Weather": [
        "Sunny", "Sunny", "Rainy", "Rainy",
        "Cloudy", "Cloudy", "Sunny", "Rainy"
    ],
    "Temperature": [
        "Hot", "Cool", "Cool", "Hot",
        "Hot", "Cool", "Hot", "Cool"
    ],
    "Play": [0, 1, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)
weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()

df["Weather"] = weather_encoder.fit_transform(df["Weather"])
df["Temperature"] = temperature_encoder.fit_transform(df["Temperature"])

X = df[["Weather", "Temperature"]]
y = df["Play"]

model = DecisionTreeClassifier()
model.fit(X, y)

weather = weather_encoder.transform(["Sunny"])[0]
temperature = temperature_encoder.transform(["Cool"])[0]

prediction = model.predict([[weather, temperature]])

print("Play:", prediction[0])
