"""Stand in for whatever actually turns this project's data into a figure.

This stage runs locally, in the ``py`` environment, on the data the
``raw-data`` stage collected remotely. That split is the point of the
example: the work that needs the other machine happens there, and
everything downstream of it carries on here as normal.
"""

import csv
import os

import matplotlib

# No display on a machine running a pipeline, and none needed to write a file
matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

t = []
signal = []
with open("data/raw.csv") as f:
    for row in csv.DictReader(f):
        t.append(float(row["t"]))
        signal.append(float(row["signal"]))

os.makedirs("figures", exist_ok=True)
fig, ax = plt.subplots(figsize=(6, 3), layout="constrained")
ax.plot(t, signal, linewidth=1)
ax.set_xlabel("t")
ax.set_ylabel("Signal")
ax.set_title(f"Collected remotely: {len(t)} points")
fig.savefig("figures/plot.png", dpi=150)

print(f"Plotted {len(t)} points to figures/plot.png")
