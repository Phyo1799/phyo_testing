import os
import shutil

# Source and destination directories
source_dir = 'C:/Users/Phyo/OneDrive - Skyloov Property Portal/Skyloov-Phyo/Master_Data/Admin_Portal_Documents/Facilities/Facilities_Icons/Skyloov Design System/Bold'
destination_dir = source_dir  # The same directory as source, change it if you want to move the files elsewhere

# Loop through each subfolder in the "Bold" folder
for foldername in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, foldername)

    # Check if it's a directory and not a file
    if os.path.isdir(folder_path):
        # Loop through each file in the subfolder
        for filename in os.listdir(folder_path):
            # Check if the file is a PNG file
            if filename.lower().endswith('.png'):
                # Move the PNG file to the "Bold" folder
                source_file = os.path.join(folder_path, filename)
                destination_file = os.path.join(destination_dir, filename)
                shutil.move(source_file, destination_file)

print("PNG files moved to", destination_dir)
