import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

data = pd.read_csv("backend_app\ml\dht11\shuffled_dataset.csv")

data.head()

data.tail()

data.columns

data.describe()

data.shape

data.dtypes

data.info()

data.isnull().sum()

df = data.dropna()

df.isnull().sum()

# sns.boxplot(df['Temperature'])

# sns.boxplot(df['Humidity'])

# sns.histplot(df['Temperature'], kde=True, color='red', bins=30, stat='density')

# sns.histplot(df['Humidity'], kde=True, color='green', bins=30, stat='density')

# sns.pairplot(df)
# plt.show()

dff = df[['Temperature', 'Humidity']]

label_encoder = LabelEncoder()
df['Comfort Level'] = label_encoder.fit_transform(df['Comfort Level'])

df['Comfort Level'].head(30)

X = df[['Temperature', 'Humidity']]
y = df['Comfort Level']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)  

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')
f1 = f1_score(y_test, predictions, average='weighted')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

joblib.dump(model, 'backend_app\ml\dht11\comfort_level_model.joblib')

# INPUT
new_data = [[11.5, 50]]
predicted_value = model.predict(new_data)

if predicted_value == 0:
    pred = "high"
elif predicted_value == 1:
    pred = "Low"
elif predicted_value == 2:
    pred = "moderate"

print("Predicted Comfort Level:", pred)
