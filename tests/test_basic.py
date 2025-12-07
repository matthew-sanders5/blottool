import numpy as np
from blottool.models import ROI
from blottool.measure import measure_bands

def test_simple_uniform_roi():
    # 10x10 image, all pixels = 100
    img = np.full((10, 10), 100.0)
    roi = ROI(label="test", x=0, y=0, width=10, height=10)
    df = measure_bands(img, [roi])

    row = df.iloc[0]
    assert row["area_px"] == 100
    assert row["sum_intensity"] == 100.0 * 100
    assert abs(row["mean_intensity"] - 100.0) < 1e-9
