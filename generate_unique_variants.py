import os
import glob
from PIL import Image, ImageEnhance, ImageOps

def process_variant(input_path, output_path, operation, crop_pos, target_width=1200, target_height=675, max_size_kb=100):
    print(f"Creating variant {output_path} from {input_path}...")
    try:
        img = Image.open(input_path)
        
        # Apply operation
        if operation == 'flip_lr':
            img = ImageOps.mirror(img)
        elif operation == 'flip_tb':
            img = ImageOps.flip(img)
        elif operation == 'darken':
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(0.7)
        elif operation == 'contrast':
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.5)
            
        # Calculate target aspect ratio
        target_ratio = target_width / target_height
        img_ratio = img.width / img.height
        
        # Smart crop with offset
        if img_ratio > target_ratio:
            new_width = int(img.height * target_ratio)
            if crop_pos == 'left':
                left, right = 0, new_width
            elif crop_pos == 'right':
                left, right = img.width - new_width, img.width
            else: # center
                left = (img.width - new_width) / 2
                right = (img.width + new_width) / 2
            top, bottom = 0, img.height
        else:
            new_height = int(img.width / target_ratio)
            if crop_pos == 'top':
                top, bottom = 0, new_height
            elif crop_pos == 'bottom':
                top, bottom = img.height - new_height, img.height
            else: # center
                top = (img.height - new_height) / 2
                bottom = (img.height + new_height) / 2
            left, right = 0, img.width
            
        img = img.crop((left, top, right, bottom))
        img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        # Save as webp
        quality = 95
        while quality > 10:
            img.save(output_path, 'WEBP', quality=quality)
            size_kb = os.path.getsize(output_path) / 1024
            if size_kb < max_size_kb:
                break
            quality -= 5
            
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    artifact_dir = r"C:\Users\amarl\.gemini\antigravity\brain\832e18a3-c8b2-4a96-8203-6d51daef6e49"
    project_img_dir = r"C:\Users\amarl\Documents\Davie concrete\images"
    
    # Base images
    stamped_base = glob.glob(os.path.join(artifact_dir, "stamped_patio_davie_*.png"))[-1]
    hero_base = glob.glob(os.path.join(artifact_dir, "hero_concrete_davie_*.png"))[-1]
    inline1_base = glob.glob(os.path.join(artifact_dir, "blog_driveway_inline1_*.png"))[-1]
    inline2_base = glob.glob(os.path.join(artifact_dir, "blog_driveway_inline2_*.png"))[-1]
    
    # Blog 2: Top Stamped Concrete Patterns
    process_variant(stamped_base, os.path.join(project_img_dir, "blog-stamped-thumb.webp"), 'flip_lr', 'left')
    
    # Blog 3: Mudjacking vs Polyurethane
    process_variant(hero_base, os.path.join(project_img_dir, "blog-mudjacking-thumb.webp"), 'none', 'right')
    
    # Blog 4: Foundation Waterproofing
    process_variant(inline2_base, os.path.join(project_img_dir, "blog-waterproofing-thumb.webp"), 'darken', 'left')
    
    # Blog 5: Ready Mix Concrete Grades
    process_variant(inline1_base, os.path.join(project_img_dir, "blog-readymix-thumb.webp"), 'contrast', 'center')
    
    # Blog 6: Process of Concrete Polishing
    process_variant(stamped_base, os.path.join(project_img_dir, "blog-polishing-thumb.webp"), 'contrast', 'right')
    
    # Homepage Uniques
    process_variant(hero_base, os.path.join(project_img_dir, "cta-bg.webp"), 'darken', 'center')
    process_variant(inline2_base, os.path.join(project_img_dir, "project-driveway.webp"), 'none', 'right')
    process_variant(stamped_base, os.path.join(project_img_dir, "project-patio.webp"), 'none', 'left')
    process_variant(hero_base, os.path.join(project_img_dir, "project-repair.webp"), 'none', 'right')
    process_variant(inline1_base, os.path.join(project_img_dir, "project-waterproofing.webp"), 'none', 'left')
    
    print("Done generating unique image variants!")
