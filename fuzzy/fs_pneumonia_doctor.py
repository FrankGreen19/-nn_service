from simpful import *

FS = FuzzySystem()

S_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=35.9), term="low")
S_2 = FuzzySet(function=Triangular_MF(a=36, b=36.6, c=37.2), term="medium")
S_3 = FuzzySet(function=Triangular_MF(a=37.1, b=39, c=42), term="high")
FS.add_linguistic_variable("BT", LinguisticVariable([S_1, S_2, S_3], universe_of_discourse=[0, 42]))

F_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=40), term="low")
F_2 = FuzzySet(function=Triangular_MF(a=40, b=50, c=65), term="medium")
F_3 = FuzzySet(function=Triangular_MF(a=65, b=70, c=100), term="high")
FS.add_linguistic_variable("A", LinguisticVariable([F_1, F_2, F_3], universe_of_discourse=[40, 100]))

BU_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=7), term="medium")
BU_2 = FuzzySet(function=Triangular_MF(a=7, b=9, c=11), term="high")
FS.add_linguistic_variable("BUN", LinguisticVariable([BU_1, BU_2], concept="Азот мочевины, ммоль/л",
                                                     universe_of_discourse=[0, 11]))

RR_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=30), term="medium")
RR_2 = FuzzySet(function=Triangular_MF(a=30, b=40, c=80), term="high")
FS.add_linguistic_variable("RR", LinguisticVariable([RR_1, RR_2], concept="частота дыхательных движений, уд/мин",
                                                    universe_of_discourse=[0, 50]))

BP_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=90), term="low")
BP_2 = FuzzySet(function=Triangular_MF(a=91, b=125, c=135), term="medium")
BP_3 = FuzzySet(function=Triangular_MF(a=140, b=170, c=200), term="high")
FS.add_linguistic_variable("BP", LinguisticVariable([BP_1, BP_2, BP_3], concept="Артериальное давление",
                                                    universe_of_discourse=[0, 200]))

HR_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=65), term="low")
HR_2 = FuzzySet(function=Triangular_MF(a=60, b=60, c=95), term="medium")
HR_3 = FuzzySet(function=Triangular_MF(a=90, b=125, c=150), term="high")
FS.add_linguistic_variable("HR", LinguisticVariable([HR_1, HR_2, HR_3], concept="Частота ударов сердца",
                                                    universe_of_discourse=[0, 150]))

AB_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=7.35), term="low")
AB_2 = FuzzySet(function=Triangular_MF(a=7.36, b=7.4, c=7.44), term="medium")
AB_3 = FuzzySet(function=Triangular_MF(a=7.43, b=7.5, c=8), term="high")
FS.add_linguistic_variable("AB", LinguisticVariable([AB_1, AB_2, AB_3], concept="рН артериальной крови",
                                                    universe_of_discourse=[0, 8]))

SU_1 = FuzzySet(function=Triangular_MF(a=2.6, b=5, c=7.5), term="medium")
SU_2 = FuzzySet(function=Triangular_MF(a=7.3, b=9, c=11), term="high")
FS.add_linguistic_variable("SU", LinguisticVariable([SU_1, SU_2], concept="Мочевина сыворотки крови, ммоль/л",
                                                    universe_of_discourse=[2.6, 11]))

SS_1 = FuzzySet(function=Triangular_MF(a=0, b=120, c=130), term="low")
SS_2 = FuzzySet(function=Triangular_MF(a=128, b=130, c=145), term="medium")
FS.add_linguistic_variable("SS", LinguisticVariable([SS_1, SS_2], concept="Натрий сыворотки крови, ммоль/л",
                                                    universe_of_discourse=[0, 160]))

SG_1 = FuzzySet(function=Triangular_MF(a=0, b=7, c=14), term="low")
SG_2 = FuzzySet(function=Triangular_MF(a=12, b=13, c=15), term="medium")
FS.add_linguistic_variable("SG", LinguisticVariable([SG_1, SG_2], concept="Глюкоза сыворотки крови, ммоль/л",
                                                    universe_of_discourse=[0, 15]))

PP_1 = FuzzySet(function=Triangular_MF(a=0, b=25, c=34), term="low")
PP_2 = FuzzySet(function=Triangular_MF(a=35, b=55, c=74), term="medium")
PP_3 = FuzzySet(function=Triangular_MF(a=75, b=85, c=100), term="high")
FS.add_linguistic_variable("PP", LinguisticVariable([PP_1, PP_2, PP_3], concept="Вероятность пневмонии",
                                                    universe_of_discourse=[0, 100]))

R1 = "IF (BT IS medium) AND (A IS medium) AND (BUN IS medium) AND (RR IS medium) AND (BP IS low) AND (HR IS medium) " \
     "AND (AB IS medium) AND (SU IS medium) AND (SS IS medium) AND (SG IS medium) THEN (PP IS low)"
R2 = "IF (BT IS high) AND (A IS high) AND (BUN IS high) AND (RR IS high) AND (BP IS high) AND (HR IS high) " \
     "AND (AB IS high) AND (SU IS high) AND (SS IS low) AND (SG IS low) THEN (PP IS high)"
R3 = "IF (BT IS high) AND (A IS medium) AND (BUN IS high) AND (RR IS medium) AND (BP IS high) AND (HR IS high) " \
     "AND (AB IS high) AND (SU IS high) AND (SS IS medium) AND (SG IS low) THEN (PP IS medium)"
R4 = "IF (BT IS medium) AND (A IS high) AND (BUN IS high) AND (RR IS high) AND (BP IS high) AND (HR IS high) " \
     "AND (AB IS high) AND (SU IS high) AND (SS IS medium) AND (SG IS medium) THEN (PP IS medium)"
FS.add_rules([R1, R2, R3, R4])


def get_fuzzy_result(bt, a, bun, rr, bp, hr, ab, su, ss, sg):
    FS.set_variable("BT", bt)
    FS.set_variable("A", a)
    FS.set_variable("BUN", bun)
    FS.set_variable("RR", rr)
    FS.set_variable("BP", bp)
    FS.set_variable("HR", hr)
    FS.set_variable("AB", ab)
    FS.set_variable("SU", su)
    FS.set_variable("SS", ss)
    FS.set_variable("SG", sg)

    return FS.Mamdani_inference(["PP"])
