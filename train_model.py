import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

# Load data
data = [[
'Anna Nagar',3,2,1500,7000000],[
'T. Nagar',2,1,1000,5000000],[
'Velachery',3,2,1600,6800000],[
'Porur',2,2,1200,5200000],[
'Ambattur',2,1,1100,4000000]]

# Encode location
le = LabelEncoder()
data['location'] = le.fit_transform(data['location'])

# Features and target
X = data[['location', 'BHK', 'bath', 'sqft']]
y = data['price']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and encoder
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(le, open('encoder.pkl', 'wb'))
