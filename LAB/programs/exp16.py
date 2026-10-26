# Implement the Birds Fly Knowledge Base.

animals = {
    'eagle':   {'is_bird': True,  'has_wings': True,  'is_penguin': False},
    'penguin': {'is_bird': True,  'has_wings': True,  'is_penguin': True},
    'bat':     {'is_bird': False, 'has_wings': True,  'is_penguin': False},
    'dog':     {'is_bird': False, 'has_wings': False, 'is_penguin': False},
    'parrot':  {'is_bird': True,  'has_wings': True,  'is_penguin': False},
    'ostrich': {'is_bird': True,  'has_wings': True,  'is_penguin': False, 'flightless': True},
}

def can_fly(animal, props):
    if not props.get('is_bird') and not props.get('has_wings'):
        return False
    if props.get('is_penguin'):
        return False
    if props.get('flightless'):
        return False
    if props.get('is_bird') and props.get('has_wings'):
        return True
    return False

print("Birds Fly Knowledge Base:")
for animal, props in animals.items():
    result = can_fly(animal, props)
    print(f"  {animal.capitalize()} can fly: {result}")
