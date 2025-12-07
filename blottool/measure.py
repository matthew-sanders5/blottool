from typing import List, Dict, Any
import numpy as np
import pandas as pd

from .models import ROI

def _extract_patch(img: np.ndarray, x: int, y: int, width: int, height: int) -> np.ndarray:
    # Basic bounds safety – clip at image edges
    h, w = img.shape[:2]
    x_end = min(x + width, w)
    y_end = min(y + height, h)
    x = max(x, 0)
    y = max(y, 0)
    if x >= x_end or y >= y_end:
        raise ValueError(f"ROI out of bounds or zero-sized: x={x}, y={y}, w={width}, h={height}")
    return img[y:y_end, x:x_end]

def measure_bands(image: np.ndarray, rois: List[ROI]) -> pd.DataFrame:
    records: List[Dict[str, Any]] = []

    for roi in rois:
        patch = _extract_patch(image, roi.x, roi.y, roi.width, roi.height)
        area = patch.size
        sum_intensity = float(patch.sum())
        mean_intensity = float(patch.mean())

        bg_mean = None
        bg_sum = None
        bg_area = None
        corrected_sum = None
        corrected_mean = None

        if roi.bg_x is not None and roi.bg_y is not None and \
           roi.bg_width is not None and roi.bg_height is not None:

            bg_patch = _extract_patch(image, roi.bg_x, roi.bg_y, roi.bg_width, roi.bg_height)
            bg_area = bg_patch.size
            bg_sum = float(bg_patch.sum())
            bg_mean = float(bg_patch.mean())

            # Background-corrected integrated density = sum(signal - bg_mean)
            corrected_sum = sum_intensity - (bg_mean * area)
            corrected_mean = corrected_sum / area

        records.append(
            {
                "label": roi.label,
                "x": roi.x,
                "y": roi.y,
                "width": roi.width,
                "height": roi.height,
                "area_px": area,
                "sum_intensity": sum_intensity,
                "mean_intensity": mean_intensity,
                "bg_mean": bg_mean,
                "bg_sum": bg_sum,
                "bg_area_px": bg_area,
                "corrected_sum_intensity": corrected_sum,
                "corrected_mean_intensity": corrected_mean,
            }
        )

    return pd.DataFrame.from_records(records)
