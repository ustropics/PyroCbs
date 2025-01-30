import os
from PIL import Image, UnidentifiedImageError

fire_id = 'B03'

def resize_images(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get all image files in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        # Skip non-image files
        if not os.path.isfile(file_path) or not filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff', '.webp')):
            continue
        
        try:
            # Open the image and resize it to 25% of its original size
            with Image.open(file_path) as img:
                original_width, original_height = img.size
                new_width = int(original_width * 0.05)
                new_height = int(original_height * 0.05)
                resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
                
                # Save the resized image in the output directory
                output_path = os.path.join(output_dir, filename)
                resized_img.save(output_path)
                print(f"Resized and saved: {output_path}")
        
        except (UnidentifiedImageError, OSError) as e:
            # Log and skip problematic files
            print(f"Skipping file {filename}: {e}")

if __name__ == "__main__":
    # Replace with your directories
    input_directory = f"static/img/full-res/{fire_id}"
    output_directory = f"static/img/thumbnail/{fire_id}"

    resize_images(input_directory, output_directory)
