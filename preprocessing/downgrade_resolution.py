from PIL import Image
import os

def resize_images_in_directory(directory, output_size):
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                resized_img = img.resize(output_size, Image.Resampling.LANCZOS)
                resized_img.save(filepath)

directory = './STOP_MODEL/STOP_tub'
resize_images_in_directory(directory, (160, 120))  # (width, height)