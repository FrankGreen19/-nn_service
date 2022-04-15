rules = [
    # 1 low parameter
    "IF (CP IS high) OR (CP IS low) AND (C IS high) AND (D IS high) AND (BT IS high) AND (A IS high) AND (F IS high) "
        "THEN (PP IS very_high)",
    "IF (CP IS high) AND (C IS high) OR (C IS low) AND (D IS high) AND (BT IS high) AND (A IS high) AND (F IS high) "
        "THEN (PP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (D IS high) OR (D IS low) AND (BT IS high) AND (A IS high) "
        "AND (F IS high) THEN (PP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (D IS high) AND (BT IS high) AND (A IS high) "
        "AND (F IS high) OR (F IS low) THEN (PP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (D IS high) AND (BT IS high) OR (BT IS medium) OR (BT IS low) AND (A IS high) "
        "AND (F IS high) THEN (PP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (D IS high) AND (BT IS high) AND (A IS high) OR (A IS medium) OR (A IS low) "
        "AND (F IS high) THEN (PP IS very_high)",

    # 2 low parameters
    "IF (CP IS high) AND (C IS high) AND (D IS high) AND (BT IS high) AND (A IS high) OR (A IS medium) OR (A IS low) "
        "AND (F IS high) OR (F IS low) THEN (PP IS high)",
    "IF (CP IS high) AND (C IS high) AND (D IS high) AND (BT IS high) OR (BT IS medium) OR (BT IS low) AND (A IS high) "
        "OR (A IS low) AND (F IS high) THEN (PP IS high)",
    "IF (CP IS high) AND (C IS high) AND (D IS high) OR (D IS low) AND (BT IS high) OR (BT IS medium) OR (BT IS low) "
        "AND (A IS high) AND (F IS high) THEN (PP IS high)",
    "IF (CP IS high) AND (C IS high) OR (C IS high) AND (D IS high) OR (D IS low) AND (BT IS high) AND (A IS high) "
        "AND (F IS high) THEN (PP IS high)",
    "IF (CP IS high) OR (CP IS low) AND (C IS high) OR (C IS high) AND (D IS high) AND (BT IS high) AND (A IS high) "
        "AND (F IS high) THEN (PP IS high)",
    "IF (CP IS high) OR (CP IS low) AND (C IS high) AND (D IS high) AND (BT IS high) AND (A IS high) "
        "AND (F IS high) OR (F IS low) THEN (PP IS high)",
    "IF (CP IS high) OR (CP IS low) AND (C IS high) AND (D IS high) AND (BT IS high) AND (A IS high) OR (A IS medium)"
        " OR (A IS low) AND (F IS high) THEN (PP IS high)",
    "IF (CP IS high) OR (CP IS low) AND (C IS high) AND (D IS high) AND (BT IS high) OR (BT IS medium) OR (BT IS low) AND "
        "(A IS high) AND (F IS high) THEN (PP IS high)",
    "IF (CP IS high) OR (CP IS low) AND (C IS high) AND (D IS high) OR (D IS low) AND (BT IS high) AND (A IS high) "
        "AND (F IS high) THEN (PP IS high)",
    "IF (CP IS high) AND (C IS high) OR (C IS low) AND (D IS high) AND (BT IS high) AND (A IS high) "
        "AND (F IS high) OR (F IS low) THEN (PP IS high)",
    "IF (CP IS high) AND (C IS high) OR (C IS low) AND (D IS high) AND (BT IS high) AND (A IS high) OR (A IS medium) OR "
        "(A IS low) AND (F IS high) THEN (PP IS high)",
    "IF (CP IS high) AND (C IS high) OR (C IS low) AND (D IS high) AND (BT IS high) OR (BT IS medium) OR (BT IS low) AND "
        "(A IS high) AND (F IS high) THEN (PP IS high)",
    "IF (CP IS high) AND (C IS high) AND (D IS high) OR (D IS low) AND (BT IS high) AND (A IS high) "
        "AND (F IS high) OR (F IS low) THEN (PP IS high)",
    "IF (CP IS high) AND (C IS high) AND (D IS high) OR (D IS low) AND (BT IS high) AND (A IS high) OR (A IS medium) OR"
        " (A IS low) AND (F IS high) THEN (PP IS high)",

    # medium (3 low parameters)
    "IF (CP IS low) AND (C IS low) AND (D IS low) AND (BT IS high) AND (A IS high) "
        "AND (F IS high) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (D IS low) AND (BT IS low) OR (BT IS medium) AND (A IS high) "
        "AND (F IS high) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (D IS low) AND (BT IS low) OR (BT IS medium) AND (A IS low) OR (A IS medium) "
        "AND (F IS high) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (D IS high) AND (BT IS low) OR (BT IS medium) AND (A IS low) OR (A IS medium) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS low) AND (C IS high) AND (D IS high) AND (BT IS high) AND (A IS low) OR (A IS medium) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (D IS high) AND (BT IS high) AND (A IS low) OR (A IS medium) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (D IS low) AND (BT IS high) AND (A IS low) OR (A IS medium) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS low) AND (C IS high) AND (D IS low) AND (BT IS low) OR (BT IS medium) AND (A IS low) OR (A IS medium) "
        "AND (F IS high) THEN (PP IS medium)",
    "IF (CP IS low) AND (C IS low) AND (D IS high) AND (BT IS low) OR (BT IS medium) AND (A IS low) OR (A IS medium) "
        "AND (F IS high) THEN (PP IS medium)",
    "IF (CP IS low) AND (C IS low) AND (D IS high) AND (BT IS high) AND (A IS high) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (D IS low) AND (BT IS high) AND (A IS high) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS low) AND (C IS high) AND (D IS low) AND (BT IS high) AND (A IS high) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS low) AND (C IS high) AND (D IS high) AND (BT IS low) OR (BT IS medium) AND (A IS high) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (D IS high) AND (BT IS low) OR (BT IS medium) AND (A IS high) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (D IS low) AND (BT IS low) OR (BT IS medium) AND (A IS high) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS low) AND (C IS low) AND (D IS high) AND (BT IS high) AND (A IS low) OR (A IS medium) "
        "AND (F IS high) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (D IS high) AND (BT IS high) AND (A IS low) OR (A IS medium) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (D IS low) AND (BT IS high) AND (A IS low) OR (A IS medium) "
        "AND (F IS low) THEN (PP IS medium)",
    "IF (CP IS low) AND (C IS high) AND (D IS low) AND (BT IS high) AND (A IS low) OR (A IS medium) "
        "AND (F IS high) THEN (PP IS medium)",

    # low (4 and more low parameters)
    # 4
    "IF (CP IS low) AND (C IS low) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS high) AND (F IS high) "
        "THEN (PP IS low)",
    "IF (CP IS high) AND (C IS low) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS high) THEN (PP IS low)",
    "IF (CP IS high) AND (C IS high) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS low) AND (C IS high) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS high) AND (C IS low) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS high) AND (C IS low) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS low) AND (C IS low) AND (D IS high) AND (BT IS high) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS high) AND (C IS low) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS high) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS high) AND (C IS low) AND (D IS high) AND (BT IS medium) OR (BT IS low) AND (A IS high) "
        "AND (F IS high) THEN (PP IS low)",
    "IF (CP IS low) AND (C IS high) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS high) "
        "AND (F IS high) THEN (PP IS low)",
    # 5
    "IF (CP IS low) AND (C IS low) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS high) THEN (PP IS low)",
    "IF (CP IS high) AND (C IS low) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS low) AND (C IS low) AND (D IS low) AND (BT IS high) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS low) AND (C IS low) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS high) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS low) AND (C IS low) AND (D IS high) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",
    "IF (CP IS low) AND (C IS high) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",

    # 6
    "IF (CP IS low) AND (C IS low) AND (D IS low) AND (BT IS medium) OR (BT IS low) AND (A IS medium) OR (A IS low) "
        "AND (F IS low) THEN (PP IS low)",
]

print(len(rules))
