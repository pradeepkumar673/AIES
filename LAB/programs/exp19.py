# Implement Planet Knowledge Representation.

planets = {
    'Mercury': {'position': 1, 'type': 'terrestrial', 'moons': 0, 'rings': False,
                'distance_from_sun_km': 57.9e6, 'diameter_km': 4879},
    'Venus':   {'position': 2, 'type': 'terrestrial', 'moons': 0, 'rings': False,
                'distance_from_sun_km': 108.2e6, 'diameter_km': 12104},
    'Earth':   {'position': 3, 'type': 'terrestrial', 'moons': 1, 'rings': False,
                'distance_from_sun_km': 149.6e6, 'diameter_km': 12742},
    'Mars':    {'position': 4, 'type': 'terrestrial', 'moons': 2, 'rings': False,
                'distance_from_sun_km': 227.9e6, 'diameter_km': 6779},
    'Jupiter': {'position': 5, 'type': 'gas_giant',   'moons': 95, 'rings': True,
                'distance_from_sun_km': 778.5e6, 'diameter_km': 139820},
    'Saturn':  {'position': 6, 'type': 'gas_giant',   'moons': 83, 'rings': True,
                'distance_from_sun_km': 1.43e9,  'diameter_km': 116460},
    'Uranus':  {'position': 7, 'type': 'ice_giant',   'moons': 27, 'rings': True,
                'distance_from_sun_km': 2.87e9,  'diameter_km': 50724},
    'Neptune': {'position': 8, 'type': 'ice_giant',   'moons': 16, 'rings': True,
                'distance_from_sun_km': 4.5e9,   'diameter_km': 49244},
}

def query_planet(name):
    if name in planets:
        p = planets[name]
        print(f"\n--- {name} ---")
        for key, value in p.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
    else:
        print(f"Planet '{name}' not found in knowledge base.")

def planets_with_rings():
    return [name for name, props in planets.items() if props['rings']]

def largest_planet():
    return max(planets, key=lambda p: planets[p]['diameter_km'])

query_planet('Earth')
query_planet('Saturn')
print("\nPlanets with rings:", planets_with_rings())
print("Largest planet:", largest_planet())
