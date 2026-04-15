"""
WSI Loader Script
Supports:
- .svs, .mrxs via OpenSlide
- .dcm via pydicom

requirements:
openslide-python
pydicom
pillow
numpy
Example : python load_wsi.py --path/to/file

Author: Solmaz Haddady
"""

import os
from pathlib import Path
import argpars
# --- OpenSlide for SVS / MRXS ---
try:
    import openslide
except ImportError:
    openslide = None

# --- DICOM ---
try:
    import pydicom
except ImportError:
    pydicom = None


def load_openslide_wsi(wsi_path):
    """Load SVS / MRXS using OpenSlide"""
    if openslide is None:
        raise ImportError("OpenSlide is not installed.")

    slide = openslide.OpenSlide(wsi_path)

    print("=== OpenSlide WSI Info ===")
    print(f"Dimensions: {slide.dimensions}")
    print(f"Levels: {slide.level_count}")
    print(f"Downsamples: {slide.level_downsamples}")

    # Read a small region (top-left corner)
    region = slide.read_region((0, 0), level=0, size=(512, 512))
    return region


def load_dicom_wsi(wsi_path):
    """Load DICOM WSI using pydicom"""
    if pydicom is None:
        raise ImportError("pydicom is not installed.")

    ds = pydicom.dcmread(wsi_path)

    print("=== DICOM WSI Info ===")
    print(f"Patient ID: {ds.get('PatientID', 'N/A')}")
    print(f"Modality: {ds.get('Modality', 'N/A')}")

    if hasattr(ds, "pixel_array"):
        img = ds.pixel_array
        print(f"Image shape: {img.shape}")
        return img
    else:
        print("No pixel data found.")
        return None


def load_wsi(wsi_path):
    """General loader based on file extension"""
    ext = Path(wsi_path).suffix.lower()

    if ext in [".svs", ".mrxs"]:
        return load_openslide_wsi(wsi_path)

    elif ext in [".dcm"]:
        return load_dicom_wsi(wsi_path)

    else:
        raise ValueError(f"Unsupported format: {ext}")


if __name__ == "__main__":
  

    parser = argparse.ArgumentParser(description="Load WSI file")
    parser.add_argument("--path", type=str, required=True, help="Path to WSI file")

    args = parser.parse_args()

    result = load_wsi(args.path)

    print("WSI loaded successfully.")


