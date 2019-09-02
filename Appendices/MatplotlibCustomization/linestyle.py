x = np.linspace(0, 5, 10)
y = np.ones(10)
ls = np.array(['-.', ':', 'o', 's', '*', 'H', 'x', 'D'])

for i in xrange(8):
	plt.plot(x, i*y, colors[i]+ls[i])
	
plt.axis([-1, 6, -1, 8])
plt.show()