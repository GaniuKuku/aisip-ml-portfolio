def main():
    # Dictionary storing 10 African countries and capitals
    african_capitals = {
        "Nigeria": "Abuja",
        "Kenya": "Nairobi",
        "South Africa": "Pretoria", # Administrative capital
        "Ghana": "Accra",
        "Egypt": "Cairo",
        "Ethiopia": "Addis Ababa",
        "Morocco": "Rabat",
        "Rwanda": "Kigali",
        "Senegal": "Dakar",
        "Tanzania": "Dodoma"
    }

    print("--- African Capital Lookup ---")
    search_country = "Rwanda" # You can change this to input("Enter a country: ")

    # Lookup logic
    if search_country in african_capitals:
        capital = african_capitals[search_country]
        print(f"The capital of {search_country} is {capital}.")
    else:
        print(f"Sorry, {search_country} is not in our database.")

if __name__ == "__main__":
    main()
