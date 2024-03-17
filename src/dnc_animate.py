from dnc.generalized_dnc import *
from matplotlib import pyplot as plt
from time import time

start = time()

control_points = [Point(-2, 0), Point(-4, 2), Point(-2, 4), Point(2, 4), Point(4, 2), Point(2, 0)]
# control_points = [Point(0, 0), Point(2, 4), Point(6, 4), Point(8, 0)]
result_points = []
mid_points = []
iterations = 2
n = len(control_points)

create_bezier_points(control_points, result_points, mid_points, iterations, n)

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

end = time()
print(f"Time Taken: {(end - start) * 1000} ms")

plt.figure()
plt.xlim(min(control_points, key=lambda x: x.x).x - 1, max(control_points, key=lambda x: x.x).x + 1)
plt.ylim(min(control_points, key=lambda x: x.y).y - 1, max(control_points, key=lambda x: x.y).y + 1)

# Plot the control points
for point in control_points:
    plt.plot(point.x, point.y, 'go')
    plt.pause(0.3)

# Plot the lines between the control points
for i in range(len(control_points) - 1): 
    plt.plot([control_points[i].x, control_points[i + 1].x], [control_points[i].y, control_points[i + 1].y], 'b-')
    plt.pause(0.3)

# Plot the result points
for array_points in result_points:
    for points in array_points:
        for point in points:
            plt.plot(point.x, point.y, 'bo')
            plt.pause(0.3)
        for i in range(len(points) - 1): 
            plt.plot([points[i].x, points[i + 1].x], [points[i].y, points[i + 1].y], 'r-')
            plt.pause(0.3)

plt.show()