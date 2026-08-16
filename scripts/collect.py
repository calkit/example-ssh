"""Stand in for whatever actually produces this project's raw data.

This is the stage that runs somewhere else. Its environment in
``calkit.yaml`` is ``remote-machine:py``, which means Calkit sends the
project to a workspace on the remote host, activates the ``py`` environment
there, and runs this script on that machine rather than on yours.

Deliberately seeded, so re-running produces byte-identical output and the
pipeline can show you a cached stage rather than fresh noise every time.
"""

import csv
import os
import platform

import numpy as np

N_POINTS = 200

rng = np.random.default_rng(seed=0)
t = np.linspace(0, 4 * np.pi, N_POINTS)
signal = np.sin(t) + rng.normal(scale=0.1, size=N_POINTS)

os.makedirs("data", exist_ok=True)
with open("data/raw.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["t", "signal"])
    writer.writerows(zip(t, signal))

print(f"Collected {N_POINTS} points on {platform.node()}")
