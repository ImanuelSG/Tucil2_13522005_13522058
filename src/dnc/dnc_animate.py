from .generalized_dnc import *
from matplotlib import pyplot as plt
from time import time

# Function to destructure the array
def destructure_array(points: list[list[Point]], n: int) -> list[list[list[Point]]]:
    array = []
    for i in range(len(points)):
        sub_array = []
        idx = 0
        for j in range(n-1):
            sub_sub_array = []
            for _ in range(n-j-1):
                sub_sub_array.append(points[i][idx])
                idx += 1
            sub_array.append(sub_sub_array)
        array.append(sub_array)
    return array

def coordinates_to_points(coordinates: list[tuple]) -> list[Point]:
    return [Point(x, y) for x, y in coordinates]


def plotBezierCurveDnC(Points: list[tuple], iterations: int, interval: int) -> None:
    # Convert coordinates into Point objects
    control_points = coordinates_to_points(Points)
    result_points = []
    mid_points = []
    n = len(control_points)

    start = time()
    create_bezier_points(control_points, result_points, mid_points, iterations, n)
    end = time()
    

    execution_time = (end - start) * 1000  # Convert to milliseconds

    result_points = destructure_array(result_points, n)    

    plt.figure()
    plt.xlim(min(control_points, key=lambda x: x.x).x - 1, max(control_points, key=lambda x: x.x).x + 1)
    plt.ylim(min(control_points, key=lambda x: x.y).y - 1, max(control_points, key=lambda x: x.y).y + 1)
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.title('Bézier Curve with ' + str(n) + ' Control Points and ' + str(iterations) + ' iteration' + '\n' + 'Execution Time: ' + str(execution_time) + ' ms')

    # Plot the control points
    for point in control_points:
        plt.plot(point.x, point.y, 'go', label='Control Points')
        plt.pause(interval)

    # Plot the lines between the control points
    for i in range(len(control_points) - 1): 
        plt.plot([control_points[i].x, control_points[i + 1].x], [control_points[i].y, control_points[i + 1].y], 'b-')
        plt.pause(interval)

    # Plot the result points
    # result_points is an array of arrays of arrays of points like [[[Point(1,1)], [Point(2,2)]], [[Point(3,3)], [Point(4,4)]]]
    # array_points is an array of array of points like [[Point(1,1)], [Point(2,2), Point(3,3)]]
    
    for array_points in result_points:
        for j, points in enumerate(array_points):
            for i , point in enumerate(points):
                if (i == len(points) - 1 and j == len(array_points) - 1):
                    plt.plot(point.x, point.y, 'ro', label='Mid Points')
                else:
                    plt.plot(point.x, point.y, 'yo', label='Result Points')
                plt.pause(interval)
            for i in range(len(points) - 1): 
                
                if (i == len(points) - 2 and j == len(array_points) - 2):
                    plt.plot([points[i].x, points[i + 1].x], [points[i].y, points[i + 1].y], 'r-')
                else : 
                    plt.plot([points[i].x, points[i + 1].x], [points[i].y, points[i + 1].y], 'y-')
                plt.pause(interval)

    plt.show()

    plt.figure()
    plt.xlim(min(control_points, key=lambda x: x.x).x - 1, max(control_points, key=lambda x: x.x).x + 1)
    plt.ylim(min(control_points, key=lambda x: x.y).y - 1, max(control_points, key=lambda x: x.y).y + 1)
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.title('Bézier Curve with ' + str(n) + ' Control Points and ' + str(iterations) + ' iteration' + '\n' + 'Execution Time: ' + str(execution_time) + ' ms')

    # Plot the control points
    for point in control_points:
        plt.plot(point.x, point.y, 'go', label='Control Points')
        plt.pause(interval)

    # Plot the lines between the control points
    for i in range(len(control_points) - 1): 
        plt.plot([control_points[i].x, control_points[i + 1].x], [control_points[i].y, control_points[i + 1].y], 'b-')
        plt.pause(interval)


    # Plot the mid points
    for point in mid_points:
        plt.plot(point.x, point.y, 'ro', label='Mid Points')
        plt.pause(interval)


    # Add the first and last control points to the mid points
    mid_points = [control_points[0]] + mid_points + [control_points[-1]]

    # Plot the lines between the mid points
    for i in range(len(mid_points) - 1): 
        plt.plot([mid_points[i].x, mid_points[i + 1].x], [mid_points[i].y, mid_points[i + 1].y], 'r-')
        plt.pause(interval)

    plt.show()
