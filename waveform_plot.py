from operator import itemgetter

import matplotlib.pyplot as plt
import numpy as np
import root_numpy

plt.rc('font', family='serif')

wlength = 400
filename = 'Cf_centered_20inches_from6inchLeadShield_64rods_noteflon_amps_27V_500s_0.root'
# filename ='Cs_15cm_test_thr20_0.root'
wavearray = root_numpy.root2array(filename, treename='Waveforms')
wavearray_sorted = sorted(wavearray, key=itemgetter(0))
sample_waveform_id = 2
sample = np.linspace(1, wlength, num=wlength)

# plt.plot(sample, wavearray_sorted[sample_waveform_id][3], linestyle='-', marker='', color='red')
plt.plot(sample * 4, wavearray_sorted[sample_waveform_id][3], linestyle='-', marker='', color='red', label='waveform')
total_start = 100
delta = 28
tail_start = total_start + delta
delta2 = 220
integration_end = total_start + delta2
plt.axvline(x=total_start * 4, linestyle='--', marker='', color='blue', label=r'$Q_{\mathrm{total}}$ integration start')
plt.axvline(x=tail_start * 4, linestyle='--', marker='', color='orange', label=r'$Q_{\mathrm{tail}}$ integration start')
plt.axvline(x=integration_end * 4, linestyle='--', marker='', color='green', label=r'$Q_{\mathrm{total}}$ and $Q_{\mathrm{tail}}$ integration end')

plt.legend(loc='upper right', numpoints=1)
# plt.title(filename,fontsize=5)

ax = plt.gca()
ax.set_xlabel(r'sample number')
ax.set_xlabel(r'Time (ns)')
# ax.set_xlim(xmin=0,xmax=wlength)
ax.set_xlim(xmin=0, xmax=wlength * 4)
ax.set_ylabel('Voltage (ADC)', rotation=90)
ax.grid(True)
plt.savefig("sample_waveform.pdf")
