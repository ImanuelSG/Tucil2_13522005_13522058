from dnc.generalized_dnc import *
from matplotlib import pyplot as plt
from time import time

start = time()

# control_points = [Point(-2, 0), Point(-4, 2), Point(-2, 4), Point(2, 4), Point(4, 2), Point(2, 0)]
coordinates = [
    (4, 52), (55, 100), (33, 61), (77, 69), (40, 13),
    (27, 87), (95, 40), (96, 71), (35, 79), (68, 2),
    (98, 3), (18, 93), (53, 57), (2, 81), (87, 42),
    (66, 90), (45, 20), (41, 30), (32, 18), (98, 72),
    (82, 76), (10, 28)
]

# Convert coordinates into Point objects
# control_points = [Point(x, y) for x, y in coordinates]
# control_points = [Point(0, 0), Point(2, 4), Point(4, 2), Point(6, 6), Point(8, 0)]
control_points = [Point(2, 4), Point(-4, -2), Point(6, 1)]
# control_points = [Point(-2,-3), Point(-3,-2), Point(0,-2), Point(1,-3), Point(2,1) ]

result_points = []
mid_points = []
iterations = 8
n = len(control_points)

create_bezier_points(control_points, result_points, mid_points, iterations, n)
end = time()


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


result_points = destructure_array(result_points, n)    


print(f"Time Taken: {(end - start) * 1000} ms")

plt.figure()
plt.xlim(min(control_points, key=lambda x: x.x).x - 1, max(control_points, key=lambda x: x.x).x + 1)
plt.ylim(min(control_points, key=lambda x: x.y).y - 1, max(control_points, key=lambda x: x.y).y + 1)

# Plot the control points
for point in control_points:
    plt.plot(point.x, point.y, 'go')
    plt.pause(0.001)

# Plot the lines between the control points
for i in range(len(control_points) - 1): 
    plt.plot([control_points[i].x, control_points[i + 1].x], [control_points[i].y, control_points[i + 1].y], 'b-')
    plt.pause(0.001)

# Plot the result points
for array_points in result_points:
    for j, points in enumerate(array_points):
        for i , point in enumerate(points):
            if (i == len(points) - 1 and j == len(array_points) - 1):
                plt.plot(point.x, point.y, 'ro')
            else:
                plt.plot(point.x, point.y, 'yo')
            plt.pause(0.001)
        for i in range(len(points) - 1): 
            plt.plot([points[i].x, points[i + 1].x], [points[i].y, points[i + 1].y], 'y-')
            plt.pause(0.001)

plt.show()

plt.figure()
plt.xlim(min(control_points, key=lambda x: x.x).x - 1, max(control_points, key=lambda x: x.x).x + 1)
plt.ylim(min(control_points, key=lambda x: x.y).y - 1, max(control_points, key=lambda x: x.y).y + 1)

# Plot the control points
for point in control_points:
    plt.plot(point.x, point.y, 'go')
    plt.pause(0.001)

# Plot the lines between the control points
for i in range(len(control_points) - 1): 
    plt.plot([control_points[i].x, control_points[i + 1].x], [control_points[i].y, control_points[i + 1].y], 'b-')
    plt.pause(0.001)


# Plot the mid points
for point in mid_points:
    plt.plot(point.x, point.y, 'ro')
    plt.pause(0.001)


# Add the first and last control points to the mid points

mid_points = [control_points[0]] + mid_points + [control_points[-1]]

# Plot the lines between the mid points
for i in range(len(mid_points) - 1): 
    plt.plot([mid_points[i].x, mid_points[i + 1].x], [mid_points[i].y, mid_points[i + 1].y], 'r-')
    plt.pause(0.001)

plt.show()
