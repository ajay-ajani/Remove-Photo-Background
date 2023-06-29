import os
from pymatting import cutout

def perform_image_cutout(input_directory, trimap_directory, output_directory):
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

# Example usage
#input_dir = "./images/"
#trimap_dir = "./create_trimap/images/results/"
#output_dir = "./final_output/"

#perform_image_cutout(input_dir, trimap_dir, output_dir)

