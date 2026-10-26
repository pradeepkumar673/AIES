# Implement Family Knowledge Representation.

family = {
    'parent': [
        ('Tom', 'Bob'), ('Tom', 'Liz'),
        ('Bob', 'Ann'), ('Bob', 'Pat'),
        ('Pat', 'Jim')
    ],
    'male': ['Tom', 'Bob', 'Pat', 'Jim'],
    'female': ['Liz', 'Ann']
}

def is_parent(x, y):
    return (x, y) in family['parent']

def is_grandparent(x, z):
    return any(is_parent(x, y) and is_parent(y, z) for y in get_all_persons())

def is_sibling(x, y):
    if x == y:
        return False
    return any(is_parent(p, x) and is_parent(p, y) for p in get_all_persons())

def is_uncle(x, y):
    return x in family['male'] and any(is_sibling(x, p) and is_parent(p, y) for p in get_all_persons())

def get_all_persons():
    persons = set()
    for a, b in family['parent']:
        persons.add(a)
        persons.add(b)
    return persons

persons = get_all_persons()

print("Family Knowledge Base Results:")
print("Is Tom a parent of Bob?", is_parent('Tom', 'Bob'))
print("Is Tom a grandparent of Ann?", is_grandparent('Tom', 'Ann'))
print("Are Bob and Liz siblings?", is_sibling('Bob', 'Liz'))
print("Is Bob an uncle of Jim?", is_uncle('Bob', 'Jim'))
