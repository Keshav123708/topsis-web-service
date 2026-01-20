def topsis_from_file(file_path, weights, impacts):
    import os
    import pandas as pd
    import numpy as np

    output_path = os.path.join("uploads", "result.csv")

    df = pd.read_csv(file_path)
    data = df.iloc[:, 1:]

    weights = [float(w) for w in weights.split(",")]
    impacts = impacts.split(",")

    if len(weights) != len(impacts):
        raise ValueError("Weights and impacts count mismatch")

    norm = np.sqrt((data ** 2).sum())
    normalized = data / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = score
    df["Rank"] = score.rank(ascending=False).astype(int)

    df.to_csv(output_path, index=False)

    return output_path
