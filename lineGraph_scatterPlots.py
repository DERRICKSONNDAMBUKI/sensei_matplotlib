# Making a scatter plot Emphasizing points
# The scatter() function takes a list of x values and a list of y values,
# and a variety of optional arguments. The s=10 argument controls
# the size of each point.
import matplotlib.pyplot as plt

x_values= list(range(1000))
squares=[x**2 for x in x_values]
# A colormap varies the point colors from one shade to another,
# based on a certain value for each point. The value used to
# determine the color of each point is passed to the c argument, and
# the cmap argument specifies which colormap to use.
# The edgecolor='none' argument removes the black outline
# from each point.

plt.scatter(x_values, squares,c=squares,cmap=plt.cm.Blues,edgecolor='none',s=10)

# Csutomizing plots
# Plots can be customized in a wide variety of ways. Just
# about any element of a plot can be customized.
# Adding titles and labels and scaling axes

# Empasizing points
# You can plot as much data as you want on one plot. Here we re-
# plot the first and last points larger to emphasize them.
plt.scatter(x_values[0], squares[0],c='green',edgecolors='none',s=100)
plt.scatter(x_values[-1], squares[-1],c='red',edgecolors='none',s=100)

plt.title('Square numbers',fontsize=24)
plt.xlabel('Values',fontsize=18)
plt.ylabel('Square of Value',fontsize=18)
plt.tick_params(axis='both',which ='major',labelsize=14)

# Removing axes
# You can customize or remove axes entirely. Here’s how to access
# each axis, and hide it.
# plt.axes().get_xaxis().set_visible(False) # To remove x-axis
# plt.axes().get_yaxis().set_visible(False) # To remove y-axis

plt.axis([0,1100,0,1100000])

# Setting a custom figure size
# You can make your plot as big or small as you want. Before
# plotting your data, add the following code. The dpi argument is
# optional; if you don’t know your system’s resolution you can omit
# the argument and adjust the figsize argument accordingly.
# plt.figure(dpi=128,figsize=(10,6))

# Saving a plot
# The matplotlib viewer has an interactive save button, but you can
# also save your visualizations programmatically. To do so, replace
# plt.show() with plt.savefig(). The bbox_inches='tight'
# argument trims extra whitespace from the plot.
plt.savefig('squares.png',bbox_inches='tight')

plt.show()
