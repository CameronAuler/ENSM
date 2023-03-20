import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LeakyReLU

# Read in the log data and preprocess it
log_data = []
with open('logfile.csv', 'r') as f:
    # Skip the header line
    next(f)
    for line in f:
        columns = line.strip().split('\t')
        one_hot_row = []
        for i, column in enumerate(columns):
            # Create a one-hot encoding for each column
            unique_values = set([row[i] for row in log_data])
            print(f"Unique values for column {i}: {unique_values}")
            if not unique_values:
                values = ['0']
            else:
                values = ['0'] * len(unique_values)
                try:
                    values[list(unique_values).index(column)] = '1'
                except ValueError:
                    print(f"ValueError: {column} is not in list")
            one_hot_row += values
        log_data.append(one_hot_row)

# Convert the preprocessed data to a numpy array
log_data = np.array(log_data, dtype=np.float32)

# Split the data into training and testing sets
train_data = log_data[:8000, :]
test_data = log_data[8000:, :]

# Define the neural network model
model = Sequential()
model.add(Dense(64, input_shape=(log_data.shape[1],)))
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.5))
model.add(Dense(32))
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(train_data[:, :-1], train_data[:, -1], epochs=10, batch_size=64, validation_data=(test_data[:, :-1], test_data[:, -1]))

# Evaluate the model on the test data
loss, accuracy = model.evaluate(test_data[:, :-1], test_data[:, -1])
print('Test loss:', loss)
print('Test accuracy:', accuracy)
