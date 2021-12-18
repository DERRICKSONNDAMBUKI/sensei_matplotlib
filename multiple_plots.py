# You can make as many plots as you want on one figure.
# When you make multiple plots, you can emphasize
# relationships in the data. For example you can fill the space
# between two sets of data.
# Plotting two sets of data
# Here we use plt.scatter() twice to plot square numbers and
# cubes on the same figure.

import matplotlib.pyplot as plt
x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

plt.scatter(x_values,squares, c='blue',edgecolor='none', s=20)
plt.scatter(x_values,cubes,c='red',edgecolor='none',s=20)
# Filling the space between data sets
# The fill_between() method fills the space between two data
# sets. It takes a series of x-values and two series of y-values. It also
# takes a facecolor to use for the fill, and an optional alpha
# argument that controls the color’s transparency.
plt.fill_between(x_values,cubes,squares,facecolor='blue',alpha=0.25)
plt.axis([0,11,0,1100])
plt.show()
# $python3 multiple_plots.py

# You can include as many individual graphs in one figure as
# you want. This is useful, for example, when comparing
# related datasets.
# Sharing an x-axis
# The following code plots a set of squares and a set of cubes on
# two separate graphs that share a common x-axis.
# The plt.subplots() function returns a figure object and a tuple
# of axes. Each set of axes corresponds to a separate plot in the
# figure. The first two arguments control the number of rows and
# columns generated in the figure.

