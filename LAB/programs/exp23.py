# Implement Forward Chaining.

rules = [
    {'conditions': ['has_engine', 'has_wheels'], 'conclusion': 'is_vehicle'},
    {'conditions': ['is_vehicle', 'has_wings'],  'conclusion': 'is_aircraft'},
    {'conditions': ['is_vehicle', 'has_propeller'], 'conclusion': 'is_boat'},
    {'conditions': ['is_aircraft', 'is_jet_powered'], 'conclusion': 'is_airplane'},
    {'conditions': ['is_aircraft', 'has_rotor'], 'conclusion': 'is_helicopter'},
]

def forward_chaining(facts):
    facts = set(facts)
    changed = True
    derived = []
    while changed:
        changed = False
        for rule in rules:
            if all(c in facts for c in rule['conditions']):
                conclusion = rule['conclusion']
                if conclusion not in facts:
                    facts.add(conclusion)
                    derived.append(conclusion)
                    changed = True
    return facts, derived

initial_facts = ['has_engine', 'has_wheels', 'has_wings', 'is_jet_powered']

print("Forward Chaining - Technical Support System")
print("Initial Facts:", initial_facts)
final_facts, derived = forward_chaining(initial_facts)
print("Derived Facts:", derived)
print("All Known Facts:", sorted(final_facts))
