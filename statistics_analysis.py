from matplotlib import pyplot as plt
import numpy as np
from sys import argv
from sys import exit as sysexit


if len(argv) == 1:
    print("Usage: python statistics_analysis.py <source path>")
    sysexit()
else:
    source_dir = argv[1]

dataset = np.genfromtxt(source_dir, delimiter=",", skip_header=1, usecols=(1,2))
reflections = dataset[:,0]
edges = dataset[:,1]

print("Dataset: " + str(dataset))

fig = plt.figure(figsize =(10, 7))
plt.hist(edges, bins = 70)
plt.title("Edge histogram")
plt.show()

fig = plt.figure(figsize =(10, 7))
plt.hist(reflections, bins = 50, range=(0,1), log=True)
plt.title("Reflection histogram")
plt.show()

#The statistics still need some work, but this is a start