# imports
from base_competitor import Competitor
import tensorflow as tf
from tensorflow import keras
import numpy as np
import itertools
import random

#TensorFlow_v1
class TF_v1(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "TF v1"
        self.epochs_num = 5

        self.correct_choice = [0]*nr

    def choose(self):

        if self.round == 0:
            self.choice = random.randint(1, 3)
        else:
            """ Import data in a training set and a test set """
            other = self.otherchoices[0:self.round]
            my = self.mychoices[0:self.round]
            correct_choice = self.correct_choice[0:self.round]
            input_data = other + my + correct_choice

            ### Fix correct data vector [0,0,1]


            print(input_data)
            print(correct_choice)


            """ Create structure for the Neural Network """

            model = keras.Sequential([
                keras.layers.Input(range(input_data)),      ### Figure this one out...
                keras.layers.Dense(32, activation="relu"),
                keras.layers.Dense(self.round, activation="softmax")
                ])
            # Set optimizer, loss function and correction metrics
            model.compile(optimmizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

            # Fit model to data
            model.fit(input_data, correct_choice, epochs=self.epochs_num)

            """ Predict data with the NN model """
            prediction = model.predict(test_images)

        self.correct_choice[self.round] = self.get_right_choice()

    # Method that creates a vector with all the right choices
    def get_right_choice(self):
        right_choice = 1
        if self.otherchoices[self.round] == 1:
            right_choice = 2
        elif self.otherchoices[self.round] == 2:
            right_choice = 3
        elif self.otherchoices[self.round] == 3:
            right_choice = 1
        return right_choice

