import time

# Ransomware demand calculator
def main():
    # program intro
    input("Did you know the average ransomware ransom is $2.73 million in 2024?")
    print("Let's take a look at what you might be paying based on your business size.")

    # Take inputs from the user
    business_name = input("Enter the business name: ")
    
    # Initialize business_size
    business_size = ""

    # Loop until valid
    while business_size not in ["large", "medium", "small"]:
        business_size = input("Enter the business size (Large, Medium, Small): ").strip().lower()
        if business_size not in ["large", "medium", "small"]:
            print("Invalid size. Please enter Large, Medium, or Small.")

    # Optionally ask for business industry
    business_industry = input("Enter the business industry (optional, press Enter to skip): ")

    # Define ransom ranges based on business size
    if business_size == "large":
        demand_range = "$1,000,000 - $3,000,000"
    elif business_size == "medium":
        demand_range = "$250,000 - $500,000"
    elif business_size == "small":
        demand_range = "$50,000 - $250,000"

    # Display progress bar for calculation
    print("\nCalculating ransomware demand...\n")
    for i in range(5):
        print("#" * (i + 1), end="\r")
        time.sleep(0.5)  # Simulates processing time

    # Print the output
    print("\n*\n*")
    print(f"Business Name: {business_name}")
    print(f"Estimated Ransomware Demand Range: {demand_range}")
    
    # Provide prevention tips
    print("\n*** Cybersecurity Tips ***")
    print("1. Regularly backup your data.")
    print("2. Use strong, unique passwords.")
    print("3. Implement multi-factor authentication (MFA).")
    print("4. Train employees to recognize phishing emails.")
    print("5. Install antivirus software and keep it updated.")
    
    input("\nStay safe! Press Enter to exit.")

if __name__ == "__main__":
    main()
