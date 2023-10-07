from PIL import Image
import os

directory_path = os.path.join(os.path.dirname(__file__), "../logo")
target_directory_path = os.path.join(os.path.dirname(__file__), "../resized_logo")

if not os.path.exists(target_directory_path):
    os.mkdir(target_directory_path)

target_width, target_height = 100, 100

for filename in os.listdir(directory_path):
    if filename.endswith(".png"):
        image_path = os.path.join(directory_path, filename)
        target_image_path = os.path.join(target_directory_path, filename)
        with Image.open(image_path) as img:
            width, height = img.size

            if width > target_width and height > target_height:
                resized_img = img.resize((target_width, target_height))
                resized_img.save(target_image_path)

                print(
                    f"Resized: {filename} from {width}x{height} to {target_width}x{target_height}"
                )
            else:
                # Copy the image to the target directory
                os.system(f"cp {image_path} {target_image_path}")
