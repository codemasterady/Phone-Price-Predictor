# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout


class NeuralEngine:
    def __init__(self):
        self.nn = Sequential()
        self.scaler = StandardScaler()
        pass

    #! Function that trains the model
    def train(self):
        # Getting the dataset
        dataset = pd.read_csv(
            r"C:\Users\Selvaseetha\YouTube Codes\App Price Range Predictor\models\train.csv")
        features = dataset.iloc[:, :-1].values
        price_range = dataset.iloc[:, -1].values
        price_range = np.array(price_range).reshape(-1, 1)

        # Scaling the dataset
        features = self.scaler.fit_transform(features)

        # Building the architecture of the Neural Network
        self.nn.add(Dense(units=150, activation='relu'))
        self.nn.add(Dense(units=75, activation='relu'))
        self.nn.add(Dropout(rate=0.2))
        self.nn.add(Dense(units=40, activation='relu'))
        self.nn.add(Dense(units=20, activation='relu'))
        self.nn.add(Dropout(rate=0.2))
        self.nn.add(Dense(units=4, activation='softmax'))
        self.nn.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
                        metrics=['accuracy'])
        self.nn.fit(features, price_range, batch_size=50, epochs=10)
        print("Model Trained")

    #! Testing The Performance
    def performanceTester(self):

        # Sample predicting
        test_set = pd.read_csv(
            r"C:\Users\Selvaseetha\YouTube Codes\App Price Range Predictor\models\test.csv")
        test_features = test_set.iloc[:, 1:].values
        test_features = self.scaler.fit_transform(test_features)
        y_pred = self.nn.predict(test_features)

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
        plt.title(
            "Performance Graph\nNote: The larger the dip, the worse the performance")
        plt.show()

    #! Predicting the final output
    def compute(self):
        pass
