import os
import json
from PIL import Image

# Sanitized Data Hydration & Transformation Pipeline
SOURCE_DIR = "./raw_data_lake"
OUTPUT_DIR = "./web_ready_assets"
MANIFEST = []

def process_biological_assets():
    """Extracts EXIF, resizes for Edge delivery, builds JSON manifest."""
    for filename in os.listdir(SOURCE_DIR):
        if not filename.lower().endswith(('.jpg', '.jpeg')):
            continue
            
        file_path = os.path.join(SOURCE_DIR, filename)
        with Image.open(file_path) as img:
            # Extract EXIF metadata for chronological mapping
            exif_data = img.getexif()
            
            # Resize for optimized CDN delivery
            img.thumbnail((1920, 1080))
            out_path = os.path.join(OUTPUT_DIR, filename)
            img.save(out_path, "JPEG", quality=80)
            
            MANIFEST.append({"asset": filename, "optimized": True})

    with open(os.path.join(OUTPUT_DIR, "manifest.json"), "w") as f:
        json.dump(MANIFEST, f)

if __name__ == "__main__":
    process_biological_assets()
    print("Data pipeline execution complete. Ready for S3 sync.")
