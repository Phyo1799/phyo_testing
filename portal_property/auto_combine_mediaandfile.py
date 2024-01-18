import os
import requests
import json
import pandas as pd

# 1st Code: Upload files and capture IDs

url_upload = "https://dev-django-portal-admin.skyloov.com/portal/medias/create/"

# List of folder paths
folder_paths = [
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000CJXU5QAP"
    # Add more folder paths as needed
]

headers_upload = {}

# Dictionary to store the mapping of file names to file IDs
file_id_mapping = {}

for folder_path in folder_paths:
    # Set the payload name to be the folder name
    folder_name = os.path.basename(folder_path)
    payload_upload = {'name': folder_name}

    # Get a list of all files in the folder
    files = [(f, open(os.path.join(folder_path, f), 'rb')) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    uploaded_ids = []

    for file_name, file_data in files:
        current_file = [('file', (file_name, file_data))]
        response = requests.post(url_upload, headers=headers_upload, data=payload_upload, files=current_file)
        print(f"Uploaded {file_name}: {response.text}")

        # Assuming the response.text contains the ID information, adapt this based on the actual response structure
        file_id = response.json().get('id', None)
        uploaded_ids.append(file_id)

        # Map file name to file ID
        file_id_mapping[file_name] = file_id

    # Optionally, print the response for the last file
    # print(response.text)

    # 2nd Code: Use the captured IDs in the payload

    url_property_files = "https://dev-django-portal-admin.skyloov.com/portal/property-files/create/"

    payload_property_files = json.dumps({
        "images": uploaded_ids
    })
    headers_property_files = {
        'Content-Type': 'application/json'
    }

    response_property_files = requests.post(url_property_files, headers=headers_property_files, data=payload_property_files)

    print(response_property_files.text)

# Write the file IDs to an Excel file
excel_file_path = r"C:\Users\Phyo\Desktop\portal_property_allid.xlsx"

# Create a DataFrame from the file_id_mapping dictionary
df = pd.DataFrame(file_id_mapping.items(), columns=['file_name', 'file_uuid'])

# Save the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print("Excel file updated successfully.")
