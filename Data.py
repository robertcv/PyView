import xlrd
from Display import printList, printTable

class Data:
    def __init__(self, excel_file):
        self.variants = []
        self.variants_result = []
        self.criteria = []
        self.criteria_weights = []
        self.data = []
        self.weighted_data = []
        self.excel_file = excel_file
        self.loadExcel()

    def loadExcel(self):
        xl_workbook = xlrd.open_workbook(self.excel_file)
        xl_sheet = xl_workbook.sheet_by_index(0)
        self.criteria = xl_sheet.row_values(0)[1:]
        for i in range(1, xl_sheet.nrows):
            row = xl_sheet.row_values(i)
            self.variants.append(row[0])
            tmp = []
            for value in row[1:]:
                if type(value) != str:
                    if int(value) == value:
                        tmp.append(int(value))
                else:
                    tmp.append(value)
            self.data.append(tmp)
        xl_workbook.release_resources()
        del xl_workbook
        self.setup()

    def setup(self):
        self.weighted_data = self.data
        self.criteria_weights = [0 for _ in range(len(self.criteria))]
        self.variants_result = [0 for _ in range(len(self.variants))]

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

    def getTable(self):
        printTable(self.variants, self.criteria, self.data)

    def getWeightedTable(self):
        printTable(self.variants, self.criteria, self.weighted_data)

    def setWeights(self, criterion, criterion_data):
        i = self.criteria.index(criterion)
        for j in range(len(criterion_data)):
            self.weighted_data[j][i] = criterion_data[j]

    def setCriterionWeights(self, criterion, weight):
        i = self.criteria.index(criterion)
        self.criteria_weights[i] = weight

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

