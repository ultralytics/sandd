import os
from sys import platform

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(linewidth=320, formatter={"float_kind": "{:11.5g}".format})  # format short g, %precision=5
matplotlib.rc("font", **{"size": 8})

path = "/Users/glennjocher/Downloads/SANDD/"


# 1. time each waveform, and then integrate based on a new t0 which is the timed sample.
# 2. make sure waveforms appear on both sides of a rod
# 3. try and make a flat fielding map from all the data
# 4. Slava will make a new format with rod_ID


def main():
    """Process waveform data files to extract and analyze signals, apply cuts, and visualize results using
    matplotlib.
    """
    files = [
        "background_64rods_noteflon_amps_27V_12hr_0.glenn",  # background
        "Cs_collimated_oneSource_center_64rods_noteflon_amps_27V_500s_0.glenn",  # Cs137 (gammas)
        "Cf_centered_20inches_from6inchLeadShield_64rods_noteflon_amps_27V_500s_0.glenn",
    ]  # Cf (gammas + neutrons)

    # Read data
    # timestamp, digitizer_ID, digitizer_channel, SiPM_ID, SiPM_channnel, number_of_samples, V1 V2 V3 .... V400
    file = files[1]
    with open(path + file) as f:  # Method 3 (5.5s)
        lines = f.read().split()
    # x = np.array(lines[:406 * 3000], dtype=np.float32).reshape((-1, 406))
    x = np.array(lines, dtype=np.float32).reshape((-1, 406))

    # Get waveforms
    y = x[:, 6:]  # waveforms

    # Subtract pedestals
    pedestal = y[:, :60]
    y -= pedestal.mean(1, keepdims=True)

    # Normalize amplitudes
    ymax = y.max(1, keepdims=True)
    yn = y / ymax

    # Time
    t0 = waveform_times(y) - 5  # 5 samples before leading edge of each pulse

    # Charges
    q_total, q_tail = charges(y, t0)

    # Candidate cuts
    j = (ymax.ravel() < 9000) & (ymax.ravel() > 100) & (yn.min(1) > -0.5) & (yn[:, :50].std(1) < 0.1) & (q_tail > 0)
    print(f"{j.sum():g}/{len(y):g} ({j.mean() * 100:.1f}%) pass candidate cuts")
    y, q_total, q_tail = y[j], q_total[j], q_tail[j]

    # Plotting
    log = False
    fig = plt.figure(figsize=(7, 7))
    plt.subplot(2, 2, 1)
    plt.plot(y[:30].T)
    plt.autoscale(axis="both", tight=True)
    plt.suptitle(file)

    plt.subplot(2, 2, 2)
    n = 100
    r = q_tail / q_total
    i = (r > 0.5) & (r < 0.8) & (q_total < 200) & (q_total > 10)
    cmap = plt.cm.jet
    cmap.set_under("w", 1)
    plt.hist2d(q_total[i], r[i], bins=n, range=[[0, 200], [0.5, 0.8]], cmap=cmap, vmin=1)

    plt.subplot(2, 2, 3)
    plt.hist(r[i & (q_total > 20)], bins=n, log=log)
    plt.title("Q_tail / Q_total")

    plt.subplot(2, 2, 4)
    plt.hist(q_total[i], bins=n, range=[0, 200], log=log)
    plt.title("Q_total")

    fig.tight_layout()
    fig.savefig("results.png", dpi=300)
    if platform == "darwin":  # MacOS
        os.system("open results.png")

    # Plot.ly
    # trace = go.Scatter(y=y.T)
    # data = [trace]

    # plot([go.Scatter(y=y)], filename='basic-line')

    # data = [go.Scatter(y=yi,mode = 'lines') for yi in y]
    # plot(data)

    # plot([go.Histogram(x=porch.std(1), nbinsx=30)])


def waveform_times(waveform):
    """Returns the index of the sample with the maximum derivative for each waveform in the input array."""
    return np.diff(waveform, axis=1).argmax(1)


def charges(x, s=100):
    """Returns Q_total and Q_tail for each waveform in x, starting from sample s."""
    n = len(s)
    q_tail, q_total = np.zeros((2, n))
    for i in range(n):
        a = x[i, s[i] + 0 : s[i] + 220]
        q_tail[i] = a[28:].sum()
        q_total[i] = a.sum()

    # q_total = x[:, s + 0: s + 220].sum(1)
    # q_tail = x[:, s + 28: s + 220].sum(1)
    return q_total / 1000, q_tail / 1000


def matched_sipms(array_id):
    """Returns None for matched SiPMs, currently not implemented."""
    return None
    # 64 to 57
    #


if __name__ == "__main__":
    main()
