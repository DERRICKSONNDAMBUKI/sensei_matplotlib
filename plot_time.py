# plotting high temperatures
# Plotting high temperatures
# The following code creates a list of dates and a corresponding list
# of high temperatures. It then plots the high temperatures, with the
# date labels displayed in a specific format.
from datetime import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import dates as mdates

dates = [
    dt(2016, 6, 21),dt(2016,6,22),
    dt(2016, 6, 23),dt(2016, 6, 24)
]
highs = [
    57, 68, 64, 59
]
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.title('Daily High Temps', fontsize=24)
plt.ylabel('Temp (F)', fontsize=16)
x_axis = plt.axes().get_xaxis()
x_axis.set_major_formatter(
    mdates.DateFormatter('%B %d %Y')
)
fig.autofmt_xdate()
plt.show()
