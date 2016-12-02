import numpy as np
import matplotlib.pyplot as plt
import pylab as pylab

import numpy as np
import matplotlib.pyplot as plt

device_perf =[3600,3600,3400,3100,2800,2500,2200,1900,1700,1500,1300,1100,992,880,786,700]

perf_gain = [1.881648352,	1.872928177,	1.777777778,	1.758823529,	1.6875,	1.6,	1.510791367,	1.467741935,	1.441441441,	1.447028424,	1.4,	1.375687844,	1.35,	1.331694577,	1.27707059,	1.269913935]
#perf_gain = [1.88,1.80,1.17,1.28,	1.15,	1.02,	1.04,	1.03,	1.04]
#perf_gain = [1.88,1.80,1.28,	1.15,	1.02,	1.04,	1.03,	1.04]

#plt.title('Area of a Circle')
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
plt.xlabel('Device Bandwidth [MB/s]' ,fontsize=25)
plt.ylabel('Speedup',fontsize=25)
ax.yaxis.grid(True, linestyle='-', which='major', color='black')
ax.set_ylim([1,2])

ax.plot(device_perf, perf_gain,'rs',linestyle='--')
plt.xlim(device_perf[-1],device_perf[0])

plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.tight_layout()
plt.show()
pylab.savefig('motivation.pdf',bbox_inches='tight')
#plt.rcParams['lines.linewidth'] = 2
#plt.rcParams['axes.labelsize'] = medium
#savefig("motivation.pdf")








