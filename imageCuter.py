import os
import pygame

# Initialize pygame
pygame.init()

# Function to split and save an image
def split_image(image_path, output_folder, max_size, start_number=1):
    # Load the image
    image = pygame.image.load(image_path)

    # Get the dimensions of the image
    width, height = image.get_size()

    # Calculate how many pieces the image should be split into
    cols = (width + max_size - 1) // max_size  # Number of horizontal pieces
    rows = (height + max_size - 1) // max_size  # Number of vertical pieces

    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Split the image into smaller sections
    image_number = start_number
    for row in range(rows):
        for col in range(cols):
            # Define the area of the sub-image (slice)
            x = col * max_size
            y = row * max_size
            rect = pygame.Rect(x, y, min(max_size, width - x), min(max_size, height - y))

            # Create a new surface for the sub-image
            sub_image = pygame.Surface(rect.size)
            sub_image.blit(image, (0, 0), rect)

            # Save the sub-image to the output folder
            sub_image_path = os.path.join(output_folder, f'image_{image_number}.png')
            pygame.image.save(sub_image, sub_image_path)
            print(f'Saved: {sub_image_path}')
            image_number += 1

# Function to load all images from a directory and split them
def process_directory(input_folder, output_folder, max_size, start_number=1):
    # Iterate through all files in the input directory
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Filter for image files
            image_path = os.path.join(input_folder, filename)
            print(f'Processing: {image_path}')
            split_image(image_path, output_folder, max_size, start_number)

# Example usage
input_folder = "path_to_input_directory"  # Folder containing the images to be split
output_folder = "output_images"  # Folder where the split images will be saved
max_size = 512  # Maximum width and height of each split image (square size)
start_number = 1  # Starting number for naming the images

# Call the function to process the directory
process_directory(input_folder, output_folder, max_size, start_number)

# Quit pygame after completion
pygame.quit()
