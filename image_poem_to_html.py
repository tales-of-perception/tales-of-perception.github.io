# This Python script takes an image/poem name, and creates the necessary html in order to insert into the html document.

# It also takes the original image and adds a white border to it ready for inserting into the glitched memories page

import os
from PIL import Image

poem_name = "Tongue twister 2"
markdown_file = "poems_and_images/" + poem_name + ".md"

# Check if image is jpg or png format
if os.path.isfile("poems_and_images/" + poem_name + ".jpg"):
    image_path = "poems_and_images/" + poem_name + ".jpg"
else:
    print("Cannot find poem image. Make sure it exists, and that it is in jpg file format.")
    os._exit(1)

def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

html_text = f"""
<div class="blog-single-post-thumb">
   <div class="blog-post-title">
       <h3 class="neuropol">{poem_name}</h3>
   </div>
   <img src="{image_path[:-4] + "_resized.jpg"}" class="img-responsive">
   <h3 class="neuropol" style="font-style: italic; font-size: 10px">X</h3>\n
"""

with open(markdown_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
if lines[-1] != '\n':
    lines.append('\n')

paragraphs = []
current_paragraph = []

for line in lines:
    stripped = line.strip()
    if stripped == "":
        if current_paragraph:
            paragraphs.append(current_paragraph)
            current_paragraph = []
    else:
        current_paragraph.append(stripped)

# Build HTML as a string
for para in paragraphs:
    html_text += '<p class="reduce-space">\n'
    for line in para:
        html_text += f'    {line}<br>\n'
    html_text += '</p>\n'

html_text += """
    <h3 class="neuropol" style="font-style: italic; font-size: 10px">X</h3>
       <p style="text-align: center; font-size: 20px; margin-top: 30px;" class="neuropol">
           <a href="glitched_memories.html">Back to Gallery</a>
       </p>
</div>
"""

print(html_text)

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

add_white_background(image_path, image_path[:-4] + "_white_border.jpg")

# Resize original image to have a max height or width of 750px

# Open the original image (make sure original image is jpg format
img = Image.open(image_path)
max_size = (750, 750)
img.thumbnail(max_size, Image.LANCZOS)  # In-place resize

img.save(image_path[:-4] + "_resized.jpg")