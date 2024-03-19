import numpy as np
import matplotlib.pyplot as plt
from time import time
##For Factorial Purposes
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

## Get the Pascal Coeffiescient at a given power and position
## This is used like generatePascalCoef(3, 2) = 3
## Because the pascal tree for 3 is 1 3 3 1 and the 2nd index position is 3
def generatePascalCoef(power, position):
    if (position > power or position < 0):
        return 0
    return factorial(power) // (factorial(position) * factorial(power - position))
    
## Generate a new point on the curve using the given formula
def generateNewPoint(Points, t, order):
    result = np.array([0.0, 0.0])
    Coeffiescient
    for i in range(order + 1):
        result += generatePascalCoef(order, i) * (1-t)**(order-i) * t**i * Points[i]
    return result

## Generate the Bézier curve using the given control points and number of iteration
def generateBezierCurve(Points, num_iteration):
    order = len(Points) - 1
    t_values = np.linspace(0, 1, num_iteration)
    curve_points = np.array([generateNewPoint(Points, t, order) for t in t_values])
    return curve_points

## Plot the Bézier curve with the given control points and number of iteration
def plotBezierCurveBruteForce(Points, num_iteration):
    start = time()
    curve_points = generateBezierCurve(Points, num_iteration)
    end = time()
    execution_time = (end - start) * 1000  # Convert to milliseconds
    plt.plot(curve_points[:, 0], curve_points[:, 1], label='Bézier Curve')
    plt.scatter(Points[:, 0], Points[:, 1], color='red', label='Control Points')
    
    # Plot lines between control points
    for i in range(len(Points) - 1):
        plt.plot([Points[i][0], Points[i+1][0]], [Points[i][1], Points[i+1][1]], color='gray', linestyle='--')
    
    # Set x and y limits
    min_x = min(curve_points[:, 0].min(), Points[:, 0].min())
    max_x = max(curve_points[:, 0].max(), Points[:, 0].max())
    min_y = min(curve_points[:, 1].min(), Points[:, 1].min())
    max_y = max(curve_points[:, 1].max(), Points[:, 1].max())
    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    plt.xlabel('X')
    plt.ylabel('Y')
    num_points = len(Points)

    plt.title('Bézier Curve with ' + str(num_points) + ' Control Points and ' + str(int(np.log2(num_iteration-1))) + ' iteration' + '\n' + 'Execution Time: ' + str(execution_time) + ' ms')
    
    plt.legend()
    plt.grid(True)
    
    # Annotate plot with execution time
    plt.show()
    plt.close()


