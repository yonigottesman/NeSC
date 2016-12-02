import numpy as np
import matplotlib.pyplot as plt
import pylab as pylab
block_size =["0.5","1","2","4","8","16","32","64"]


marksize=10
my_linewidth = 3



#plt.title('Area of a Circle')
plt.figure(figsize=(10,10))

#read
raw_read = [7.08459,7.1112,9.95308,10.296,14.4322,24.364,41.8219,85.1153]
direct_assin_read = [8.01839,8.08628,8.6697,12.1472,17.1955,27.4618,47.6317,94.8892]
virtio_read = [50.6018,50.6251,53.1763,53.3233,58.575,69.2209,89.3687,138.032]
ide_read = [
    173.357,
    172.902,
    175.889,
    175.753,
    181.669,
    191.799,
    212.605,
    262.167,
]
ax2 = plt.subplot(211)
#plt.xlabel('Block size [KB]')
plt.ylabel('Read [usec]',fontsize=20)
plt.plot(block_size, raw_read ,linestyle='-',label='Host',marker='x',color='b',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, virtio_read, marker='o', linestyle='--', color='r', label='virtio',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, direct_assin_read, marker='s', linestyle=':', color='g', label='NeSC',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, ide_read, marker='D', linestyle='-.', color='m', label='Emulation',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
#plt.legend(loc=4)
ax2.set_xscale('log')
ax2.set_xticks([float(x) for x in block_size])
ax2.set_xticklabels(block_size,fontsize=15)
ax2.set_ylim([0,300])
ax2.yaxis.grid(True, linestyle='-', which='major', color='black')
ax2.set_yticks(np.arange(0,300,50))
ax2.set_xlim(float(block_size[0]),float(block_size[-1]))
#write
raw_write = [6.53739,7.38523,6.98499,7.78802,11.5504,17.5058,32.1346,64.2666]
direct_assin_write = [8.94831,8.87642,8.97366,9.76668,14.3608,18.7582,32.4188,64.6678]
virtio_write = [57.7683,
               57.7572,
               57.8303,
               59.0849,
               63.296,
               71.2803,
               85.5786,
               124.044]

ide_write = [
    223.612,
    224.064,
    223.721,
    250.272,
    256.135,
    261.128,
    270.602,
    319.865,
]
plt.yticks(fontsize=20)
plt.xticks(fontsize=15)

ax = plt.subplot(212)
plt.xlabel('Block size [KB]',fontsize=20)
plt.ylabel('Write [usec]',fontsize=20)
plt.plot(block_size, ide_write, marker='D', linestyle='-.', color='m', label='Emulation',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, virtio_write, marker='o', linestyle='--', color='r', label='virtio',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, direct_assin_write, marker='s', linestyle=':', color='g', label='NeSC',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, raw_write ,linestyle='-',label='Host',marker='x',color='b',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)



#plt.legend(loc=4)
ax.set_xscale('log')
ax.set_xticks([float(x) for x in block_size])
ax.set_xticklabels(block_size,fontsize=15)
ax.set_ylim([0,350])
ax.yaxis.grid(True, linestyle='-', which='major', color='black')
ax.set_yticks(np.arange(0,350,50))
ax.set_xlim(float(block_size[0]),float(block_size[-1]))

plt.yticks(fontsize=20)
plt.xticks(fontsize=15)
ax.legend( bbox_to_anchor=(0.22, 0.5),
          ncol=1, fancybox=True, shadow=False)
plt.tight_layout()
pylab.savefig('latency_block_size.pdf',bbox_inches='tight')
plt.show()
