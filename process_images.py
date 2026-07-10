import os
import glob
from PIL import Image

def process_image(input_path, output_path, target_width=1200, target_height=675, max_size_kb=100):
    print(f"Processing {input_path}...")
    try:
        img = Image.open(input_path)
        
        # Calculate target aspect ratio
        target_ratio = target_width / target_height
        img_ratio = img.width / img.height
        
        # Smart center crop
        if img_ratio > target_ratio:
            # Image is wider than target ratio
            new_width = int(img.height * target_ratio)
            left = (img.width - new_width) / 2
            top = 0
            right = (img.width + new_width) / 2
            bottom = img.height
        else:
            # Image is taller than target ratio
            new_height = int(img.width / target_ratio)
            left = 0
            top = (img.height - new_height) / 2
            right = img.width
            bottom = (img.height + new_height) / 2
            
        img = img.crop((left, top, right, bottom))
        
        # Resize to exactly 1200x675
        img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        # Save as webp and compress until < max_size_kb
        quality = 95
        while quality > 10:
            img.save(output_path, 'WEBP', quality=quality)
            size_kb = os.path.getsize(output_path) / 1024
            if size_kb < max_size_kb:
                print(f"Saved {output_path} at quality {quality} (Size: {size_kb:.2f}KB)")
                break
            quality -= 5
            
        if quality <= 10:
            print(f"Warning: Could not compress {output_path} below {max_size_kb}KB. Final size: {os.path.getsize(output_path)/1024:.2f}KB")
            
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    artifact_dir = r"C:\Users\amarl\.gemini\antigravity\brain\832e18a3-c8b2-4a96-8203-6d51daef6e49"
    project_img_dir = r"C:\Users\amarl\Documents\Davie concrete\images"
    
    # Process hero image
    hero_pattern = os.path.join(artifact_dir, "blog_driveway_hero_*.png")
    hero_files = glob.glob(hero_pattern)
    if hero_files:
        process_image(hero_files[-1], os.path.join(project_img_dir, "blog-driveway-hero.webp"))
        
    # Process inline 1
    inline1_pattern = os.path.join(artifact_dir, "blog_driveway_inline1_*.png")
    inline1_files = glob.glob(inline1_pattern)
    if inline1_files:
        process_image(inline1_files[-1], os.path.join(project_img_dir, "blog-driveway-inline1.webp"))
        
    # Process inline 2
    inline2_pattern = os.path.join(artifact_dir, "blog_driveway_inline2_*.png")
    inline2_files = glob.glob(inline2_pattern)
    if inline2_files:
        process_image(inline2_files[-1], os.path.join(project_img_dir, "blog-driveway-inline2.webp"))
