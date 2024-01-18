import requests
import json
import csv

# File path to your CSV
csv_file_path = r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\propertyidfileidupdate.csv"

url_base = "https://dev-django-portal-admin.skyloov.com/portal/properties/"

# Read CSV file
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Loop through each row in the CSV
    for row in reader:
        # Construct the URL for each property_id
        url = f"{url_base}{row['property_id']}/update/partial/"

        # Prepare payload with user_id and files
        payload = json.dumps({
            "user_id": row['file_id'],
            "files": "f60626ad-a7ed-4ac0-8589-0d9a2cdedfe0"
        })

        headers = {'Content-Type': 'application/json'}

        # Make the request
        response = requests.patch(url, headers=headers, data=payload)

        # Print the response
        print(f"Property ID: {row['property_id']}, File ID: {row['file_id']}")
        print(response.text)
        print("-" * 50)
