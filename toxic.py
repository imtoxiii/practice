import re

# Function to extract credentials for a particular URL
def extract_credentials(file_path, target_url):
    credentials = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into url, username/email, and password
            parts = line.strip().split(':')
            
            # Check if the line has exactly three parts
            if len(parts) == 3:
                url, username_email, password = parts
                
                # If the URL matches the target URL, store the credentials
                if target_url in url:
                    credentials.append(f"{username_email}:{password}")
    
    return credentials

# File path to the text document
file_path = r'C:\Users\imsum\Downloads\Telegram Desktop\urllof.txt'

# Target URL to search for
target_url = 'https://nullphp.net/'

# Get the extracted credentials
extracted_credentials = extract_credentials(file_path, target_url)

# Path to save the extracted credentials
output_file_path = r'C:\Users\imsum\Downloads\Telegram Desktop\extracted_credentials.txt'

# Write the extracted credentials to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for credential in extracted_credentials:
        output_file.write(credential + '\n')

# Inform the user that the credentials have been saved
print(f"Extracted credentials have been saved to {output_file_path}")
