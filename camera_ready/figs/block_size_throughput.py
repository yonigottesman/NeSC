import numpy as np
import matplotlib.pyplot as plt
import pylab as pylab
block_size =["0.5","1","2","4","8","16","32","64","128","256","512","1024","2048","4096"]



#plt.title('Area of a Circle')
fig = plt.figure(figsize=(10,10))

#read
raw_read = [68.2,
            136,
            195,
            380,
            518,
            659,
            773,
            770,
            788,
            799,
            806,
            804,
            797,
            796]
direct_assin_read = [58.9,
                     129,
                     242,
                     347,
                     475,
                     593,
                     691,
                     694,
                     703,
                     719,
                     724,
                     725,
                     725,
                     723]
virtio_read = [9.8,
               19.8,
               38.2,
               75.8,
               140,
               234,
               365,
               474,
               573,
               638,
               685,
               700,
               727,
               740]

ide_read = [2.4,
            6,
            11.7,
            23.4,
            45.6,
            84.3,
            151,
            247,
            375,
            486,
            587,
            592,
            596,
            599,

]

marksize=10
my_linewidth = 3


ax2 =plt.subplot(211)
ax2.set_xscale('log')
ax2.set_xticks([float(x) for x in block_size])
ax2.set_xticklabels(block_size,fontsize=20)
ax2.set_ylim([0,850])
ax2.yaxis.grid(True, linestyle='-', which='major', color='black')
ax2.set_yticks(np.arange(0,1200,200))

#plt.xlabel('Block size [KB]')
plt.ylabel('Read [MB/s]',fontsize=20)
plt.plot(block_size, raw_read ,linestyle='-',label='Host',marker='x',color='b',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, virtio_read, marker='o', linestyle='--', color='r', label='virtio',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, direct_assin_read, marker='s', linestyle=':', color='g', label='NeSC',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, ide_read, marker='D', linestyle='-.', color='m', label='Emulation',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
#plt.tight_layout()
plt.yticks(fontsize=20)
plt.xticks(fontsize=15)



#plt.legend(loc=4)

#write
raw_write = [79,141,296,515,712,935,1000,1000,1000,1000,989,971,963,963]
direct_assin_write = [55.6,114,226,418,569,881,1000,1000,1000,984,956,954,949,946]
virtio_write = [7.6,17.7,35.3,69.7,130,173,306,366,468,591,619,661,726,766]
ide_write = [
    2.78,
    5.64,
    11.1,
    21.64,
    42.98,
    80.42,
    156.6,
    263.2,
    412.8,
    539,
    644.4,
    639.6,
    638,
    659.6,

]

ax = plt.subplot(212)

plt.plot(block_size, raw_write ,linestyle='-',label='Host',marker='x',color='b',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, direct_assin_write, marker='s', linestyle=':', color='g', label='NeSC',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, virtio_write, marker='o', linestyle='--', color='r', label='virtio',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.plot(block_size, ide_write, marker='D', linestyle='-.', color='m', label='Emulation',linewidth=my_linewidth,markersize=marksize,markeredgewidth=1)
plt.legend(loc=4)


ax.set_xscale('log')
ax.set_xticks([float(x) for x in block_size])
ax.set_xticklabels(block_size,fontsize=15)
ax.set_xlim(float(block_size[0]),float(block_size[-1]))
ax.set_ylim([0,1050])
ax.yaxis.grid(True, linestyle='-', which='major', color='black')
ax.set_yticks(np.arange(0,1200,200))

plt.yticks(fontsize=20)
plt.xticks(fontsize=15)

plt.xlabel('Block size [KB]',fontsize=20)
plt.ylabel('Write [MB/s]',fontsize=20)
plt.tight_layout()


pylab.savefig('throughput_block_size.pdf',bbox_inches='tight')
plt.show()
