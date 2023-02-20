import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LeakyReLU
from keras.preprocessing import sequence
from keras.utils import np_utils

def build_model():
    model = Sequential()
    model.add(Dense(128, input_dim=200, activation=LeakyReLU(alpha=0.3)))
    model.add(Dense(64, activation=LeakyReLU(alpha=0.3)))
    model.add(Dense(32, activation=LeakyReLU(alpha=0.3)))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def load_data(filename):
    # Load log data into a pandas dataframe
    log_data = pd.read_csv(filename)

    # Preprocess log data and extract relevant features
    log_data = log_data.dropna()
    log_data = log_data.drop(['timestamp', 'host', 'message'], axis=1)

    # Encode categorical variables as one-hot encodings
    log_data = pd.get_dummies(log_data, columns=['level'])

    # Split log data into features and labels
    features = log_data.drop('anomaly', axis=1).values
    labels = log_data['anomaly'].values.reshape(-1, 1)

    # Normalize feature values to have zero mean and unit variance
    features = (features - np.mean(features, axis=0)) / np.std(features, axis=0)

    return features, labels

def train_model(features, labels, epochs=10):
    model = build_model()
    model.fit(features, labels, epochs=epochs, batch_size=32, validation_split=0.2)
    return model

def evaluate_model(model, features, labels):
    accuracy = model.evaluate(features, labels, verbose=0)[1]
    print('Accuracy: {:.2f}%'.format(accuracy * 100))

def predict(model, features):
    probabilities = model.predict(features)
    return probabilities

filename = 'logs.csv'
features, labels = load_data(filename)
model = train_model(features, labels)
evaluate_model(model, features, labels)

predictions = predict(model, features)

# Generate a report based on the predictions
anomalies = []
for i, p in enumerate(predictions):
    if p > 0.5:
        anomalies.append(i)

if anomalies:
    print('Anomalies detected in logs:')
    for i in anomalies:
        print('Log {}: {:.2f}% chance of being an anomaly'.format(i, predictions[i][0] * 100))
else:
    print('No anomalies detected in logs.')