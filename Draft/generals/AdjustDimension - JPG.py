from PIL import Image, ImageOps
import os

# Input and output directories
input_dir = 'C:/Users/Phyo/OneDrive - Skyloov Property Portal/Skyloov-Phyo/Admin_Portal_Documents/Developers'
output_dir = 'C:/Users/Phyo/OneDrive - Skyloov Property Portal/Skyloov-Phyo/Admin_Portal_Documents/Developer(FixedSizes) - JPG'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Desired size for the square canvas
canvas_size = (400, 400)  # Adjust this to your desired square size

# List of accepted file extensions
valid_extensions = ('.jpg', '.webp', '.jpeg', '.png', '.jfif')

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    # Check if the file has one of the valid extensions
    if filename.lower().endswith(valid_extensions):
        # Open the image
        with Image.open(os.path.join(input_dir, filename)) as img:
            # Ensure the image is in RGB mode
            img = img.convert('RGB')
            
            # Create a square canvas with a white background
            square_img = ImageOps.pad(img, canvas_size, method=Image.BOX, color='white')

            # Save the modified image to the output directory in JPG format
            output_filename = os.path.splitext(filename)[0] + '.jpg'
            square_img.save(os.path.join(output_dir, output_filename), format='JPEG')

print("Images converted and saved to", output_dir)
