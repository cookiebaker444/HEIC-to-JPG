import os
from pillow_heif import open_heif
from PIL import Image

def convert_all_heic_to_jpg(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".heic"):
            input_path = os.path.join(folder_path, file_name)
            output_path = os.path.join(folder_path, file_name.rsplit(".", 1)[0] + ".jpg")

            try:
                heif_image = open_heif(input_path)
                image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)
                image.save(output_path, "JPEG")
                print(f"Converted: {file_name} → {os.path.basename(output_path)}")
            except Exception as e:
                print(f"Failed to convert {file_name}: {e}")

if __name__ == "__main__":
    convert_all_heic_to_jpg("/app")
