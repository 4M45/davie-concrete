import os
import urllib.request
from PIL import Image

def download_and_process(url, output_path, target_width, target_height, max_kb):
    print(f"Downloading from {url}...")
    temp_path = "temp_download.jpg"
    
    # Add headers to avoid 403 Forbidden
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(temp_path, 'wb') as out_file:
        out_file.write(response.read())
        
    try:
        img = Image.open(temp_path).convert('RGB')
        img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        quality = 95
        while quality > 10:
            img.save(output_path, 'WEBP', quality=quality)
            size_kb = os.path.getsize(output_path) / 1024
            if size_kb < max_kb:
                break
            quality -= 5
            
        print(f"Saved {output_path} ({size_kb:.1f} KB)")
    except Exception as e:
        print(f"Error processing image: {e}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    out_dir = r"C:\Users\amarl\Documents\Davie concrete\images"
    
    # Large images
    download_and_process("https://loremflickr.com/1200/675/concrete,driveway", os.path.join(out_dir, "stock-hero.webp"), 1200, 675, 100)
    download_and_process("https://loremflickr.com/1200/675/concrete,paving", os.path.join(out_dir, "stock-proj1.webp"), 1200, 675, 100)
    download_and_process("https://loremflickr.com/1200/675/patio,concrete", os.path.join(out_dir, "stock-proj2.webp"), 1200, 675, 100)
    download_and_process("https://loremflickr.com/1200/675/concrete,repair", os.path.join(out_dir, "stock-proj3.webp"), 1200, 675, 100)
    download_and_process("https://loremflickr.com/1200/675/foundation,wall", os.path.join(out_dir, "stock-proj4.webp"), 1200, 675, 100)
    
    # Portrait images
    download_and_process("https://loremflickr.com/200/200/headshot,man", os.path.join(out_dir, "portrait-1.webp"), 200, 200, 30)
    download_and_process("https://loremflickr.com/200/200/headshot,woman", os.path.join(out_dir, "portrait-2.webp"), 200, 200, 30)
    download_and_process("https://loremflickr.com/200/200/face,person", os.path.join(out_dir, "portrait-3.webp"), 200, 200, 30)
    
    print("All stock images downloaded and processed.")
