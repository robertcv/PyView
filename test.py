from PyView import PyView

model = PyView("example_table.xlsx")
model.getTable()

model.setLinearWeights('Nadstropje', min_v=3, max_v=5)
model.setLinearWeights('Cena', reversed=True)
model.setLinearWeights('Udobje')
model.setLinearWeights('Velikost sobe')
model.setDiscreteWeights('Na vrhu stavbe', {'DA':100, 'NE':0})

model.getWeightedTable()

model.setCriterionWeights('Nadstropje', 5)
model.setCriterionWeights('Cena', 3)
model.setCriterionWeights('Udobje', 2)
model.setCriterionWeights('Velikost sobe', 3)
model.setCriterionWeights('Na vrhu stavbe', 4)

model.normalizeCriteriaWeights()

model.calcResult()

model.getBest()
model.getWorst()