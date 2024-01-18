import os
import pandas as pd
import requests
import time  # Import the time module for adding delays

# Path to the CSV file
csv_path = r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\enb_docmentsforpythons\url_media.csv"

# Output folder
output_folder = r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Download images and save with unique names
for index, row in df.iterrows():
    property_id = str(row['PropertyID'])
    url = row['URL']

    # Download the image
    response = requests.get(url)

    # Add a delay of 1 second between requests
    time.sleep(1)

    if response.status_code == 200:
        # Save the image with a unique name in a folder with PropertyID
        folder_path = os.path.join(output_folder, property_id)
        os.makedirs(folder_path, exist_ok=True)

        # Get the index within the current folder
        folder_index = index % len(df[df['PropertyID'] == property_id])

        # Save the image with a unique name (e.g., 1.jpg, 2.jpg)
        file_name = f"{property_id}_{folder_index + 1}.jpg"
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded: {url} -> {file_path}")
    else:
        print(f"Failed to download: {url}")

print("Download process completed.")
