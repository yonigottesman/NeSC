import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pylab as pylab


block_size =["0.5","1","2","4","8","16","32","64"]
#plt.title('Area of a Circle')
fig = plt.figure(figsize=(10,5))
marksize=10
my_linewidth = 3


#write
direc_write_journal = [
    44.7097,
    45.1575,
    48.2966,
    54.8129,
    59.9098,
    65.1749,
    80.8348,
    114.786
]

# direc_write_no_journal = [
#     10.7617,
#     12.6169,
#     15.873,
#     29.8904,
#     26.6887,
#     33.4202,
#     45.9174,
#     83.7847,
#     ]
direc_write_no_fs = [8.94831,
                          8.87642,
                          8.97366,
                          9.76668,
                          14.3608,
                          18.7582,
                          32.4188,
                          64.6678,
    ]



virtio_write_journal = [
    227.929,
    228.694,
    226.638,
    227.091,
    232.783,
    238.375,
    250.058,
    290.26,
]
# virtio_write_no_journal= [
#     65.2433,
#     75.0593,
#     90.7658,
#     122.657,
#     128.906,
#     136.583,
#     151.962,
#     219.139,
# ]


virtio_write_no_fs = [
    57.7683,
    57.7572,
    57.8303,
    59.0849,
    63.296,
    71.2803,
    85.5786,
    124.044,

    
]

ax = fig.add_subplot(111)
ax.set_xscale('log')
ax.set_xticks([float(x) for x in block_size])
ax.set_xticklabels(block_size,fontsize=20)
ax.yaxis.grid(True, linestyle='-', which='major', color='black')
plt.xlabel('Block size [KB]',fontsize=20)
plt.ylabel('Write Latency [usec]',fontsize=20)
plt.plot(block_size, virtio_write_journal, marker='s', linestyle=':', color='g', label='Virtio - FS',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, virtio_write_no_fs, marker='x', linestyle='-.', color='m', label='Virtio - raw',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, direc_write_journal ,linestyle='-',label='NeSC - FS',marker='D',color='b',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1 )
plt.plot(block_size, direc_write_no_fs, marker='o', linestyle='--', color='r', label='NeSC - raw',markersize=marksize,linewidth=my_linewidth,markeredgewidth=1)

plt.yticks(fontsize=20)
plt.xticks(fontsize=20)

#plt.legend(loc=4)
plt.tight_layout()
ax.legend( bbox_to_anchor=(0.22, 0.6),
          ncol=1, fancybox=True, shadow=False)







pylab.savefig('fs_affect.pdf',bbox_inches='tight')
plt.show()

