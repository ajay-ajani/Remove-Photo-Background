import os
from pymatting import cutout

# Directory paths
input_directory = "./images/"
trimap_directory = "./create_trimap/images/results/"
output_directory = "final_output/"

# Get absolute paths based on the current working directory
input_directory = os.path.abspath(input_directory)
trimap_directory = os.path.abspath(trimap_directory)
output_directory = os.path.abspath(output_directory)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate over the files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # Get the file paths
        input_image_path = os.path.join(input_directory, filename)
        trimap_path = os.path.join(trimap_directory, filename)
        output_cutout_path = os.path.join(output_directory, filename)

        # Perform cutout
        cutout(input_image_path, trimap_path, output_cutout_path)
