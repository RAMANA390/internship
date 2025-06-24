# Training and prediction inside Colab (simplified)
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Sample data
data = {
    "location": ["Anna Nagar", "T. Nagar", "Velachery", "Porur", "Ambattur"],
    "BHK": [3, 2, 3, 2, 2],
    "bath": [2, 1, 2, 2, 1],
    "sqft": [1500, 1000, 1600, 1200, 1100],
    "price": [7000000, 5000000, 6800000, 5200000, 4000000]
}
df = pd.DataFrame(data)

# Encode location
le = LabelEncoder()
df['location'] = le.fit_transform(df['location'])

X = df[['location', 'BHK', 'bath', 'sqft']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# --- Prediction part ---
# User inputs
location = "Velachery"
bhk = 3
bath = 2
sqft = 1500

loc_encoded = le.transform([location])[0]
input_data = np.array([[loc_encoded, bhk, bath, sqft]])
prediction = model.predict(input_data)[0]

print(f"Predicted Price for {location} with {bhk} BHK, {bath} bath, {sqft} sqft = ₹ {round(prediction, 2)}")
