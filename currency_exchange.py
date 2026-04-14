def main():
    # Current approximate exchange rates against 1 NGN
    # Note: Rates fluctuate, these are sample static values for demonstration
    ngn_to_kes_rate = 0.11
    ngn_to_zar_rate = 0.015
    ngn_to_ghs_rate = 0.010

    # User input (hardcoded for the script, but could use input())
    amount_in_ngn = 50000  

    # Calculations using operators
    amount_in_kes = amount_in_ngn * ngn_to_kes_rate
    amount_in_zar = amount_in_ngn * ngn_to_zar_rate
    amount_in_ghs = amount_in_ngn * ngn_to_ghs_rate

    print(f"--- Currency Exchange Converter ---")
    print(f"Base Amount: {amount_in_ngn} NGN")
    print(f"Equivalent in KES: {amount_in_kes} Shillings")
    print(f"Equivalent in ZAR: {amount_in_zar} Rand")
    print(f"Equivalent in GHS: {amount_in_ghs} Cedi")

if __name__ == "__main__":
    main()
