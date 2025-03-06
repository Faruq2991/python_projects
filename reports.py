
def main():
    spacecraft = {
        "name": "Voyager 1",
        "distance": 163,
        "orbit": "Moon"
    }
    print(create_report(spacecraft))

    distances = {
        "Voyager 1": 163,
        "Voyager 2": 136,
         "Pioneer 10": 80,
         "Pioneer 11": 44,
         "New Horizons": 58,
    }
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth.")
    print(create_distance(distances))

def create_report(spacecraft):
    return f"""
    ========== SPACECRAFT REPORT ===========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==============================
    """

def create_distance(distances):
    return f"""
    ========== SPACECRAFT REPORT ===========
    Name: {distances.get("name", "Unknown")}
    ==============================
    """
main()