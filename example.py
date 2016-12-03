from PyView import PyView

model = PyView("example_table.xlsx")
model.getTable()

print("---------------------------------------------------")
model.getCriteria()
model.getVariants()

print("---------------------------------------------------")
model.setLinearWeights('Nadstropje', min_v=3, max_v=6)
model.setLinearWeights('Cena', reversed=True)
model.setLinearWeights('Udobje')

def MojaFunkcija(criterion_data):
    return [100 if x%2 else 0 for x in criterion_data]

model.setFunctionWeights('Velikost sobe', MojaFunkcija)
model.setDiscreteWeights('Na vrhu stavbe', {'DA':100, 'NE':0})

model.getWeightedTable()

print("---------------------------------------------------")
model.setCriterionWeight('Nadstropje', 5)
model.setCriterionWeight('Cena', 3)
model.setCriterionWeight('Udobje', 2)
model.setCriterionWeight('Velikost sobe', 3)
model.setCriterionWeight('Na vrhu stavbe', 4)

model.normalizeCriteriaWeights()
model.getCriteriaWeights()

print("---------------------------------------------------")
model.calcResult()
model.getBest()
model.getWorst()
model.getVariantsResults()

print("---------------------------------------------------")
model.showCriteriaContribution()

print("---------------------------------------------------")
model.showMap('Cena', 'Nadstropje')

print("---------------------------------------------------")
model.showSensitivity('Cena')
