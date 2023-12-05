from PIL import Image
import os

def crop_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                width, height = img.size
                cropped_img = img.crop((0, 50, width, height))
                cropped_img.save(img_path)

folder_path = '../../../STOP_MODEL/STOP_tub_cropped'
crop_images_in_folder(folder_path)
