import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data from CSV
data = pd.read_csv('health_data.csv')

# Assume 'sick' column is not present, you can add it based on your criteria
# For example, if cholesterol_level > threshold, consider the person sick
threshold = 200
data['sick'] = (data['cholesterol_level'] > threshold).astype(int)

# Features and target variable
X = data[['age', 'cholesterol_level']]
y = data['sick']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')