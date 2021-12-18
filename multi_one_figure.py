# Multiple plots in one figure
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
import matplotlib.pyplot as plt

x_vals = list(range(11))
squares = [x**2 for x in x_vals]
cubes = [x**3 for x in x_vals]

fig,axarr=plt.subplots(2,1,sharex=True)

# Sharing a y-axis
# To share a y-axis, we use the sharey=True argument.
# fig,axarr=plt.subplots(1,2,sharey=True)

axarr[0].scatter(x_vals,squares)
axarr[0].set_title('Squares')

axarr[1].scatter(x_vals, cubes, c='red')
axarr[1].set_title('Cubes')
plt.show()
