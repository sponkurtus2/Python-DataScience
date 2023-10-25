import matplotlib.pyplot as plt
from matplotlib import style
# TIP FOR PYCHARM
# If you have problems with the graphics view, you can disable the sci View in settings,
# and do -> pip install PyQt5, to load the graphics on a new window

# pylot is used to make graphics, in this example below we have .plot()
# which creates a graphic with X values as the first parameter, and Y values as second parameter
'''
    plt.plot([1, 3, 5, 7], [5, 10, 25, 125])
    plt.show()
'''

style.use('bmh')
# We can also define the values manually


x = [2, 4, 6]
y = [4, 8, 24]

x2 = [3, 6, 9]
y2 = [10, 15, 36]


plt.plot(x, y)
plt.plot(x2, y2)

plt.title('Graphic using Matplotlib')
plt.xlabel('Values for X')
plt.ylabel('Values for Y')
plt.show()
