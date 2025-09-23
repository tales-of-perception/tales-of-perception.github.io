from PIL import Image

def add_white_background(image_path, output_path):
    # Open the original image
    img = Image.open(image_path).convert("RGBA")

    # Resize with max width or height of 475, keeping aspect ratio
    max_size = (500, 500)
    img.thumbnail(max_size, Image.LANCZOS)  # In-place resize

    # Get image size
    width, height = img.size
    max_dim = int(max(width, height) * 1.05)

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

# image_name = "poem_7.jpg"
# # Example usage
# add_white_background(image_name, image_name[:-4] + "_white_border.jpg")

for image_name in [
    "poem_12.jpg",
    "poem_13.jpg",
    "poem_14.jpg",]:
    
    add_white_background(image_name, image_name[:-4] + "_white_border.jpg")
    
    # Open the original image
    img = Image.open(image_name).convert("RGBA")

    # Resize with max width or height of 500, keeping aspect ratio
    max_size = (500, 500)
    img.thumbnail(max_size, Image.LANCZOS)  # In-place resize

    img.save(image_name[:-4] + "_resized.png")

