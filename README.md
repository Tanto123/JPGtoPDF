
# JPGtoPDF

A simple Python tool to convert JPG images into a single PDF file.

## Description

JPGtoPDF is a lightweight script that allows you to convert one or multiple JPG images into a PDF document. It uses the Pillow library to open images and save them as a PDF, supporting multi-page PDFs by combining multiple images.

## Features

- Convert single or multiple JPG images to PDF.
- Automatically handles image conversion to RGB mode.
- Saves all images into one PDF file.
- Easy to use via command line or as a Python module.

## Requirements

- Python 3.x
- Pillow library

## Installation

Install the Pillow library using pip:

```
pip install Pillow
```

## Usage

### Command line example

Run the script with your images and specify the output PDF filename:

```
python convert.py output.pdf image1.jpg image2.jpg image3.jpg
```

### Example Python code

```
from PIL import Image
import sys

def jpgs_to_pdf(image_paths, output_pdf_path):
    images = [Image.open(img).convert('RGB') for img in image_paths]
    first_image = images.pop(0)
    first_image.save(output_pdf_path, save_all=True, append_images=images)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert.py output.pdf image1.jpg [image2.jpg ...]")
        sys.exit(1)
    output_pdf = sys.argv[1]
    input_images = sys.argv[2:]
    jpgs_to_pdf(input_images, output_pdf)
```

## Notes

- All input images should be in JPG format.
- Images are converted to RGB mode to ensure PDF compatibility.
- The output PDF will contain all images as separate pages in the order provided.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

