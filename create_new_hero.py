import os
import glob
from PIL import Image

artifact_dir = r"C:\Users\amarl\.gemini\antigravity\brain\832e18a3-c8b2-4a96-8203-6d51daef6e49"
project_img_dir = r"C:\Users\amarl\Documents\Davie concrete\images"

# Find an alternate unused image we generated earlier
inline_imgs = glob.glob(os.path.join(artifact_dir, "blog_driveway_inline1_*.png"))
if inline_imgs:
    img_path = inline_imgs[-1]
    output_path = os.path.join(project_img_dir, "new-hero.webp")
    print(f"Using {img_path} as new hero...")
    try:
        img = Image.open(img_path)
        img = img.resize((1200, 675), Image.Resampling.LANCZOS)
        img.save(output_path, 'WEBP', quality=85)
        print("Done creating new hero image.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("No alternate images found.")
