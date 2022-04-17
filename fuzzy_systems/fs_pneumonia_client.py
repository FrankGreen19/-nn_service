from simpful import *
from fuzzy_systems.fuzzy_rules.client_pneumonia_rules import rules

FS = FuzzySystem()

CP_1 = FuzzySet(function=Triangular_MF(a=0, b=0.5, c=0.9), term="low")
CP_2 = FuzzySet(function=Triangular_MF(a=1, b=1.1, c=1.2), term="high")
FS.add_linguistic_variable("CP", LinguisticVariable([CP_1, CP_2], concept="Боль в груди",
                                                    universe_of_discourse=[0, 1.2]))

C_1 = FuzzySet(function=Triangular_MF(a=0, b=0.5, c=0.9), term="low")
C_2 = FuzzySet(function=Triangular_MF(a=1, b=1.1, c=1.2), term="high")
FS.add_linguistic_variable("C", LinguisticVariable([C_1, C_2], concept="Кашель",
                                                    universe_of_discourse=[0, 1.2]))

D_1 = FuzzySet(function=Triangular_MF(a=0, b=0.5, c=0.9), term="low")
D_2 = FuzzySet(function=Triangular_MF(a=1, b=1.1, c=1.2), term="high")
FS.add_linguistic_variable("D", LinguisticVariable([D_1, D_2], concept="Одышка",
                                                    universe_of_discourse=[0, 1.2]))

BT_1 = FuzzySet(function=Triangular_MF(a=0, b=34, c=36.1), term="low")
BT_2 = FuzzySet(function=Triangular_MF(a=35.8, b=36.6, c=37.2), term="medium")
BT_3 = FuzzySet(function=Triangular_MF(a=37, b=39, c=42), term="high")
FS.add_linguistic_variable("BT", LinguisticVariable([BT_1, BT_2, BT_3], concept="Температура тела",
                                                    universe_of_discourse=[0, 42]))

A_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=39), term="low")
A_2 = FuzzySet(function=Triangular_MF(a=38, b=50, c=65), term="medium")
A_3 = FuzzySet(function=Triangular_MF(a=65, b=70, c=100), term="high")
FS.add_linguistic_variable("A", LinguisticVariable([A_1, A_2, A_3], concept="Возраст",
                                                   universe_of_discourse=[0, 100]))

F_1 = FuzzySet(function=Triangular_MF(a=0, b=0.5, c=0.9), term="low")
F_2 = FuzzySet(function=Triangular_MF(a=1, b=1.1, c=1.2), term="high")
FS.add_linguistic_variable("F", LinguisticVariable([F_1, F_2], concept="Повышенная утомляемость",
                                                    universe_of_discourse=[0, 1.2]))

PP_1 = FuzzySet(function=Triangular_MF(a=0, b=25, c=34), term="low")
PP_2 = FuzzySet(function=Triangular_MF(a=35, b=55, c=71), term="medium")
PP_3 = FuzzySet(function=Triangular_MF(a=70, b=80, c=90), term="high")
PP_4 = FuzzySet(function=Triangular_MF(a=87, b=95, c=100), term="very_high")
FS.add_linguistic_variable("PP", LinguisticVariable([PP_1, PP_2, PP_3, PP_4], concept="Вероятность пневмонии",
                                                    universe_of_discourse=[0, 100]))


FS.add_rules(rules)

FS.set_variable("CP", 1.1)
FS.set_variable("C", 1.1)
FS.set_variable("D", 1.1)
FS.set_variable("BT", 36.6)
FS.set_variable("A", 70)
FS.set_variable("F", 0.5)

print(FS.Mamdani_inference(["PP"]))
