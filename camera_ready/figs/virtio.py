import numpy as np
import matplotlib.pyplot as plt

#plot for virtio direct assignment and bare metal
#men = baremetal woman = virtio

N=2

metal = (960, 807)
sriov = (945, 780)
virtio = (680,670)

ind = np.arange(N)  # the x locations for the groups

margin = 0.05
#width = (1.-2.*margin)/N
width = 0.2      # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind, metal, width, color='r')
rects2 = ax.bar(ind + width, sriov, width, color='y')
rects3 = ax.bar(ind + width + width, virtio, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('MB/s')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Write', 'Read'))

ax.legend((rects1[0], rects2[0],rects3[0]), ('Bare Metal', 'SR-IOV', 'virtio'))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()
