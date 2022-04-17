rules = [
    # 1 low
    "IF (CP IS low) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS high) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS high) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS high) AND (DA IS high) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS high) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS very_high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS very_high)",

    # 2 lows
    "IF (CP IS low) AND (C IS low) AND (H IS high) AND (D IS high) AND (DA IS high) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS high) AND (DA IS high) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS low) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS low) AND (BT IS low) AND "
    "(F IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS high) AND (BT IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",
    "IF (CP IS low) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS low) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS high) AND (DA IS high) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS high) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",
    "IF (CP IS low) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS low) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS high) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS low) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS low) AND (H IS high) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",
    "IF (CP IS low) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS high) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS low)  AND (H IS high) AND (D IS low) AND (DA IS high) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS high) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS high) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS high) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",
    "IF (CP IS low) AND (C IS high) AND (H IS low) AND (D IS high) AND (DA IS high) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS high) AND (DA IS high) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS high)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS high)",

    # 3 lows
    "IF (CP IS low) AND (C IS low) AND (H IS low) AND (D IS high) AND (DA IS high) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS low) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS low) AND (DA IS low) AND (BT IS high) AND "
    "(F IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS low) AND (C IS low) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS low)  AND (H IS low) AND (D IS high) AND (DA IS high) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS low) AND (DA IS high) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS low) AND (C IS low) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS low) AND (DA IS high) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS medium)",
    "IF (CP IS low) AND (C IS low) AND (H IS high) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS medium)",
    "IF (CP IS low) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS low) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",

    # 4
    "IF (CP IS low) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS high) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (H IS high) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS low) AND (C IS low) AND (H IS high) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS low) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS low) AND (H IS high) AND (D IS low) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS high) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",
    "IF (CP IS low) AND (C IS high) AND (H IS high) AND (D IS high) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS medium)",

    # 5 low parameters
    "IF (CP IS low) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS high) AND "
    "(BT IS high) THEN (TP IS low)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS low)",
    "IF (CP IS high) AND (C IS high) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS low) AND (C IS low) AND (H IS low) AND (D IS high) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS low) AND (C IS low) AND (H IS high) AND (D IS low) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS low) AND (C IS high) AND (H IS low) AND (D IS low) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS low) AND (C IS high) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS low)",

    # 6
    "IF (CP IS low) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS high) THEN (TP IS low)",
    "IF (CP IS low) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS high) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS low) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS high) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS low) AND (C IS low) AND (H IS low) AND (D IS high) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS low) AND (C IS low) AND (H IS high) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS low) AND (C IS high) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
    "IF (CP IS high) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",

    # 7
    "IF (CP IS low) AND (C IS low) AND (H IS low) AND (D IS low) AND (DA IS low) AND (F IS low) AND "
    "(BT IS medium) OR (BT IS low) THEN (TP IS low)",
]
