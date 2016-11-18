import xlrd
from CostFunctions import Linear, Discrete
from Display import printList, printTable

class Data:
    def __init__(self, excel_file):
        self.variants = []
        self.criteria = []
        self.data = []
        self.weighted_data = []
        self.excel_file = excel_file
        self.loadExcel()

    def loadExcel(self):
        pass

    def getVariants(self):
        printList(self.variants)

    def getCriteria(self):
        printList(self.criteria)

    def getTable(self):
        printTable(self.variants, self.criteria, self.data)

    def getWeightedTable(self):
        printTable(self.variants, self.criteria, self.weighted_data)

    def calculateWeight(self, variant, fun):
        pass


