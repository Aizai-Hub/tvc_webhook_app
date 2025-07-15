import itertools
import json
import os

# Make sure the output folder exists
os.makedirs("rsi_tunes", exist_ok=True)

# Define the RSI parameter options (Param A, Param B)
rsi_params = [(6,1), (9,1), (14,1), (21,2), (23,2)]

# Generate all 5-feature combinations from the list
combinations = list(itertools.combinations(rsi_params, 5))

# Save each combination into its own JSON file
for idx, combo in enumerate(combinations, start=1):
    features = [{"type": "RSI", "a": a, "b": b} for (a, b) in combo]
    
    config = {
        "tune_id": idx,
        "features": features,
        "note": f"RSI combo {idx}"
    }

    filename = f"rsi_tunes/tune_{idx}.json"
    with open(filename, "w") as f:
        json.dump(config, f, indent=2)

    print(f"✅ Saved: {filename}")
