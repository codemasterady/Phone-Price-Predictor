# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout


# Getting the dataset
dataset = pd.read_csv("train.csv")
features = dataset.iloc[:, :-1].values
price_range = dataset.iloc[:, -1].values
price_range = np.array(price_range).reshape(-1, 1)

# Scaling the dataset
scaler = StandardScaler()
features = scaler.fit_transform(features)

# Building the architecture of the Neural Network
nn = Sequential()
nn.add(Dense(units=150, activation='relu'))
nn.add(Dense(units=75, activation='relu'))
nn.add(Dropout(rate=0.2))
nn.add(Dense(units=40, activation='relu'))
nn.add(Dense(units=20, activation='relu'))
nn.add(Dropout(rate=0.2))
nn.add(Dense(units=4, activation='softmax'))
nn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
nn.fit(features, price_range, batch_size=50, epochs=10)
print("Model Trained")

# Sample predicting
test_set = pd.read_csv("test.csv")
test_features = test_set.iloc[:, 1:].values
test_features = scaler.fit_transform(test_features)
y_pred = nn.predict(test_features)

# Extracting y_pred
list_of_preds_percentage = []
list_of_selected_members = []
for inner_list in y_pred:
    prev_value = -1
    selected_index = -1
    for i in range(0, len(inner_list)):
        if (inner_list[i] > prev_value):
            prev_value = inner_list[i]
            selected_index = i
    list_of_preds_percentage.append(prev_value)
    list_of_selected_members.append(selected_index)

# Plotting the assurance graph
plt.plot(list_of_preds_percentage[:100], color='green')
plt.xlabel("Case Number")
plt.ylabel("Percentage") 
plt.title("Assurance Graph")
plt.show()
