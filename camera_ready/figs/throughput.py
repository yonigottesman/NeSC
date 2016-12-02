import numpy as np
import matplotlib.pyplot as plt

n_groups = 4

bare_metal = (805,800,970,938)
virtio = (745,716,800,740)
direct = (782,780,937,897)
emulation = (549,555,616,580)


fig, ax = plt.subplots()
index = np.arange(0,n_groups*2,2)
error_config = {'ecolor': '0.3'}
opacity = 0.4
bar_width = 0.35



rects1 = plt.bar(index, bare_metal, bar_width,
                 alpha=opacity,
                 color='b',
#                 yerr=std_men,
                 error_kw=error_config,
                 label='Host')

rects3 = plt.bar(index + bar_width, direct, bar_width,
                 alpha=opacity,
                 color='y',
 #                yerr=std_women,
                 error_kw=error_config,
                 label='NeSC')

rects2 = plt.bar(index + bar_width*2, virtio, bar_width,
                 alpha=opacity,
                 color='r',
 #                yerr=std_women,
                 error_kw=error_config,
                 label='virtio')




rects4 = plt.bar(index + bar_width*3, emulation, bar_width,
                 alpha=opacity,
                 color='g',
 #                yerr=std_women,
                 error_kw=error_config,
                 label='Emulation')



#plt.xlabel('Group')
plt.ylabel('MB/s')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width, ('Read Raw', 'Read FS', 'Write Raw', 'Write FS' ))
plt.legend(loc =4)

plt.tight_layout()
plt.show()
