# imports
from base_competitor import Competitor
import tensorflow as tf
from tensorflow import keras
import numpy as np
import random

#TensorFlow_v1
class TF_v1(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "TF v1"
        self.epochs_num = 5

    def choose(self):

        if self.round == 0:
            self.choice = random.randint(1, 3)
        else:
            """ Import data in a training set and a test set """
            other = self.otherchoices[0:self.round]
            my = self.mychoices[0:self.round]
            input_data = other + my
            input_data = input_data / 3     # Data is flat and minimized
            correct_choice = self.get_right_choice()

            """ Create structure for the Neural Network """

            model = keras.Sequential([
                keras.layers.Flatten(input_shape=(self.round, 1)),
                keras.layers.Dense(32, activation="relu"),
                keras.layers.Dense(3, activation="softmax")
                ])
            # Set optimizer, loss function and correction metrics
            model.compile(optimmizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

            # Fit model to data
            model.fit(input_data, correct_choice, epochs=self.epochs_num)

            """ Predict data with the NN model """
            prediction = model.predict(test_images)

    # Method that creates a vector with all the right choices
    def get_right_choice(self):
        output = [0] * self.round
        for i in range(self.round):
            if self.otherchoices[i] == 1:
                right_choice = 2
            if self.otherchoices[i] == 2:
                right_choice = 3
            if self.otherchoices[i] == 3:
                right_choice = 1
            output[i] = right_choice
        return output


