# Implement Person DOB Knowledge Base.

from datetime import date

persons_db = [
    {'name': 'Alice',   'dob': date(1990, 5, 14), 'city': 'Chennai'},
    {'name': 'Bob',     'dob': date(1985, 11, 23), 'city': 'Mumbai'},
    {'name': 'Charlie', 'dob': date(2000, 3, 8),   'city': 'Delhi'},
    {'name': 'Diana',   'dob': date(1995, 7, 30),  'city': 'Kolkata'},
    {'name': 'Eve',     'dob': date(1988, 1, 19),  'city': 'Bangalore'},
]

def query_by_name(name):
    for person in persons_db:
        if person['name'].lower() == name.lower():
            age = (date.today() - person['dob']).days // 365
            print(f"Name: {person['name']}, DOB: {person['dob']}, City: {person['city']}, Age: {age}")
            return
    print(f"Person '{name}' not found.")

def query_by_dob(dob):
    results = [p for p in persons_db if p['dob'] == dob]
    if results:
        for p in results:
            print(f"Name: {p['name']}, City: {p['city']}")
    else:
        print(f"No person found with DOB {dob}.")

def query_by_city(city):
    results = [p for p in persons_db if p['city'].lower() == city.lower()]
    if results:
        for p in results:
            print(f"Name: {p['name']}, DOB: {p['dob']}")
    else:
        print(f"No person found in city '{city}'.")

print("Person DOB Knowledge Base")
print("\nQuery by Name:")
query_by_name("Alice")
query_by_name("Charlie")

print("\nQuery by DOB:")
query_by_dob(date(1985, 11, 23))

print("\nQuery by City:")
query_by_city("Delhi")
