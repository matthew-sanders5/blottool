from pathlib import Path
from typing import List
import numpy as np
import pandas as pd
from skimage import io as skio

from .models import ROI

def load_image(path: str) -> np.ndarray:
    path = Path(path)
    img = skio.imread(path.as_posix())

    # Convert to grayscale if needed
    if img.ndim == 3:
        img = img[..., :3].mean(axis=2)

    # INVERT because Western blots are dark-on-light
    # ImageJ internally treats dark = high intensity
    img = 255 - img

    return img.astype(float)

def load_rois_from_csv(path: str) -> List[ROI]:
    df = pd.read_csv(path)
    required = ["label", "x", "y", "width", "height"]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing required column '{col}' in ROI CSV")

    rois: List[ROI] = []

    for _, row in df.iterrows():
        rois.append(
            ROI(
                label=str(row["label"]),
                x=int(row["x"]),
                y=int(row["y"]),
                width=int(row["width"]),
                height=int(row["height"]),
                bg_x=int(row["bg_x"]) if "bg_x" in df.columns and not pd.isna(row["bg_x"]) else None,
                bg_y=int(row["bg_y"]) if "bg_y" in df.columns and not pd.isna(row["bg_y"]) else None,
                bg_width=int(row["bg_width"]) if "bg_width" in df.columns and not pd.isna(row["bg_width"]) else None,
                bg_height=int(row["bg_height"]) if "bg_height" in df.columns and not pd.isna(row["bg_height"]) else None,
            )
        )

    return rois
