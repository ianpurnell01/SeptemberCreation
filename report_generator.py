import sys
import os
#Generating the report
def generate_report_pdf(business_name, business_size, demand_range):
#HTML content for the report
    html_content = f'''<!DOCTYPE html>
<html>
<head><title>Ransomware Demand Report</title></head>
<body>
<h1>Ransomware Demand Report</h1>
<p>Business Name: {business_name}</p>
<p>Business Size: {business_size}</p>
<p>Estimated Ransomware Demand Range: {demand_range}</p>
<h2>Cybersecurity Tips:</h2>
<ul>
<li>Regularly backup your data.</li>
<li>Use strong, unique passwords.</li>
<li>Implement multi-factor authentication (MFA).</li>
<li>Train employees to recognize phishing emails.</li>
<li>Install antivirus software and keep it updated.</li>
</ul>
</body>
</html>'''
    
    # Output HTML to a temporary file
    with open('report.html', 'w') as file:
        file.write(html_content)

    # Convert HTML to PDF using wkhtmltopdf
    os.system('wkhtmltopdf report.html ransom_report.pdf')
    os.remove('report.html')
    
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_report.py <business_name> <business_size> <demand_range>")
        sys.exit(1)

    _, business_name, business_size, demand_range = sys.argv
    generate_report_pdf(business_name, business_size, demand_range)