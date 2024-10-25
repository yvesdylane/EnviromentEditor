import pygame
import os

def Load_Tiles(directory):
    # Store tiles in a list
    img_list = []

    # Get the root directory of the current script
    root_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    img_dir = os.path.join(root_dir, directory)  # Construct the image directory path

    # Loop through all files in the specified directory
    for filename in os.listdir(img_dir):
        # Check if the file is a PNG, JPG, or JPEG
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Load the image
            img_path = os.path.join(img_dir, filename)  # Get the full path
            img = pygame.image.load(img_path).convert_alpha()

            # Append a tuple of (image, filename) to the list
            img_list.append((img, filename))

    return img_list

def load_images(directory):
    img_list = []

    for i in range (1, 89):
        img = pygame.image.load(f'output/images/{i}.png').convert_alpha()

        img_list.append((img, f'images/{i}.png'))

    return  img_list
