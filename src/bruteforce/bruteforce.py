import numpy as np
import matplotlib.pyplot as plt

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
    for i in range(order + 1):
        result += generatePascalCoef(order, i) * (1-t)**(order-i) * t**i * Points[i]
    return result

## Generate the Bézier curve using the given control points and number of samples
def generateBezierCurve(Points, num_samples):
    order = len(Points) - 1
    t_values = np.linspace(0, 1, num_samples)
    curve_points = np.array([generateNewPoint(Points, t, order) for t in t_values])
    return curve_points

## Plot the Bézier curve with the given control points
def plotBezierCurve(Points, num_samples):
    curve_points = generateBezierCurve(Points, num_samples)
    plt.plot(curve_points[:, 0], curve_points[:, 1], label='Bézier Curve')
    plt.scatter(Points[:, 0], Points[:, 1], color='red', label='Control Points')
    
    # Plot lines between control points
    for i in range(len(Points) - 1):
        plt.plot([Points[i][0], Points[i+1][0]], [Points[i][1], Points[i+1][1]], color='gray', linestyle='--')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bézier Curve with Control Points')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

