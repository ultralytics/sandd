import matplotlib.pyplot as plt
import numpy as np

path = '/Users/glennjocher/Downloads/SANDD/'
file = 'Cf_centered_20inches_from6inchLeadShield_64rods_noteflon_amps_27V_500s_0.glenn'


# timestamp, digitizer_ID, digitizer_channel, SiPM_ID, SiPM_channnel, number_of_samples, V1 V2 V3 .... V400

def main():
    # Read data
    with open(path + file, 'r') as f:  # Method 3 (5.5s)
        lines = f.read().split()
    x = np.array(lines[:406 * 100], dtype=np.float32).reshape((-1, 406))

    # Plot waveforms
    i = range(0, 30)  # rows to plot
    fig = plt.figure()
    plt.plot(x[i, 6:].T)
    plt.autoscale(axis='both', tight=True)

    fig.tight_layout()
    fig.savefig('results.png', dpi=300)


if __name__ == '__main__':
    main()
