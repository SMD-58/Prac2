{
    'A': {"dependencies": set(['B', 'C'])},
    'B': {"dependencies": set(['A', 'D', 'E'])},
    'C': {"dependencies": set(['A', 'F'])},
    'D': {"dependencies": set(['B'])},
    'E': {"dependencies": set(['B', 'F'])},
    'F': {"dependencies": set(['C', 'E'])}
}