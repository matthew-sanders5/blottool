import argparse
from pathlib import Path

from .io import load_image, load_rois_from_csv
from .measure import measure_bands
from .visualize import overlay_rois

def main():
    parser = argparse.ArgumentParser(description="Simple western blot densitometry tool.")
    parser.add_argument("--image", required=True, help="Path to blot image (tif/png/jpg).")
    parser.add_argument("--rois", required=True, help="Path to ROI CSV.")
    parser.add_argument("--out", required=True, help="Path to output CSV.")
    parser.add_argument("--overlay", help="Optional path to save overlay PNG.")
    args = parser.parse_args()

    img = load_image(args.image)
    rois = load_rois_from_csv(args.rois)
    df = measure_bands(img, rois)
    df.to_csv(args.out, index=False)

    if args.overlay:
        overlay_rois(img, rois, args.overlay)

if __name__ == "__main__":
    main()
