from Data import Data
from CostFunctions import Linear, Discrete
from Analyse import criteriaContribution, Map, Sensitivity

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

    def setFunctionWeights(self, criterion, function):
        """Set weights with zour function

        Args:
            criterion (str): Selected craterion
            function (function): Function for generating weighted values.

        Function:
            Args:
                data (table): Table of craterion values.
            Returns:
                table: Weighted values in same order.
        """
        self.data.setWeights(criterion, function(self.data.getCriterionValues(criterion)))

    def getWeightedTable(self):
        self.data.getWeightedTable()

    def setCriterionWeight(self, criterion, weight):
        self.data.setCriterionWeight(criterion, weight)

    def normalizeCriteriaWeights(self):
        self.data.normalizeCriteriaWeights()

    def getCriteriaWeights(self):
        self.data.getCriteriaWeights()

    def calcResult(self):
        self.data.calcResult()

    def getVariantsResults(self):
        self.data.getVariantsResults()

    def getBest(self):
        self.data.getBest()

    def getWorst(self):
        self.data.getWorst()

    def showCriteriaContribution(self):
        criteriaContribution(self.data)

    def showMap(self, craterion1, craiterion2):
        Map(self.data, craterion1, craiterion2)

    def showSensitivity(self, craterion):
        Sensitivity(self.data, craterion)
