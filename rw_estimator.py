import time
import webbrowser
import os


# Function to generate the updated HTML report
def generate_report_with_risk(business_name, business_size, demand_range, risk_level, answers):
    # HTML content for the report
    html_content = f'''<!DOCTYPE html>
<html>
<head>
    <title>Ransomware Demand Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
        h1, h2 {{ color: #2c3e50; }}
        ul {{ padding-left: 20px; }}
        li {{ margin-bottom: 10px; }}
        .risk-level {{ font-weight: bold; color: {'#27ae60' if risk_level == 'Low' else '#f39c12' if risk_level == 'Moderate' else '#c0392b'}; }}
    </style>
</head>
<body>
<h1>Ransomware Demand Report</h1>
<p><strong>Business Name:</strong> {business_name}</p>
<p><strong>Business Size:</strong> {business_size}</p>
<p><strong>Estimated Ransomware Demand Range:</strong> {demand_range}</p>
<p><strong>Risk Level:</strong> <span class="risk-level">{risk_level}</span></p>

<h2>Answers Contributing to Risk Level:</h2>
<ul>
'''
    # Add each question and its corresponding answer to the HTML
    for question, answer in answers.items():
        html_content += f'<li><strong>{question}:</strong> {answer.capitalize()}</li>'

    html_content += '''
</ul>

<h2>Cybersecurity Tips:</h2>
    <ul>
        <li>
            <strong>Regularly backup your data.</strong><br>
            Use cloud-based services or external drives to back up your important files.<br>
            Follow the <strong>3-2-1 rule</strong>: Have three copies of your data, on two different types of storage, with one copy stored offsite.<br>
            <a href="https://www.pcworld.com/article/backup-your-data-guide" target="_blank">Learn more about backing up your data</a>.
        </li>
        <li>
            <strong>Use strong, unique passwords.</strong><br>
            Tools like password managers can help you generate and store secure passwords.<br>
            Avoid reusing passwords across multiple accounts.<br>
            <a href="https://www.nist.gov/publications/digital-identity-guidelines" target="_blank">Learn more about password best practices</a>.
        </li>
        <li>
            <strong>Implement multi-factor authentication (MFA).</strong><br>
            Add an extra layer of security by requiring a second form of identification (e.g., phone app, SMS code).<br>
            Many services like Google, Microsoft, and banks provide MFA options.<br>
            <a href="https://www.cisa.gov/mfa" target="_blank">Learn more about multi-factor authentication</a>.
        </li>
        <li>
            <strong>Train employees to recognize phishing emails.</strong><br>
            Regular training sessions can reduce the likelihood of successful phishing attacks.<br>
            Be cautious with unexpected emails, especially those requesting sensitive information.<br>
            <a href="https://www.phishingbox.com/" target="_blank">Learn more about phishing awareness training</a>.
        </li>
        <li>
            <strong>Install antivirus software and keep it updated.</strong><br>
            Ensure your antivirus software is configured to update automatically and scan regularly.<br>
            Choose reputable antivirus programs like Norton, McAfee, or Bitdefender.<br>
            <a href="https://www.pcmag.com/picks/the-best-antivirus-protection" target="_blank">Learn more about the best antivirus software</a>.
        </li>
    </ul>
</body>
</html>'''

    # Output HTML to a file
    with open('updated_report.html', 'w') as file:
        file.write(html_content)

# Main program
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

    # Gather answers for the report
    answers = {
        "Do you regularly back up your data?": q1,
        "Do you use strong, unique passwords for all systems?": q2,
        "Do you implement multi-factor authentication (MFA)?": q3,
        "Do you train employees to recognize phishing emails?": q4,
        "Do you update and patch your systems regularly?": q5
    }
    # generate_report_pdf(business_name, business_size.capitalize(), demand_range, risk_level, answers)
    # pdf_file_path = os.path.abspath('ransom_report.pdf')
    # print(f"\nPDF report generated successfully: {pdf_file_path}")

    # Generate and open the HTML report
    generate_report_with_risk(business_name, business_size.capitalize(), demand_range, risk_level, answers)
    file_path = os.path.abspath('updated_report.html')
    webbrowser.open_new_tab(f'file://{file_path}')

if __name__ == "__main__":
    main()
