import pandas
import numpy as np
import matplotlib.pyplot as plt


class PyView:
    # loading data from excel file
    def __init__(self, excelFile):
        self.cost = dict()
        self.weights = dict()
        self.data = pandas.read_excel(excelFile)
        self.result_data = self.data.copy()

    # add attribut as parameter to set cost function for it
    # and add function of your own to calculate attributs in data
    def insertCost(self, attribut, fun):
        if attribut not in self.data.columns:
            print("Attribut doesn't exist in data!")
            return
        self.cost[attribut] = fun

    # inserting weights to attribut
    def insertWeight(self, attribut, weight):
        if attribut not in self.data.columns:
            print("Attribut doesn't exist in data!")
            return
        self.weights[attribut] = weight

    # converting attributes with cost functions
    def convertCosts(self):
        keys = list(self.cost.keys())

        if len(keys) == 0:
            print("No cost function dictionary! Insert them with function obj.insertCost(Attribut, fun)")
            return

        # going through all inserted attributes
        for key in keys:

            # converting current value with inserted function witch is saved in costs
            for value in range(0, len(self.data[key])):
                self.data[key][value] = self.cost[key](self.data[key][value])

    # muptiply each value in data with his weight
    def convertWeights(self):
        keys = list(self.weights.keys())

        if len(keys) == 0:
            print("No weight in dictionary! Insert them with function obj.insertWeight(Attribut, weight)")
            return

        for key in keys:

            for value in range(0, len(self.data[key])):
                self.result_data[key][value] = self.data[key][value] * self.weights[key]

                # returns result of each row

    def result(self):
        # all columns in our data
        keys = list(self.result_data.columns.values)
        # preparing array of zeros with length of first column
        res = [0] * len(self.result_data[keys[0]])

        for key in keys:
            for index in range(0, len(self.data[key])):
                res[index] += self.result_data[key][index]

        return res

    # draw a graph of sensitivity on desired attribut
    def showDiagram(self, attribut):

        if attribut not in self.weights:
            print("Attribut doesn't exist!")
            return

        size = len(self.data[attribut])
        # getting results of our data
        results = self.result()
        # current weight of desired attribut
        weight = self.weights[attribut]

        # preparing figure to display linear lines for each variation
        plt.figure()

        plt.title("Graph of sensitivity")
        plt.xlabel("Evalueted attribut: " + attribut)
        plt.ylabel("Cost")

        plt.plot([weight, weight], [0, 100], '--b')

        for index in range(0, size):
            cost = self.data[attribut][index]

            plt.plot([0, 1], [PyView.linear(weight, results[index], 1, cost, 0), cost], 'r')

        plt.show()

    # display data in table
    def displayData(self):
        print(self.data)

    # display cost of each added attribut in insertCost
    def displayCosts(self):
        keys = list(self.cost.keys())

        for key in keys:
            print(key + " " + str(self.cost[key](self.data[key][0])))

    # display weights of each added attribute in insertWeight
    def displayWeights(self):
        keys = list(self.weights.keys())

        for key in keys:
            print(key + ": " + self.weights[key])

    # displaing all values of attribut in our data
    def displayAttribut(self, attribut):
        print(self.data[attribut])

    # function used in creation of cost functions for each attribut
    def linear(x1, y1, x2, y2, x):
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return m * x + b