import matplotlib.pyplot as plt

x = [5, 10, 15, 20, 25, 30]
y = [96, 83, 78, 60, 52, 30]

plt.style.use('ggplot')

fig, ax = plt.subplots()

ax.scatter(x, y)

fig.savefig('scatter_plot.jpg')