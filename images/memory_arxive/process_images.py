# This Python script processes the images in the current directory, adding a white border to them and resizing the full images

import os
from PIL import Image


def add_white_background(image_path, output_path):
    # Open the original image
    img = Image.open(image_path).convert("RGBA")

    # Resize with max width or height of 475, keeping aspect ratio
    max_size = (500, 500)
    img.thumbnail(max_size, Image.LANCZOS)  # In-place resize

    # Get image size
    width, height = img.size
    max_dim = int(max(width, height)*1.05)

    # Create a white background image (square)
    square_bg = Image.new("RGB", (max_dim, max_dim), (255, 255, 255))

    # Calculate top-left position to paste the original image
    x_offset = (max_dim - width) // 2
    y_offset = (max_dim - height) // 2

    # Paste image onto the center of white background
    square_bg.paste(img.convert("RGB"), (x_offset, y_offset))

    # Save result
    square_bg.save(output_path)
    print(f"Saved: {output_path}")

script_dir = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(script_dir):
    if file.endswith('.jpg') and not file.endswith('_white_border.jpg') and not file.endswith('_resized.jpg'):
        add_white_background(script_dir + "/" + file, script_dir + "/" + file[:-4] + "_white_border.jpg")

        # Resize original image to have a max height or width of 750px
        img = Image.open(script_dir + "/" + file)
        max_size = (750, 750)
        img.thumbnail(max_size, Image.LANCZOS)  # In-place resize
        img.save(script_dir + "/" + file[:-4] + "_resized.jpg")


