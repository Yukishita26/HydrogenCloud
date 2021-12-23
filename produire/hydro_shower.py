import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

target_names = sys.argv[1:-1]
skip_step = int(sys.argv[-1])

plots = []
for target_name in target_names:
	with open(target_name) as f:
	   txt = f.read()

	lines = txt.split("\n")
	plots += [np.array([list(map(float, line.split(','))) for line in lines[:-1]])]

plots = np.asarray(plots)

_range = 5
fig = plt.figure(figsize=(6,6))
ax = Axes3D(fig)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

for i,_ in enumerate(target_names):
	ax.plot(
		plots[i, ::skip_step, 0],
		plots[i, ::skip_step, 1],
		plots[i, ::skip_step, 2],
	    marker=".", markersize=0.5, linestyle='None', color=['k','r','b'][i%3], alpha=0.5)

ax.set_xlim(-_range, _range)
ax.set_ylim(-_range, _range)
ax.set_zlim(-_range*0.75, _range*0.75)

plt.show()

#plt.figure(figsize=(6,6))
#plt.scatter(plots[::skip_step, 0], plots[::skip_step, 2], s=1)
#plt.show()