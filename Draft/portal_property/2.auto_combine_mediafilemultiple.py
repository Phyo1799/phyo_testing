import os
import requests
import json

# 1st Code: Upload files and capture IDs

url_upload = "https://dev-django-portal-admin.skyloov.com/portal/medias/create/"

# List of folder paths
folder_paths = [
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F2katQAB",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F2kFgQAJ",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F2kILQAZ",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F2uVwQAJ",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F2v46QAB",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F345zQAB",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3a1xQAB",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3EbeQAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3EK9QAN",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3enjQAB",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3f4zQAB",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3Ix4QAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3J2iQAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3J3vQAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3J5jQAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3J6mQAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3J8xQAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3jb8QAB",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3jcQQAR",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3jegQAB",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3N02QAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3N0WQAV",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3QRMQA3",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3TYyQAN",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3ytSQAR",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000F3Zi0QAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GO09WQAT",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GOlesQAD",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GOlgVQAT",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GOlouQAD",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GPDf7QAH",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GPfkOQAT",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GQhHpQAL",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GQQuVQAX",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GQu2YQAT",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GQyr2QAD",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GQzM9QAL",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GQZQrQAP",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GR5EeQAL",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GRMmfQAH",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000GRW2AQAX",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000HfAhVQAV",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000HhfqAQAR",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000HhfrNQAR",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000HhFuFQAV",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000HhHnqQAF",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000JAFyLQAX",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000JAka5QAD",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000JCjPHQA1",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000JCKg5QAH",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000JCKgPQAX",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0k8Z00000JCKgZQAX",
    r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\ENB_Data\Pictures\a0kPa000001rOV3IAM",

    # Add more folder paths as needed
]

headers_upload = {}

# Define top_level_ids_summary outside the loop
top_level_ids_summary = []

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

    # Print the top-level ID from the response
    top_level_id = response_property_files.json().get('id', None)
    top_level_ids_summary.append(top_level_id)
    print(f"Top-level ID for folder '{folder_name}': {top_level_id}")
    print(response_property_files.text)

# Print the summary of top-level IDs
print("\nTop-level IDs for folders:")
for top_level_id in top_level_ids_summary:
    print(f"- {top_level_id}")
