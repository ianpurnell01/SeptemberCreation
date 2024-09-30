# Ransomware demand calculator

def main():
    #program intro
    input("Did you know the average ransomware ransom is $2.73 million in 2024?")

    input("Let's take a look at what you might be paying based on your business size.")

    # Take inputs from the user
    business_name = input("Enter the business name: ")
    
    # Initialize business_size
    business_size = ""
    
    # Loop until valid
    while business_size not in ["large", "medium", "small"]:
        business_size = input("Enter the business size (Large, Medium, Small): ").strip().lower()
        if business_size not in ["large", "medium", "small"]:
            print("Invalid size. Please enter Large, Medium, or Small.")

    # for future use, also calculate industry
    # business_industry = input("Enter the business industry: ")

    # Determine the output based on business size
    if business_size == "large":
        output = "$1,000,000+"
    elif business_size == "medium":
        output = "$250,000-$500,000"
    elif business_size == "small":
        output = "$50,000-$250,000"

    # Print the output
    print("*\n*")
    print(f"Business Name: {business_name}")
    input(f"Average Estimated Ransomware Demand: {output}")
    

if __name__ == "__main__":
    main()

# Info collected from various sources including, Coveware, Sophos, and CISA.gov