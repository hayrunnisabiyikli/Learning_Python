import matplotlib.pyplot as plt

# Define x and y axis values for line 1
x1 = [1, 4, 5, 6, 7]
y1 = [2, 6, 3, 6, 3]

# Define x and y axis values for line 2
x2 = [1, 2, 3, 4, 5]
y2 = [5, 3, 2, 7, 8]

# Plot the lines with line markers
plt.plot(x1, y1, 'o-', label='Line 1')  # 'o-' specifies circle markers connected by lines
plt.plot(x2, y2, 'x--', label='Line 2')  # 'x--' specifies cross markers connected by dashed lines

# Set plot title and axis labels
plt.title('Line Plot with Markers')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()
