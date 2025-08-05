from PIL import Image

def add_white_background(image_path, output_path):
    # Open the original image
    img = Image.open(image_path).convert("RGBA")

    # Get original size
    width, height = img.size
    max_dim = int(max(width, height) * 1.05)

    # Create a white background image (square)
    square_bg = Image.new("RGB", (max_dim, max_dim), (255, 255, 255))

    # Calculate top-left position to paste the original image
    x_offset = (max_dim + 100 - width) // 2
    y_offset = (max_dim - height) // 2

    # Paste image onto the center of white background
    square_bg.paste(img.convert("RGB"), (x_offset, y_offset))

    # Save result
    square_bg.save(output_path)
    print(f"Saved: {output_path}")

image_name = "poem_7.jpg"
# Example usage
add_white_background(image_name, image_name[:-4] + "_white_border.jpg")