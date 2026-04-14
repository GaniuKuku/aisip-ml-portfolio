def main():
    # List of tuples: (City Name, Population in millions)
    cities = [
        ("Lagos", 21.0),
        ("Kigali", 1.2),
        ("Cairo", 20.4),
        ("Nairobi", 4.4),
        ("Kinshasa", 14.9),
        ("Accra", 2.6)
    ]

    # Create a copy to modify so we don't destroy the original list
    cities_copy = cities.copy()
    top_3 = []

    # Using a for loop to find the top 3 largest cities
    for _ in range(3):
        largest_city = ("", 0)
        for city in cities_copy:
            if city[1] > largest_city[1]:
                largest_city = city
        
        top_3.append(largest_city)
        cities_copy.remove(largest_city) # Remove so we can find the next largest

    print("--- Top 3 Largest Cities in the List ---")
    for rank, city in enumerate(top_3, start=1):
        print(f"{rank}. {city[0]} - {city[1]} million people")

if __name__ == "__main__":
    main()
