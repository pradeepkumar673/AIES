# Implement Fruit Color Classification.

fruit_rules = [
    {'color': 'red',    'texture': 'smooth', 'fruit': 'Apple'},
    {'color': 'yellow', 'texture': 'smooth', 'fruit': 'Banana'},
    {'color': 'orange', 'texture': 'rough',  'fruit': 'Orange'},
    {'color': 'green',  'texture': 'smooth', 'fruit': 'Lime'},
    {'color': 'purple', 'texture': 'smooth', 'fruit': 'Grapes'},
    {'color': 'yellow', 'texture': 'rough',  'fruit': 'Pineapple'},
    {'color': 'red',    'texture': 'rough',  'fruit': 'Strawberry'},
    {'color': 'green',  'texture': 'rough',  'fruit': 'Kiwi'},
]

def classify_fruit(color, texture):
    for rule in fruit_rules:
        if rule['color'] == color and rule['texture'] == texture:
            return rule['fruit']
    return "Unknown Fruit"

test_cases = [
    ('red', 'smooth'),
    ('yellow', 'rough'),
    ('green', 'smooth'),
    ('orange', 'rough'),
    ('purple', 'smooth'),
]

print("Fruit Color Classification:")
for color, texture in test_cases:
    fruit = classify_fruit(color, texture)
    print(f"  Color: {color}, Texture: {texture} => {fruit}")
