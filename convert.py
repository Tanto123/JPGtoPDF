from PIL import Image
import sys

def jpgs_to_pdf(image_paths, output_pdf_path):
    # Open the first image and convert it to RGB
    first_image = Image.open(image_paths[0]).convert('RGB')
    
    # Open the rest of the images and convert to RGB
    images = [Image.open(img).convert('RGB') for img in image_paths[1:]]
    
    # Save all images into a single PDF file
    first_image.save(output_pdf_path, save_all=True, append_images=images)
    print(f"PDF saved as {output_pdf_path}")

if __name__ == "__main__":
    # Example usage: python convert_jpg_to_pdf.py img1.jpg img2.jpg output.pdf
    if len(sys.argv) < 3:
        print("Usage: python convert_jpg_to_pdf.py <image1.jpg> [<image2.jpg> ...] <output.pdf>")
        sys.exit(1)

    *input_images, output_pdf = sys.argv[1:]
    jpgs_to_pdf(input_images, output_pdf)
