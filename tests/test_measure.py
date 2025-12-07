import numpy as np
from blottool.models import ROI
from blottool.measure import measure_bands

def test_background_subtraction():
    # Image 20x10
    img = np.zeros((20, 10), dtype=float)
    # Signal region: y 0–10, value 100
    img[0:10, :] = 100.0
    # Background region: y 10–20, value 10
    img[10:20, :] = 10.0

    roi = ROI(
        label="band",
        x=0,
        y=0,
        width=10,
        height=10,
        bg_x=0,
        bg_y=10,
        bg_width=10,
        bg_height=10,
    )

    df = measure_bands(img, [roi])
    row = df.iloc[0]

    # Area
    assert row["area_px"] == 100
    # Raw sums
    assert row["sum_intensity"] == 100.0 * 100
    assert row["bg_area_px"] == 100
    assert row["bg_sum"] == 10.0 * 100
    # Background mean
    assert abs(row["bg_mean"] - 10.0) < 1e-9
    # Corrected sum: (100 - 10) * 100
    assert abs(row["corrected_sum_intensity"] - (90.0 * 100)) < 1e-6
