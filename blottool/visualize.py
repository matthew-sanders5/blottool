from typing import List
import numpy as np
import matplotlib.pyplot as plt

from .models import ROI

def overlay_rois(image: np.ndarray, rois: List[ROI], out_path: str) -> None:
    fig, ax = plt.subplots()
    ax.imshow(image, cmap="gray")  # don't overthink color; grayscale is fine

    for roi in rois:
        rect = plt.Rectangle(
            (roi.x, roi.y),
            roi.width,
            roi.height,
            fill=False,
            linewidth=1.5,
	    edgecolor="white"
        )
        ax.add_patch(rect)
        ax.text(roi.x, roi.y - 2, roi.label, fontsize=6)

        if roi.bg_x is not None:
            bg_rect = plt.Rectangle(
                (roi.bg_x, roi.bg_y),
                roi.bg_width,
                roi.bg_height,
                fill=False,
                linestyle="dashed",
                linewidth=1.0
            )
            ax.add_patch(bg_rect)

    ax.axis("off")
    fig.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
