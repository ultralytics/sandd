import os
from sys import platform

import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(linewidth=320, formatter={'float_kind': '{:11.5g}'.format})  # format short g, %precision=5

path = '/Users/glennjocher/Downloads/SANDD/'


# 1. time each waveform, and then integrate based on a new t0 which is the timed sample.
# 2. make sure waveforms appear on both sides of a rod
# 3. try and make a flat fielding map from all the data
# 4. Slava will make a new format with rod_ID

def main():
    # file = 'background_64rods_noteflon_amps_27V_12hr_0.glenn'  # background
    file = 'Cs_collimated_oneSource_center_64rods_noteflon_amps_27V_500s_0.glenn'  # Cs (gammas)
    # file = 'Cf_centered_20inches_from6inchLeadShield_64rods_noteflon_amps_27V_500s_0.glenn'  # Cf (gammas + neutrons)

    # Read data
    # timestamp, digitizer_ID, digitizer_channel, SiPM_ID, SiPM_channnel, number_of_samples, V1 V2 V3 .... V400
    with open(path + file, 'r') as f:  # Method 3 (5.5s)
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

    # Candidate cuts
    j = (ymax.ravel() < 9000) & (ymax.ravel() > 100)  # & (yn.min(1) > -0.5) & (yn[:, :50].std(1) < 0.1)
    print('%g/%g (%.1f%%) pass candidate cuts' % (j.sum(), len(y), j.mean() * 100))

    # Charges
    s = 100  # start sample
    q_total = y[j, s + 0: s + 220].sum(1)
    q_tail = y[j, s + 28: s + 220].sum(1)

    # Plot matplotlib
    log = False
    fig = plt.figure(figsize=(16, 8))
    plt.subplot(3, 1, 1)
    waveform = y[j][:1].T
    waveform = np.ediff1d(waveform)
    plt.plot(waveform)
    plt.autoscale(axis='both', tight=True)

    plt.subplot(3, 2, 3)
    plt.hist(q_total, 100, log=log)
    plt.title('Q total')

    plt.subplot(3, 2, 4)
    plt.hist(q_tail, 100, log=log)
    plt.title('Q tail')

    plt.subplot(3, 2, 5)
    plt.hist(q_tail / q_total, np.linspace(0.3, .9, 100), log=log)
    plt.title('Q tail / Q total')

    plt.subplot(3, 2, 6)
    plt.hist(y[j].sum(1), np.linspace(0, 250000, 100), log=log)
    plt.title('Q full waveform')

    fig.tight_layout()
    fig.savefig('results.png', dpi=300)
    if platform == 'darwin':  # macos
        os.system('open results.png')

    # Plot.ly
    # trace = go.Scatter(y=y.T)
    # data = [trace]

    # plot([go.Scatter(y=y)], filename='basic-line')

    # data = [go.Scatter(y=yi,mode = 'lines') for yi in y]
    # plot(data)

    # plot([go.Histogram(x=porch.std(1), nbinsx=30)])


def waveform_times(waveform):
    # returns the max derivative sample
    x = np.ediff1d(waveform).argmax()
    return None


def matched_sipms(array_id, ):
    # 64 to 57
    #


if __name__ == '__main__':
    main()
