import xlrd
from Display import printList, printTable

class Data:
    def __init__(self, excel_file):
        self.variants = [] #table of variant names
        self.variants_result = [] #table of calculated and values of each variant
        self.criteria = [] #table of criteria names
        self.criteria_weights = [] #table of criteria weights
        self.data = [] #matrix of original data
        self.weighted_data = [] #matrix of weighted data
        self.excel_file = excel_file #file name
        self.setup() #load data from file and initialize tables

    def setup(self):
        self.loadExcel()
        self.weighted_data = self.data
        self.criteria_weights = [0 for _ in range(len(self.criteria))]
        self.variants_result = [0 for _ in range(len(self.variants))]

    def loadExcel(self):
        xl_workbook = xlrd.open_workbook(self.excel_file)
        xl_sheet = xl_workbook.sheet_by_index(0)
        self.criteria = xl_sheet.row_values(0)[1:] #get criteria names
        for i in range(1, xl_sheet.nrows): #get the rest data
            row = xl_sheet.row_values(i)
            self.variants.append(row[0]) #get variant name
            tmp = []
            for value in row[1:]: #get criteria values
                if type(value) != str:
                    if int(value) == value: #convert float to int
                        tmp.append(int(value))
                else:
                    tmp.append(value)
            self.data.append(tmp)
        xl_workbook.release_resources()
        del xl_workbook

    def getVariants(self):
        printList(self.variants)

    def getCriteria(self):
        printList(self.criteria)

    def getCriterionValues(self, criterion):
        result = []
        i = self.criteria.index(criterion)
        for row in self.data:
            result.append(row[i])
        return result

    def getWeightedCriterionValues(self, criterion):
        result = []
        i = self.criteria.index(criterion)
        for row in self.weighted_data:
            result.append(row[i])
        return result

    def getCriterionWeighted(self, criterion):
        return self.criteria_weights[self.criteria.index(criterion)]

    def getTable(self):
        printTable(self.variants, self.criteria, self.data)

    def getWeightedTable(self):
        printTable(self.variants, self.criteria, self.weighted_data)

    def getVariantsResults(self):
        printTable(['Rezultat:'], self.variants, [self.variants_result])

    def setWeights(self, criterion, criterion_data):
        i = self.criteria.index(criterion)
        for j in range(len(criterion_data)):
            self.weighted_data[j][i] = criterion_data[j]

    def setCriterionWeight(self, criterion, weight):
        i = self.criteria.index(criterion)
        self.criteria_weights[i] = weight

    def getCriteriaWeights(self):
        printTable(['Utezi:'], self.criteria, [self.criteria_weights])

    def normalizeCriteriaWeights(self):
        sum_w = sum(self.criteria_weights)
        for i in range(len(self.criteria_weights)):
            self.criteria_weights[i] /= sum_w

    def calcResult(self):
        for i in range(len(self.variants)):
            tmp = 0
            for j in range(len(self.criteria)):
                tmp += self.weighted_data[i][j]*self.criteria_weights[j]
            self.variants_result[i] = tmp

    def getBest(self):
        i = self.variants_result.index(max(self.variants_result))
        print("Best variant: " + self.variants[i] + " with " + "{:.2f}".format(max(self.variants_result)) + " points.")

    def getWorst(self):
        i = self.variants_result.index(min(self.variants_result))
        print("Worst variant: " + self.variants[i] + " with " + "{:.2f}".format(min(self.variants_result)) + " points.")

