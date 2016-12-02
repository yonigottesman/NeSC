import numpy as np
import matplotlib.pyplot as plt

block_size =["0.5","1","2","4","8","16","32","64"]



#plt.title('Area of a Circle')
plt.figure(figsize=(10,5))

#read
raw_read = [7.08459,7.1112,9.95308,10.296,14.4322,24.364,41.8219,85.1153]
direct_assin_read = [8.01839,8.08628,8.6697,12.1472,17.1955,27.4618,47.6317,94.8892]
virtio_read = [50.6018,50.6251,53.1763,53.3233,58.575,69.2209,89.3687,138.032]
plt.subplot(211)
plt.xlabel('Block size [KB]')
plt.ylabel('Read Latency[usec]')
plt.plot(block_size, raw_read ,linestyle='-',label='Raw',marker='x',color='b')
plt.plot(block_size, virtio_read, marker='o', linestyle='--', color='r', label='virtio')
plt.plot(block_size, direct_assin_read, marker='s', linestyle=':', color='g', label='Direct')
plt.legend(loc=4)

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
plt.subplot(212)
plt.xlabel('Block size [KB]')
plt.ylabel('Write Latency [usec]')
plt.plot(block_size, raw_write ,linestyle='-',label='Raw',marker='x',color='b')
plt.plot(block_size, virtio_write, marker='o', linestyle='--', color='r', label='virtio')
plt.plot(block_size, direct_assin_write, marker='s', linestyle=':', color='g', label='Direct')
plt.legend(loc=4)


plt.show()
