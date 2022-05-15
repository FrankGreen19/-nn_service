from simpful import *
from fuzzy_systems.fuzzy_rules.client_tuberculosis_rules import rules

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

H_1 = FuzzySet(function=Triangular_MF(a=0, b=0.5, c=0.9), term="low")
H_2 = FuzzySet(function=Triangular_MF(a=1, b=1.1, c=1.2), term="high")
FS.add_linguistic_variable("H", LinguisticVariable([H_1, H_2], concept="Кровохарканье",
                                                   universe_of_discourse=[0, 1.2]))

DA_1 = FuzzySet(function=Triangular_MF(a=0, b=0.5, c=0.9), term="low")
DA_2 = FuzzySet(function=Triangular_MF(a=1, b=1.1, c=1.2), term="high")
FS.add_linguistic_variable("DA", LinguisticVariable([DA_1, DA_2], concept="Потеря аппетита и снижение веса",
                                                   universe_of_discourse=[0, 1.2]))

BT_1 = FuzzySet(function=Triangular_MF(a=0, b=34, c=36.1), term="low")
BT_2 = FuzzySet(function=Triangular_MF(a=35.8, b=36.6, c=37.2), term="medium")
BT_3 = FuzzySet(function=Triangular_MF(a=37, b=39, c=42), term="high")
FS.add_linguistic_variable("BT", LinguisticVariable([BT_1, BT_2, BT_3], concept="Температура тела",
                                                    universe_of_discourse=[0, 42]))

F_1 = FuzzySet(function=Triangular_MF(a=0, b=0.5, c=0.9), term="low")
F_2 = FuzzySet(function=Triangular_MF(a=1, b=1.1, c=1.2), term="high")
FS.add_linguistic_variable("F", LinguisticVariable([F_1, F_2], concept="Повышенная утомляемость",
                                                    universe_of_discourse=[0, 1.2]))

PP_1 = FuzzySet(function=Triangular_MF(a=0, b=25, c=34), term="low")
PP_2 = FuzzySet(function=Triangular_MF(a=35, b=55, c=71), term="medium")
PP_3 = FuzzySet(function=Triangular_MF(a=70, b=80, c=90), term="high")
PP_4 = FuzzySet(function=Triangular_MF(a=87, b=95, c=100), term="very_high")
FS.add_linguistic_variable("TP", LinguisticVariable([PP_1, PP_2, PP_3, PP_4], concept="Вероятность туберкулеза",
                                                    universe_of_discourse=[0, 100]))

FS.add_rules(rules)


def get_fuzzy_tuberculosis_result(params):
    symptoms = ['CP', 'C', 'H', 'D', 'DA', 'F', 'BT']

    for symptom in symptoms:
        if symptom in params:
            if params[symptom] == 'true':
                params[symptom] = 1.1
            elif params[symptom] == 'false':
                params[symptom] = 0.5

            FS.set_variable(symptom, params[symptom])

    return FS.Mamdani_inference(["TP"])['TP']
