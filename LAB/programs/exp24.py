# Implement Backward Chaining.

rules = {
    'is_airplane':   [['is_aircraft', 'is_jet_powered']],
    'is_helicopter': [['is_aircraft', 'has_rotor']],
    'is_aircraft':   [['is_vehicle', 'has_wings']],
    'is_boat':       [['is_vehicle', 'has_propeller']],
    'is_vehicle':    [['has_engine', 'has_wheels'], ['has_engine', 'has_hull']],
}

def backward_chaining(goal, facts, rules, depth=0):
    indent = "  " * depth
    print(f"{indent}Trying to prove: {goal}")
    if goal in facts:
        print(f"{indent}  -> {goal} is a known fact.")
        return True
    if goal not in rules:
        print(f"{indent}  -> {goal} cannot be proven.")
        return False
    for condition_set in rules[goal]:
        print(f"{indent}  Rule: {goal} <- {condition_set}")
        if all(backward_chaining(cond, facts, rules, depth + 1) for cond in condition_set):
            facts.add(goal)
            print(f"{indent}  -> Proved: {goal}")
            return True
    return False

known_facts = {'has_engine', 'has_wheels', 'has_wings', 'is_jet_powered'}
goal = 'is_airplane'

print("Backward Chaining - Medical Diagnosis System")
print("Known Facts:", known_facts)
print(f"\nGoal: Prove '{goal}'\n")
result = backward_chaining(goal, known_facts, rules)
print(f"\nResult: '{goal}' is {'proven' if result else 'not proven'}.")
