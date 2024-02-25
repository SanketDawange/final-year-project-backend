import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("backend_app\ml\mqt135\Gas_Sensors_Measurements.csv")

df.head()

df.tail()

df.columns

df.describe()

df.shape

df.size

df.dtypes

df.info()

df.isnull().sum()

# sns.boxplot(df['MQ135'])

# sns.histplot(df['MQ135'], kde=True, color='red', bins=30, stat='density')

# plt.xlabel('MQ135')
# plt.ylabel('Concentration')
# plt.title('Histogram ')
# plt.show()

# sns.pairplot(df)
# plt.show()

df['MQ135'].value_counts()

df['Gas'].value_counts()

X = df[['MQ135']]
y = df['Gas']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_pred

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Updating ML model...")
joblib.dump(model, 'backend_app\ml\mqt135\gas_concentration.joblib')
print("ML model updated successfully")

# concentration_input = float(input("Enter the concentration value: "))
# concentration_input = [[concentration_input]]
# predicted_gas = model.predict(concentration_input)[0]
# print("Predicted gas type:", predicted_gas)
