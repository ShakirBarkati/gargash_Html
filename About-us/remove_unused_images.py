import os
import re

# Project ke main folder ka path (change if needed)
project_path = "F:\Projects\Gargash HTML\About-us"

# Images folder ka path
image_folder = os.path.join(project_path, "img")

# Ye extensions wali images ko check karega
image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")

# Function to scan all project files
def get_used_images():
    used_images = set()
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith((".html", ".css", ".js", ".ejs", ".php")):  # Change extensions as needed
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for image in os.listdir(image_folder):
                        if image.endswith(image_extensions) and re.search(r"\b" + re.escape(image) + r"\b", content):
                            used_images.add(image)
    return used_images

# Function to delete unused images
def delete_unused_images():
    used_images = get_used_images()
    for image in os.listdir(image_folder):
        if image.endswith(image_extensions) and image not in used_images:
            os.remove(os.path.join(image_folder, image))
            print(f"Deleted: {image}")

delete_unused_images()
print("✅ Unused images deleted successfully!")
