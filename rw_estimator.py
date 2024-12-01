import time
import subprocess
import sys
import webbrowser
import os

# Ransomware demand calculator
def main():
    # Program intro
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

    # Ask for business industry
    print("\nSelect your business industry from the options below:")
    industries = {
        "healthcare": 0.7,
        "finance": 0.75,
        "technology": 0.80,
        "education": 0.85,
        "retail": 0.90,
        "other": 1.0
    }
    print("\n".join([f"- {key.capitalize()}" for key in industries.keys()]))
    
    business_industry = ""
    while business_industry not in industries:
        business_industry = input("Enter the business industry: ").strip().lower()
        if business_industry not in industries:
            print("Invalid industry. Please select one from the list.")

    industry_multiplier = industries[business_industry]

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
    print(f"Industry: {business_industry.capitalize()} (Risk Multiplier: {industry_multiplier})")
    
    # Provide prevention tips
    print("\n*** Cybersecurity Tips ***")
    print("1. Regularly backup your data.")
    print("2. Use strong, unique passwords.")
    print("3. Implement multi-factor authentication (MFA).")
    print("4. Train employees to recognize phishing emails.")
    print("5. Install antivirus software and keep it updated.")

    # Add Risk Assessment Feature
    print("\nNow, let's assess your cybersecurity risk level.")
    risk_score = 0

    # Assign weights to each question
    weights = {
        "q1": 25,  # Backing up data
        "q2": 15,  # Strong passwords
        "q3": 30,  # Multi-factor authentication
        "q4": 20,  # Employee training
        "q5": 10   # System updates
    }

    # Ask the user risk-related questions
    print("\nAnswer the following questions with 'yes' or 'no':")

    q1 = input("Do you regularly back up your data? ").strip().lower()
    if q1 == "yes":
        risk_score += weights["q1"]

    q2 = input("Do you use strong, unique passwords for all systems? ").strip().lower()
    if q2 == "yes":
        risk_score += weights["q2"]

    q3 = input("Do you implement multi-factor authentication (MFA)? ").strip().lower()
    if q3 == "yes":
        risk_score += weights["q3"]

    q4 = input("Do you train your employees to recognize phishing emails? ").strip().lower()
    if q4 == "yes":
        risk_score += weights["q4"]

    q5 = input("Do you update and patch your systems regularly? ").strip().lower()
    if q5 == "yes":
        risk_score += weights["q5"]

    # Adjust risk score by industry multiplier
    adjusted_risk_score = risk_score * industry_multiplier
    adjusted_risk_score = min(adjusted_risk_score, 100)  # Cap the score at 100

    # Calculate risk level
    if adjusted_risk_score >= 80:
        risk_level = "Low"
    elif 50 <= adjusted_risk_score < 80:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    print(f"\nYour Cybersecurity Risk Score (Adjusted for Industry): {adjusted_risk_score:.1f}/100")
    print(f"Your Risk Level: {risk_level}")

    # Provide tailored advice based on risk level
    if risk_level == "High":
        print("\nYour business is at high risk of cyberattacks. Implement the recommended tips as soon as possible.")
    elif risk_level == "Moderate":
        print("\nYour risk level is moderate. Strengthen your cybersecurity measures to further reduce your risk.")
    else:
        print("\nYour risk level is low. Keep maintaining your good cybersecurity practices.")

    input("\nStay safe! Press Enter to exit.")
    
    def openfaqs():
        file_path = os.path.abspath('FAQs.html')
        webbrowser.open_new_tab(f'file://{file_path}')
        
    openfaqs()
    # Call the report generation script
    subprocess.run([sys.executable, 'report_generator.py', business_name, business_size.capitalize(), demand_range])

if __name__ == "__main__":
    main()
