from Data import Data
from CostFunctions import Linear, Discrete

class PyView:
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = Data(self.fileName)

    def getVariants(self):
        self.data.getVariants()

    def getCriteria(self):
        self.data.getCriteria()

    def getTable(self):
        self.data.getTable()

    def setLinearWeights(self, criterion, reversed=False, min_v=None, max_v=None):
        self.data.setWeights(criterion, Linear(self.data.getCriterionValues(criterion), reversed=reversed, min_v=min_v, max_v=max_v))

    def setDiscreteWeights(self, criterion, dic):
        self.data.setWeights(criterion, Discrete(self.data.getCriterionValues(criterion), dic))

    def getWeightedTable(self):
        self.data.getWeightedTable()

    def setCriterionWeights(self, criterion, weight):
        self.data.setCriterionWeights(criterion, weight)

    def normalizeCriteriaWeights(self):
        self.data.normalizeCriteriaWeights()

    def calcResult(self):
        self.data.calcResult()

    def getBest(self):
        self.data.getBest()

    def getWorst(self):
        self.data.getWorst()