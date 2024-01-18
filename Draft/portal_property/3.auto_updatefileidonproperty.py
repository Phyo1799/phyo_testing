import requests
import json
import csv

# Define the file path to your CSV file
file_path = r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\enb_docmentsforpythons\propertyidfileidupdate.csv"

#"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\enb_docmentsforpythons\propertyidfileidupdate.csv"

url_base = "https://dev-django-portal-admin.skyloov.com/portal/properties/{}/update/partial/"

headers = {
    'Content-Type': 'application/json'
}

# Open the CSV file and read its contents
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header row if it exists
    next(csvreader, None)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Ensure the row has at least two elements
        if len(row) < 2:
            print("Error: Each row must have at least two elements.")
            exit()

        property_id = row[0]  # Assuming the first column is property_id
        file_id = row[1]      # Assuming the second column is file_id

        # Construct the URL using property_id
        url = url_base.format(property_id)

        # Construct the payload with the appropriate file_id
        payload = json.dumps({
            "user_id": "f6d3fe4e-0cef-4dbb-ae71-9dd8751197a0",
            "files": file_id  # This will use the file_id from the current row
        })

        # Send a PATCH request to the constructed URL
        response = requests.request("PATCH", url, headers=headers, data=payload)

        # Print the response text
        print(f"For Property ID {property_id} and File ID {file_id}:")
        print(response.text)
        print("------")  # Just to separate each response for clarity
