import pandas as pd

# Load FIJI and blottool results
fiji = pd.read_csv("example/fiji_results.csv")
bt = pd.read_csv("example/blottool_results.csv")

# Sort both by label to align rows
fiji = fiji.sort_values("label").reset_index(drop=True)
bt = bt.sort_values("label").reset_index(drop=True)

# Keep only the band rows from blottool (ignore any non-lane labels if present)
bt = bt[bt["label"].str.startswith("lane")].reset_index(drop=True)

# Sanity check: same number of rows
if len(fiji) != len(bt):
    raise ValueError(f"Row count mismatch: FIJI={len(fiji)} vs blottool={len(bt)}")

# Compare mean and integrated density
mean_diff = bt["mean_intensity"] - fiji["mean_intensity"]
sum_diff = bt["sum_intensity"] - fiji["sum_intensity"]

comparison = pd.DataFrame({
    "label": bt["label"],
    "bt_mean": bt["mean_intensity"],
    "fiji_mean": fiji["mean_intensity"],
    "diff_mean": mean_diff,
    "bt_sum": bt["sum_intensity"],
    "fiji_sum": fiji["sum_intensity"],
    "diff_sum": sum_diff,
})

print("=== FIJI vs blottool (band ROIs) ===\n")
print(comparison)

print("\nMax abs diff (mean gray):", mean_diff.abs().max())
print("Max abs diff (IntDen):   ", sum_diff.abs().max())

if mean_diff.abs().max() < 1e-3:
    print("\nValidation PASSED: blottool reproduces FIJI to <0.001 gray units.")
else:
    print("\nValidation WARNING: mean differences exceed 0.001 gray units.")
