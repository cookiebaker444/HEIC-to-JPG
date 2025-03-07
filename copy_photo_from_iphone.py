import os
import shutil

def copy_photos_from_iphone(source_folder, destination_folder):
    # Ensure destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through the iPhone DCIM folder
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.heic', '.mov', '.mp4')):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)

                try:
                    shutil.copy2(source_path, destination_path)
                    print(f"Copied: {file}")
                except Exception as e:
                    print(f"Failed to copy {file}: {e}")

# Define paths (update your iPhone's DCIM path accordingly)
iphone_photos_path = r"E:\DCIM"  # Replace with your actual iPhone drive letter
destination_path = r"C:\Users\YourUser\Pictures\iPhoneBackup"

# Run the copy function
copy_photos_from_iphone(iphone_photos_path, destination_path)
