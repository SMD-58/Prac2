{
    "A": {"dependencies": set(["B"])},
    "B": {"dependencies": set(["C", "F"])},
    "C": {"dependencies": set(["F"])},
    "F": {"dependencies": set(["A", "P"])}
}