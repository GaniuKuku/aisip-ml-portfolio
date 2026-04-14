def main():
    print("--- GDP per Capita Income Categorizer ---")
    country = "Senegal"
    gdp_per_capita = 1600 # USD

    # Categorization logic using if/elif/else
    if gdp_per_capita < 1135:
        category = "Low-income"
    elif 1135 <= gdp_per_capita <= 13845:
        category = "Middle-income"
    else:
        category = "High-income"

    print(f"{country} has a GDP per capita of ${gdp_per_capita}.")
    print(f"Category: {category} economy.")

if __name__ == "__main__":
    main()
