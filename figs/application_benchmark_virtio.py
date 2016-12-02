import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pylab as pylab


import numpy as np
import matplotlib.pyplot as plt

n_groups = 3

emulation_speedup = (1.2,6.8,12.7)
virtio_speed = (1.17,2.1,1.3)


fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
#fig, ax = plt.subplots()
#index = np.arange(0,n_groups*2,2)
index = np.arange(n_groups)
error_config = {'ecolor': '0.3'}
opacity = 1
bar_width = 0.2


ax.set_yticks(np.arange(1,2.4,0.2))
ax.set_yticklabels(np.arange(1,2.4,0.2),fontsize=15)
ax.set_ylim([1,2.2])


rects1 = plt.bar(index, virtio_speed, bar_width,
                 alpha=opacity,
                 color='y',
                 error_kw=error_config,
                 label='Speedup over Emulation',hatch="*")







#plt.xlabel('Group')
plt.ylabel('speedup',fontsize=20)
#plt.title('Scores by group and gender')
plt.xticks(index , ('OLTP','Postmark','SysBench'),fontsize = 20,rotation=300)
#plt.legend(loc =4)
#ax.legend(loc='upper left', bbox_to_anchor=(0.5, 1.0),
#          ncol=3, fancybox=True, shadow=False)

ax.yaxis.grid(True, linestyle='-', which='major', color='black')

plt.yticks(fontsize=20)
plt.xticks(fontsize=15)

plt.xticks(index , ('OLTP','Postmark','SysBench'),fontsize = 20,rotation=300)
plt.tight_layout()
pylab.savefig('application_benchmark_virtio.pdf',bbox_inches='tight')
plt.show()



